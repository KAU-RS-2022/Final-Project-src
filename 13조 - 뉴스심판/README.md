# 13조 : 하리보

------------------------


## Prerequisites

https://drive.google.com/drive/folders/1PMRRWkTosjai4f-7eFvms0DJ2t6hbFhU?usp=sharing

_google_colab 환경을 기반으로 하였습니다.   
/gdrive 경로에 yolo, resnet 폴더를 위치해 주세요  
img.zip 파일은 /gdrive/resnet 안에 압축을 해제해 주세요_
<br/>

_based on google_colab env.   
please put yolo, resnet folder in path '/gdrive'  
please unzip img.zip file in /gdrive/resnet_

<br/>

### yolo folder

+ custom.names
  + names of classes we trained
+ custom.data
  + path for .names file
+ yolov4-custom.cfg
  + set img size to 64x64 and modified to fit our class number
+ yolov4-custom_last.weights
  + weights file we trained in custom
+ image.c
  + modified to save labeled images
<br/>

### resnet folder

+ img.zip
  + image files we used
+ input_list.txt
  + names of images files in /img
+ train_df.csv
  + specific data of image files we used
+ image_emb.npy
  + pre-trained model



<br/>

## Yolov4.ipynb

  + Yolo - Get Yolov4
    + git clone from https://github.com/AlexeyAB/darknet and follow official instructions
  + Yolo - Get Weight and Files
    + mount goolge drive and copy our custom files
    + make result_img dir for saving cropped images
  + Yolo - Auto Exe
    + put arguments in code in advance to make it convenient to execute darknet with original weights
  + Yolo - Test
    + execute darknet with our custom weights 
  <br/>

  + ResNet - Get Files
    + make test dir and copy files from gdrive
  + ResNet - Import
    + import necessary libraries
  + ResNet - Data Preprocessing
    + extract data of categories we are going to use from original csv file
  + ResNet - Pretrained Model
    + embedding process
  + ResNet - Get Similarity
    + get similar images from input file
  + ResNet - Test
    + execute codes 
  <br/>

  + Final
    + run final model
    <br/>
    
    + "OSError: [Errno 5] Input/output error:"  
    https://research.google.com/colaboratory/faq.html#drive-timeout  
    img 폴더에 사진이 너무 많아서 생기는 gdrive 오류입니다. 현 섹션을 다시 실행하면 정상 작동 합니다.  
    The error comes from gdrive because there are too many files in 'img' folder. It will be automatically solved if you run this section again
