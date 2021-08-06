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
    samples_per_gpu=16,
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
        ann_file="/data/workspace/dataset/imagenet /imagenet.val.nori.list",
        pipeline=test_pipeline))
evaluation = dict(interval=10, metric='accuracy')

############## 3. quantization setting ###############
quant_transformer = dict(
    type = "mTransformerV2",
    quan_policy=dict(
        Conv2d=dict(type='DSQConv', num_bit_w=4, num_bit_a=4, bSetQ=True),
        Linear=dict(type='DSQLinear', num_bit_w=4, num_bit_a=4)
        ),
    special_layers = dict(
        layers_name = [
            'backbone.conv1',
            'head.fc'],
        convert_type = [dict(type='DSQConv', num_bit_w=8, num_bit_a=8, bSetQ=True, quant_activation=False),
                        dict(type='DSQLinear', num_bit_w=8, num_bit_a=8)]
        )
)

############## 4. optimizer, log, workdir, and etc ###############
# checkpoint saving
checkpoint_config = dict(interval=10)

# optimizer
num_nodes = 9
optimizer = dict(type='SGD', lr=0.001 * num_nodes, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# learning policy
lr_config = dict(
    policy='step',
#    warmup='linear',
#    warmup_iters=3000,
#    warmup_ratio=0.25,
    step=[30, 60, 90])
total_epochs = 100

# logger setting
log_level = 'INFO'
log_config = dict(
    interval=200,
    hooks=[
        dict(type='TextLoggerHook'),
#        dict(type='TensorboardLoggerHook')
])
dist_params = dict(backend='nccl')
work_dir = '/data/workspace/lowbit_classification/workdirs/DSQ/res50/config6_res50_dsq_m9_16_4w4f'
workflow = [('train', 1)]
load_from = './thirdparty/modelzoo/res50.pth'
resume_from = None
cpu_only=False
find_unused_parameters = True
