# LG 입자 형태 분석 대회

## 대회 개요 및 task
데이터셋을 활용해서 유체상의 떠다니는 유동입자의 윤곽을 검출하는 것으로 주 task는 instance segmentation이다. 
The major task is an instance segmentation to detect the outline of floating particles in a fluid using a dataset.

#### instance segmentation vs. sementic segmentation
: 대회 참여하기에 앞서, 대회의 주 task인 instance segmentation에 대해 알아보는 것이 중요했다. segmentation은 이미지의 pixel 단위로 각 영역을 분리하는 방법인데, 크게 두가지로 나뉜다.
1. Semantic segmentation 
  : 한 이미지 내에 class의 위치를 인식(localization)하고, 판별(classification)하는 접근법이다. 예를 들어 강아지 2마리, 고양이 2마리가 있다고 하면, semantic segmentation 같은 경우, "강아지, 강아지, 고양이, 고양이"가 판별된다.
2. Instance segmentation
  : Sementic segmentation과 비슷하지만, 같은 class 이더라도 따로 구분을 한다. 이것은 각 object의 위치를 정확히 식별하는 object detection의 접근법을 보여준다. 위와 같은 예시로 들자면, intance segmentation 같은 경우, "강아지1, 강아지2, 고양이1, 고양이2" 로 판별된다. 


![image](https://user-images.githubusercontent.com/106142512/184824975-ac292126-28ad-43d9-8abd-a4c98f541e8c.png)

## Directory

### mmdetection
  - training

### _data_
- EDA.ipynb
- dataset : image + annotation file
  - image : 프레임 단뒤로 추출된 유동입자 이미지.
  - annotation file : 각 입자의 윤곽을 레이블링한 데이터.
 
### _ppt_
- 정리 발표 자료

