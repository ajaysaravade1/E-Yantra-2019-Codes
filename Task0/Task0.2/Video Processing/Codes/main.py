import cv2 as cv
import numpy as np
import os

def partA():
	#1  save each .mp4 file name with extention into list
    for subdir,dir,files in os.walk('..//Videos//'):
    	for file in files:
    		if file.endswith('.mp4'):
	    		vid_name=file
	#2 find Videos path and set file path
    vid_path=os.path.abspath(os.path.join('','..//Videos//'))
    vid_path=vid_path + '\\'+vid_name

    #3 get path of Generated folder if Generated folder not present then create Generated folder
    gen_path =os.path.abspath(os.path.join('','..//Generated//'))
    if not os.path.exists(gen_path):
    	os.mkdir(gen_path)
    #4 start video cature and use i variable to get count of frames
    video = cv.VideoCapture(vid_path)
    c=0
    #5 read each frame till 126th and store this as image into Generated folder
    # frame rate is 25fps, so each second have 25 frames, so 5*25 =125th which is end of 5th frame, 
    # so 126th frame will give start fo 6th second image
    # but we start count from 0 so we will get 126th frame at index 125 

    while True:
    	check, frame = video.read()
    	if c ==125:
    		cv.imwrite(gen_path+"//frame_as_6.jpg",frame)
    		break
    	c=c+1
    video.release()

def partB():
    #1 find frame_as_6.jpg path
    gen_path=os.path.abspath(os.path.join('','..//Generated//'))
    frame_path=gen_path + '\\frame_as_6.jpg'
    
    #2 read frame_as_6.jpg with b,g,r channel
    img = cv.imread(frame_path,1)

    #3 set Green and Blue channel to 0
    img[:,:,1]=0
    img[:,:,0]=0

    #4 save image to Generated folder
    cv.imwrite(gen_path+"\\frame_as_6_red.jpg",img)


partA()
partB()