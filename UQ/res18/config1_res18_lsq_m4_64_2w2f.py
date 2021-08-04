############## 1. Model ###############
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNet',
        depth=18,
        num_stages=4,
        out_indices=(3, ),
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=512,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))

############## 2. Dataset setting ###############
# dataset settings
dataset_type = 'ImageNetV1'
img_norm_cfg = dict(
    mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], to_rgb=True)
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
    samples_per_gpu=128,
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
        Conv2d=dict(type='APOTQuantConv2d', bit_w=2, bit_a=2, power=False),
        Linear=dict(type='APOTQuantLinear', bit_w=2, bit_a=2, power=False)
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
optimizer = dict(type='SGD', lr=1e-3 * num_nodes, momentum=0.9, weight_decay=0.5e-4)
optimizer_config = dict(grad_clip=None)

# learning policy
# lr_config = dict(
#     policy='step',
#     step=[20, 40, 60, 80, 100])


lr_config = dict(
    policy='CosineAnnealing',
    min_lr=0,
    warmup='linear',
    warmup_iters=500,
    warmup_ratio=0.25)
total_epochs = 150

# logger setting
log_level = 'INFO'
log_config = dict(
    interval=10,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHookV2')
])
dist_params = dict(backend='nccl')
work_dir = '/data/work_dirs/UniformQuant/res18/config2_res18_UQ_m2_128_w2f2'

workflow = [('train', 1)]

load_from = '/data/work_dirs/UniformQuant/res18/config3_res18_UQ_m2_128_w3f3/latest.pth'
resume_from = '' 
find_unused_parameters = True
sycbn = False