############## 1. Model ###############
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(3, ),
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=2048,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))

############## 2. Dataset setting ###############
# dataset settings
dataset_type = 'ImageNetV1'
img_norm_cfg = dict(
    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], to_rgb=True)
        # mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromNori'),
    dict(type='RandomResizedCrop', size=224),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]
test_pipeline = [
    dict(type='LoadImageFromNori'),
    dict(type='Resize', size=(256, -1)),
    dict(type='CenterCrop', crop_size=224),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]
data = dict(
    samples_per_gpu=32,
    workers_per_gpu=3,
    train=dict(
        type=dataset_type,
        data_prefix= None,
        ann_file="/data/workspace/dataset/imagenet/imagenet.train.nori.list",
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_prefix=None,
        ann_file="/data/workspace/dataset/imagenet/imagenet.val.nori.list",
        pipeline=test_pipeline),
    test=dict(
        # replace `data/val` with `data/test` for standard test
        type=dataset_type,
        data_prefix= None,
        ann_file="/data/workspace/dataset/imagenet/imagenet.val.nori.list",
        pipeline=test_pipeline))
evaluation = dict(interval=2, metric='accuracy')

############## 3. quantization setting ###############
quant_transformer = dict(
    type='QuanTransformer',
    quan_policy=dict(
        Conv2d=dict(type='APOTQuantConv2d', bit_w=3, bit_a=3),
        Linear = dict(
            type = "EightBitQuantLinear")
        ),
    special_layers = dict(
        layers_name = [
            'backbone.conv1',
            'head.fc'],
        convert_type = [dict(type='EightBitQuantConv'),
                        dict(type='EightBitQuantLinear')]
            ))

############## 3. optimizer, log, workdir, and etc ###############
# checkpoint saving
checkpoint_config = dict(interval=2)

# optimizer
num_nodes = 3
optimizer = dict(type='SGD', lr=1e-3 * num_nodes, momentum=0.9, weight_decay=0.25e-4)
optimizer_config = dict(grad_clip=None)

# learning policy
# lr_config = dict(
#     policy='step',
# #    warmup='linear',
# #    warmup_iters=3000,
# #    warmup_ratio=0.25,
#     step=[30, 60, 90])
# total_epochs = 100

lr_config = dict(
policy='CosineAnnealing',
min_lr=0,
warmup='linear',
warmup_iters=500,
warmup_ratio=0.25)

total_epochs = 120


# logger setting
log_level = 'INFO'
log_config = dict(
    interval=10,
    hooks=[
        dict(type='TextLoggerHook'),
#        dict(type='TensorboardLoggerHook')
])
dist_params = dict(backend='nccl')
work_dir = '/data/work_dirs/APOT/res50/config2_res50_lsq_m2_64_3w3f_new'
workflow = [('train', 1)]

load_from = 'thirdparty/res50_apot_4w4f.pth'
resume_from = ''
cpu_only=True
find_unused_parameters = True
sycbn = False
