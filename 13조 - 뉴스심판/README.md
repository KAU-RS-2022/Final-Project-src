# 13조 : 하리보

------------------------


## Prerequisites

https://drive.google.com/drive/folders/1PMRRWkTosjai4f-7eFvms0DJ2t6hbFhU?usp=sharing

_colab /gdrive 경로에 yolo, resnet 폴더를 위치해 주세요  
img.zip 파일은 /gdrive/resnet/img 위치로 압축을 해제해 주세요_

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
