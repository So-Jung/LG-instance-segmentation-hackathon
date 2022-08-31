# LG 입자 형태 분석 대회

## 대회 개요 및 task
: 데이터셋을 활용해서 유체상의 떠다니는 유동입자의 윤곽을 검출하는 것으로 주 task는 instance segmentation이다. 

: The major task is an instance segmentation to detect the outline of floating particles in a fluid using a dataset.

#### instance segmentation vs. sementic segmentation
: 대회 참여하기에 앞서, 대회의 주 task인 instance segmentation에 대해 알아보는 것이 중요했다. segmentation은 이미지의 pixel 단위로 각 영역을 분리하는 방법인데, 크게 두가지로 나뉜다.
1. Semantic segmentation 
  : 한 이미지 내에 class의 위치를 인식(localization)하고, 판별(classification)하는 접근법이다.
2. Instance segmentation
  : Sementic segmentation과 비슷하지만, 같은 class 이더라도 따로 구분을 한다. 이것은 각 object의 위치를 정확히 식별하는 object detection의 접근법을 보여준다.
  
 아래의 예시를 보면, semantic segmentation 경우 사람이라는 객체 구분은 없지만 사람의 위치를 인식하고 판별한다. 반면에, instance segmentation은 객체를 사람이라 인식하고, 같은 class이더라도 "사람1, 사람2, 사람3 등", 각 object의 위치를 정확히 식별한다. 
 
![image](https://user-images.githubusercontent.com/106142512/184824975-ac292126-28ad-43d9-8abd-a4c98f541e8c.png)

#### 

## Directory

### mmdetection
 - "mask scoring rcnn" folder 
    - model: Mask Scoring R-CNN /  backbone: ResNeXt 101, ResNet stikes back
    - optimzer : Adadelta
    
    - ms_rcnn_x101_64x4d_fpn_1x_coco.py 와 mask_scoring_config.py 두 파일을 
    
 - "cascade mask rcnn" folder    
    - model: Cascade Mask R-CNN / backbone: GCNet, RegNet, PVT, Generalized Attention, ConvNeXt, HRNet
    - optimizer: SGD, ASGD, Adadelta, Adam, AdamW, Nadam, Radam, Adagrad, Adamax, RMSprop
    
### _data_
- _EDA.ipynb_
- dataset : image + annotation file
  - image : 프레임 단뒤로 추출된 유동입자 이미지.
  - annotation file : 각 입자의 윤곽을 레이블링한 데이터.
- _data augmentation_ : mm detection에서 제공하는 augmentation 라이브러리 경우, 이미지의 증강 보다는 기존의 이미지를 일정 확률로 바꿔주는 기능(flip, rotation, etc)을 한다(transform). transform의 기능 보다는 이미지 증강이 성능 향상에 도움이 될 것 같아서 offline augmentation을 진행했다. 
 
### _ppt_
- 정리 발표 자료


# LG Particle Instance Segmentation Hakathon

The major task of this hakathos is **"_instance segmentation_"** to detect the outline of floating particles in a fluid using a dataset. 
Instance segmentation is one of the major types of image segmentation. Image segmentation is the process of dividing an image into different regions based on the charactersitics of pixels to identify objects or boundaries to simplify an image and more efficiently analyze it. 

__Image Segmentaion__

(A) _Semantic Segmentation_

Semantic segmentation is the task of classifying each pixel in an image from a predefined set of classes. Objects of the same class cannot be distinguished.        Therefore, if there are objects overlapping, it is considered as one.  
    
(B) _Instance Segmentation_

Instance segmentation is a special form of image segmentation that deals with detecting instances of objects and demarcating their boundaries.
It goes further from the semantic segmentation and distinguishes even if it is the same class. Therefore, the problem in the semantic segmentation, which does       not distinguish each object when the objects overlap, can be solved through instance segmentation. 

__MM detection__ is a Python toolbox built as a codebase exclusively for object detection and instance segmentation tasks.
It is a built in a modular way with PyTorch implementation. 
There are numerous methods available for object detection and instance segmentation collected from various well-acclaimed models.
It enables quick training and inference with quality. 
On the other hand, the toolbox contains weights for more than 200 pre-trainied networks, making the toolbox an instance solution in the object detection domain.

MM detection can be a powerful tool in 3 ways:
- In MM detection, various models and backbones are modular, making it easy to construct a customized object detection framework by combining different modules. 
- The optimizer and learning rate schedule provided by PyTorch can be applied.
- Training speed is faster than other codebases, such as Detectron2 or SimpleDet since all basic bbox and mask operation run on GPUs.
- It provides numerous pretrained models. 
