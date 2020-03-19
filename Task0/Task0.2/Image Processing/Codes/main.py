import cv2 as cv
import pandas as pd
import numpy as np
import os
def partA():
    #1 save each file name with extention into list
	imgFileName = []
	for subdir, dirs, files in os.walk('..//Images/'):
	    for file in files:
	    	if(file.endswith('.jpg')):
	      		imgFileName.append(file)

	#2 find Images directory path
	imgDirPath=(os.path.abspath(os.path.join("", os.pardir)))
	imgDirPath=imgDirPath+"\\Images\\"

	#3 create empty list for storing data 
	dataList = []
	
	#4 itrate for each file name and get data of each row 
	for iName in imgFileName:
		
		#5 read each image file from Images directory into open cv format (array format) as color image
		img = cv.imread(imgDirPath+iName,1)
		#6 read height, width and no. of channels of image
		height,width,channel = img.shape
		
		#6 intensity value at pixel location (m/2 ,n/2) for each channel
		row = int((height-1)/2)
		col = int((width-1)/2)
		b,g,r = img[row,col]
		
		#7 add each row of into dataList with image name, height of image,width of image, intensity value of channel b,intensity value of channel g,intensity value of channel r
		dataList.append([iName,height,width,channel,b,g,r])

	#8 convert the dataList of type list to type DataFrame to store file into csv
	df = pd.DataFrame(data = dataList)
	#9 get Generated folder path
	genPath =imgDirPath.replace("\\Images\\","")+"\\Generated\\"
	
	#10 get path of Generated folder if Generated folder not present then create Generated folder
	gen_path =os.path.abspath(os.path.join('','..//Generated//'))
	if not os.path.exists(gen_path):
		os.mkdir(gen_path)

	#11 store data frame into csv file
	df.to_csv(genPath+"stats.csv",index=False,header=False)


def partB():
    #1 read cat.jpg
	cat_img = os.path.abspath(os.path.join("","..//Images//cat.jpg"))
	img = cv.imread(cat_img,3)

	#2 set channels to blue and green to 0 
	img[:, :, 0] = 0
	img[:, :, 1] = 0

	#3 save image as cat_red.jpg in Generated folder 
	write_path = os.path.abspath(os.path.join("","..//Generated//cat_red.jpg"))
	cv.imwrite(write_path,img)

def partC():
	#1 read flowers.jpg as b g r from Images folder 
	flowers_img = os.path.abspath(os.path.join("","..//Images//flowers.jpg"))
	img = cv.imread(flowers_img,3)
	#2 create arrray of 0's with height X width X 1 dimention this will create 1 channel
	alpha_channel = np.zeros((img.shape[0],img.shape[1],1),dtype=img.dtype)

	#3 set each value of alpha_channel to 0.5, we can set the value between 0 to 255 for transparency between 0% to 100%
	#  To set transparency 50% we neet set alpha_channel to 127
	alpha_channel=alpha_channel+0.5
	#4 merge image and alpha_channel to newimg
	newimg = np.c_[img,alpha_channel]

	#5 save newimg as flowers_alpha.jpg in Generated folder
	write_path = os.path.abspath(os.path.join("","..//Generated//flowers_alpha.png"))
	cv.imwrite(write_path,newimg)
def partD():
    #1 read image horse.jpg from Images folder 
	horse_img = os.path.abspath(os.path.join("","..//Images//horse.jpg"))
	img = cv.imread(horse_img,3)
	#2 get BGR values of image
	b , g , r =cv.split(img)
	#3 find intensity using formula 𝐼 = ((0.3 × 𝑅𝑒𝑑 𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡)+ (0.59 × 𝐺𝑟𝑒𝑒𝑛 𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡) + (0.11 × 𝐵𝑙𝑢𝑒 𝐶𝑜𝑚𝑝𝑜𝑛𝑒𝑛𝑡))
	intensity = ((0.3 * r) + (0.59 * g) + (0.11 * b))
	#4 save image at Generated folder 
	write_path = os.path.abspath(os.path.join("","..//Generated//horse_gray.jpg"))
	cv.imwrite(write_path,intensity)

partA()
partB()
partC()
partD()