###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv




########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))




############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    angle = 0.00
    #1 find number of circles whose origin is 511,511 in image and get 2nd,3rd circle co-ordinates
    b,g,r = 32,30,30
    c=0
    for i in range(1,511):
        if ip_image[i-1,511,0]!=ip_image[i,511,0]!=ip_image[i+1,511,0] and ip_image[i-1,511,0]!=ip_image[i,511,0]!=ip_image[i+1,511,0] and ip_image[i-1,511,0]!=ip_image[i,511,0]!=ip_image[i+1,511,0]:
            c=c+1
            for j in range(0,10):
                ip_image[i+j,511,:]=0,255,0
        if c ==2 :
            x3,y3 = 511,i
        if c ==3 :
            x4,y4 = 511,i
    
    #2 find green and red circle's all co - ordinates
    green_dot_row=[]
    green_dot_col=[]
    red_dot_row=[]
    red_dot_col=[]
    rad1=int(math.sqrt(511-y3)**2)
    rad2=int(math.sqrt(511-y4)**2)
    for i in range(0,1024):
        for j in range(0,1024):
            rad_cal=math.sqrt((i-511)**2+(j-511)**2)
            if rad_cal>=rad2 and rad_cal<=rad1:
                if ip_image[i,j,0]==0 and ip_image[i,j,1]==255 and ip_image[i,j,2]==0:
                    green_dot_row.append(i)
                    green_dot_col.append(j)
                if ip_image[i,j,0]==0 and ip_image[i,j,1]==0 and ip_image[i,j,2]==255:
                    red_dot_row.append(i)
                    red_dot_col.append(j)    

    #3 find average co-ordinates of red and green
    avg_g_row = int(sum(green_dot_row)/len(green_dot_row))
    avg_g_col = int(sum(green_dot_col)/len(green_dot_col))
    avg_r_row = int(sum(red_dot_row)/len(red_dot_row))
    avg_r_col = int(sum(red_dot_col)/len(red_dot_col))
    
    g_y , g_x = avg_g_row,avg_g_col
    r_y , r_x = avg_r_row,avg_r_col

    #4 set co-ordinates of origin
    origin_x=511
    origin_y=511
    #5 find distance from each of each side of trangle
    D_GO=math.sqrt((origin_x-g_x)**2+(origin_y-g_y)**2)
    D_RO=math.sqrt((origin_x-r_x)**2+(origin_y-r_y)**2)
    D_RG=math.sqrt((r_x-g_x)**2+(r_y-g_y)**2)
       
    #6 find all angles of trangle
    angle_RG = math.acos((D_RO**2+D_GO**2-D_RG**2)/(2*D_RO*D_GO))
    angle_RO = math.acos((D_RG**2+D_GO**2-D_RO**2)/(2*D_RG*D_GO))
    angle_GO = math.acos((D_RO**2+D_RG**2-D_GO**2)/(2*D_RO*D_RG))
    
    angle=angle_RG*180/3.14
    ## Your Code goes here
    ###########################
    cv2.imshow("window", ip_image)
    cv2.waitKey(0);
    return angle




    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A = process(ip_image)
        ## saving the output in  a list variable
        line.append([str(i), image_name , str(A)])
        ## incrementing counter variable
        i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
