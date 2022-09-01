 #사용할 모델 선택
_base_ = '/content/lg_test/mmdetection/configs/cascade_rcnn/cascade_mask_rcnn_x101_64x4d_fpn_1x_coco.py'

# 데이터 폴더 설정 및 데이터 경로 수정 - coco_instance.py 수정
data_root = 'data/dataset/'
classes = ('Normal',)

data = dict(
    samples_per_gpu=1,
    workers_per_gpu=0,
    train=dict(
      img_prefix=data_root + "train/",
      classes = classes,
      ann_file=data_root + "label(polygon)_train.json"
),
    val=dict(
        img_prefix=data_root + "train/",
        classes = classes,
        ann_file=data_root + "label(polygon)_train.json"
),
    test=dict(
        img_prefix=data_root + "test/",
        classes = classes,
        ann_file=data_root + "test.json"
)
)

# 평가 방법 - coco_instance.py 수정
evaluation = dict(interval=1, save_best='segm_mAP', metric=['bbox', 'segm'])

# log 저장 위치 - default_runtime.py 수정
checkpoint_config = dict(interval=1,out_dir='/content/drive/MyDrive/lg_output/MS_rsb_adadelta_15e/')

# 사전 가중치 사용 - default_runtime.py 수정
load_from = 'checkpoint/cascade_mask_rcnn_x101_64x4d_fpn_1x_coco_20200203-9a2db89d.pth'

# batch size 설정 - default_runtime.py 수정
auto_scale_lr = dict(enable=True, base_batch_size=16)

# epoch 설정 - schedule_1x.py 수정
runner = dict(type='EpochBasedRunner', max_epochs=15)

# 기타 직접 파일에서 수정 
# - schedule_1x.py : optimizer = dict(type='Adadelta', lr=1.0, rho=0.9, eps=1e-06, weight_decay=0, foreach=None, maximize=False) "SGD -> Adadelta"
# - default_runtime.py : auto_scale_lr = dict(enable=True, base_batch_size=16) "False -> True"
# - ms_rcnn_r50_fpn_1x_coco.py / mask_rcnn_r50_fpn.py : num_classes:1 "80 -> 1"
# - coco_instance.py : train_pipeline > image_scale = (1280, 1024) / test_pipeline > image_scale = (1280, 1024) "(1333, 800 -> (1280, 1024)"