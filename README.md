# LG 입자 형태 분석 대회

## 대회 개요 및 task
데이터셋을 활용해서 유체상의 떠다니는 유동입자의 윤곽을 검출하는 것으로 주 task는 instance segmentation이다. 
The major task is an instance segmentation to detect the outline of floating particles in a fluid using a dataset.

#### instance segmentation vs. sementic segmentation
1. Sementic segmentation 
  : 한 이미지 내에 class의 위치를 인식(localization)하고, 판별(classification)하는 접근법이다.
2. Instance segmentation
  : Sementic segmentation과 비슷하지만, 같은 class 이더라도 따로 구분을 한다. 이것은 각 object의 위치를 정확히 식별하는 object detection의 접근법을 보여준다. 


![image](https://user-images.githubusercontent.com/106142512/184824975-ac292126-28ad-43d9-8abd-a4c98f541e8c.png)
## Directory

### _data_
- EDA.ipynb
- dataset : image + annotation file
  - image : 프레임 단뒤로 추출된 유동입자 이미지
  - annotation file : 각 입자의 윤곽이 레이블링
 
### _ppt_
- 정리 발표 자료

이미지 업로드(드래그) -> ![날지않아](https://user-images.githubusercontent.com/106142512/178384994-42cf94d8-89f1-4049-9375-923d709d5e5e.jpg)

