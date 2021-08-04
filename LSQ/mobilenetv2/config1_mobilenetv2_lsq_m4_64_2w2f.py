############## 1. Model ###############
model = dict(
    type='ImageClassifier',
    backbone=dict(type='MobileNetV2', widen_factor=1.0),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=1280,
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
    samples_per_gpu=64,
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
evaluation = dict(interval=1, metric='accuracy')

############## 3. quantization setting ###############
quant_transformer = dict(
    type = "mTransformerV2",
    quan_policy=dict(
        Conv2d=dict(type='LSQConv2d', nbits_w=2, nbits_a=2, debug = False),
        # Conv2d=dict(type='LSQDPlusConv2d', 
                    # nbits_w=4,
                    # init_method_w = 4,
                    # customer_backward_w = False, 
                    # add_offset_w = True, 
                    # wquant_error_loss = True,
                    # nbits_a=4,
                    # init_method_a = 4,
                    # customer_backward_a = False,
                    # add_offset_a = True, 
                    # momentum = 1.0, 
                    # auto_signed = True,
                    # debug = False),
      ),
    special_layers = dict(
        layers_name = [
            'backbone.conv1.conv',
            'head.fc'],
        convert_type = [dict(type='LSQConv2d', nbits_w=8, nbits_a=8, quant_activation=False, debug = True),
                        dict(type='LSQLinear', nbits_w=8, nbits_a=8)]
        )
)

############## 3. optimizer, log, workdir, and etc ###############
# checkpoint saving
checkpoint_config = dict(interval=2)

# optimizer
num_nodes = 3
optimizer = dict(type='SGD', lr=0.001 * num_nodes, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)

# learning policy
# lr_config = dict(
#     policy='CosineAnnealing',
#     min_lr=0,
#     warmup='linear',
#     warmup_iters=500,
#     warmup_ratio=0.25)
# total_epochs = 180

lr_config = dict(
    policy='step',
#    warmup='linear',
#    warmup_iters=3000,
#    warmup_ratio=0.25,
    step=[30, 60, 90, 120, 150, 180])
total_epochs = 180
# logger setting
log_level = 'INFO'
log_config = dict(
    interval=10,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHookV2', cmp_multilayer_dist = True)
])
dist_params = dict(backend='nccl')
work_dir = '/data/work_dirs/LSQ/mobilenet/config1_mobilenetv2_lsq_m3_32_2w2f_new'
workflow = [('train', 1)]

load_from = 'thirdparty/modelzoo/MobileNetV2.pth'
resume_from = None 
cpu_only=True
find_unused_parameters = True
sycbn = False
