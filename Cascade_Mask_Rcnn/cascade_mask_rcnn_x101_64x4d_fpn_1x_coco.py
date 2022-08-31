_base_ = './cascade_mask_rcnn_r50_fpn_1x_coco.py'
# ResNeXt 101
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

# # backbone 변경 예시

# # ResNet strike back
# checkpoint = 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb256-rsb-a1-600e_in1k_20211228-20e21305.pth'  # noqa
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

# # GCNet
# model = dict(
#     backbone=dict(
#         type='ResNeXt',
#         depth=101,
#         groups=64,
#         base_width=4,
#         num_stages=4,
#         out_indices=(0, 1, 2, 3),
#         frozen_stages=1,
#         norm_cfg=dict(type='SynBN', requires_grad=True), 
#         norm_eval=Fasle,
#         style='pytorch',
#         init_cfg=dict(
#             type='Pretrained', checkpoint='open-mmlab://resnext101_64x4d')))

# # RegNet
# model = dict(
#     backbone=dict(
#         type='RegNet',
#         arch='regnetx_4.0gf',
#         out_indices=(0, 1, 2, 3),
#         frozen_stages=1,
#         norm_cfg=dict(type='BN', requires_grad=True),
#         norm_eval=True,
#         style='pytorch',
#         init_cfg=dict(
#             type='Pretrained', checkpoint='open-mmlab://regnetx_4.0gf')),
#     neck=dict(
#         type='FPN',
#         in_channels=[80, 240, 560, 1360],
#         out_channels=256,
#         num_outs=5))

# # PVT
# model = dict(
#     type='RetinaNet',
#     backbone=dict(
#         _delete_=True,
#         type='PyramidVisionTransformerV2',
#         embed_dims=32,
#         num_layers=[2, 2, 2, 2],
#         init_cfg=dict(checkpoint='https://github.com/whai362/PVT/'
#                       'releases/download/v2/pvt_v2_b0.pth')),
#     neck=dict(in_channels=[32, 64, 160, 256]))

# # Generalized Attention
# model = dict(
#     backbone=dict(plugins=[
#         dict(
#             cfg=dict(
#                 type='GeneralizedAttention',
#                 spatial_range=-1,
#                 num_heads=8,
#                 attention_type='1111',
#                 kv_stride=2),
#             stages=(False, False, True, True),
#             position='after_conv2')
#     ]))

# # ConvNext
# ## please install mmcls>=0.22.0
# ## import mmcls.models to trigger register_module in mmcls
# custom_imports = dict(imports=['mmcls.models'], allow_failed_imports=False)
# checkpoint = 'https://download.openmmlab.com/mmclassification/v0/convnext/downstream/convnext-small_3rdparty_32xb128-noema_in1k_20220301-303e75e3.pth'  # noqa

# model = dict(
#     backbone=dict(
#         _delete_=True,
#         type='mmcls.ConvNeXt',
#         arch='small',
#         out_indices=[0, 1, 2, 3],
#         drop_path_rate=0.6,
#         layer_scale_init_value=1.0,
#         gap_before_final_norm=False,
#         init_cfg=dict(
#             type='Pretrained', checkpoint=checkpoint,
#             prefix='backbone.')))

# # HRNet
# model = dict(
#     backbone=dict(
#         extra=dict(
#             stage2=dict(num_channels=(18, 36)),
#             stage3=dict(num_channels=(18, 36, 72)),
#             stage4=dict(num_channels=(18, 36, 72, 144))),
#         init_cfg=dict(
#             type='Pretrained', checkpoint='open-mmlab://msra/hrnetv2_w18')),
#     neck=dict(type='HRFPN', in_channels=[18, 36, 72, 144], out_channels=256))
