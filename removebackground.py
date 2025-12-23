import cv2
import numpy as np
count = 0
raw = cv2.VideoCapture("invisable/invasablebackground.mp4")
#loading the video into the program
for i in range(61): # read the video frame by frame
    returnvalue,background = raw.read()
    if returnvalue == False:
        continue
background = np.flip(background,axis = 1)# we are displaying the background over the image to to give the illusion that the image has turned invasable
while raw.isOpened():# until the time the file is open
    returnvalue,image = raw.read()# dividing the video into two parts,# 1 is image second is retrurn value which will contain true or false
    count += 1#move to next frame
    image = np.flip(image,axis = 1)#flip every frame of the video
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)#convert the image colors from bgr to hsv colour codes
    startingrange = np.array([36, 50, 70])
    endingrange = np.array([89, 255, 255])
    mask1 = cv2.inRange(hsv,startingrange,endingrange)
    startingrange2 = np.array([36, 50, 70])
    endingrange2 = np.array([89, 255, 255])
    mask2 = cv2.inRange(hsv,startingrange2,endingrange2)
    mask1 = mask1 + mask2 # we are combining all the shades of red

    mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)# expanding the image so that it will cover the entire red colour
    mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations=1)# it enlargens the image to help the machine detect the image befor making it invisable
    mask2 = cv2.bitwise_not(mask1)#inversing the image so we can focus on none red areas
    result1 = cv2.bitwise_and(background,background,mask= mask1)
    result2 = cv2.bitwise_and(image,image,mask = mask2)
    finaloutput = cv2.addWeighted(result1,1,result2,1,0)
    cv2.imshow("invisable man",finaloutput)
    a = cv2.waitKey(10)
    if a == 27:
        break