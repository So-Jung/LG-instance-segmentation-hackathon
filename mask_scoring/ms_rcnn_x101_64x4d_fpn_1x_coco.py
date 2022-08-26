_base_ = './ms_rcnn_r50_fpn_1x_coco.py'

# backbone = ResNeXt
model = dict(
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch',
        init_cfg=dict(
            type='Pretrained', checkpoint='open-mmlab://resnext101_64x4d')))

# # backbone = ResNet Strike Back
# checkpoint = 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb256-rsb-a1-600e_in1k_20211228-20e21305.pth' 

# model = dict(
#     backbone=dict(
#         type='ResNeXt',
#         depth=101,
#         groups=64,
#         base_width=4,
#         num_stages=4,
#         out_indices=(0, 1, 2, 3),
#         frozen_stages=1,
#         norm_cfg=dict(type='BN', requires_grad=True),
#         style='pytorch',
#         init_cfg=dict(
#             type='Pretrained', prefix='backbone.', checkpoint=checkpoint)))

