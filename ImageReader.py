import numpy as np
import cv2
from cv2 import VideoCapture,imshow,waitKey,resize,INTER_AREA,destroyWindow
import sys
import time


def captureImage(isShow):
	cam_port = 2
	cam = VideoCapture(cam_port)
	result, image = cam.read()
	image = image[0:480, 80:560]
	if result and isShow:
		imshow("Test", image)
		waitKey(0)
		destroyWindow("Test")
	return image;



def captureVideo():
	print("Starting capture")
	cam_port = 2
	cam = VideoCapture(cam_port)

	if not cam.isOpened():
		raise IOError("Cannot open webcam")

	while True:
		ret,image = cam.read()
		image = resize(image, None, fx=1, fy=1, interpolation=INTER_AREA)
		image = image[0:480, 80:560]
		imshow("test",image)
		c = waitKey(1)
		if c == 27:
			break

	cam.release()
	cv2.destroyAllWindows()



# Used for MSE formulahttps://pyimagesearch.com/2014/09/15/python-compare-two-images/
def meanSquareError(image1, image2):
	err = np.sum((image1.astype("float") - image2.astype("float")) ** 2)
	err /= float(image1.shape[0] * image1.shape[1])
	print(err)
	return err;

def compareChange(img1, img2):
	diff = img1.copy()
	cv2.absdiff(img1,img2,diff)
	diffgrey = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
	for i in range(0,1):
		dilated = cv2.dilate(diffgrey.copy(),None, iterations= i+1)

	(T,thresh) = cv2.threshold(dilated,50,255,cv2.THRESH_BINARY)


	return(thresh)

def showImage(image):
	imshow("Test", image)
	waitKey(0)
	destroyWindow("Test")

def chessImage(image):
	#image = cv2.resize(image, None, fx=.0125, fy=.016666, interpolation=INTER_AREA)
	image = cv2.resize(image, None, fx=.0166666, fy=.016666, interpolation=INTER_AREA)
	print(image)
	thresh = findTwoMax(image)
	(T,thresh) = cv2.threshold(image,150,255,cv2.THRESH_BINARY)
	print(thresh)
	return thresh

def findTwoMax(image):
	first = 0
	second = 0

	index1 = [0,0]
	index2 = [0,0]

	for i in range(0,8):
		for j in range (0,8):
			if(image[i][j] >= second):
				second = image[i][j]
				if(second > first):
					temp = first
					tempindex = index1
					first = second
					second = temp
					index1 = [i,j]
					index2 = tempindex
				else:
					index2 = [i,j]



	print(index1)
	print(index2)
	image[index1[0]][index1[1]] = 255
	image[index2[0]][index2[1]] = 255
	#print(image)

	return image

def validToCompare(image):
	image = cv2.resize(image, None, fx=.0166666, fy=.016666, interpolation=INTER_AREA)
	squaresMore = 0
	squaresLess = 0
	for i in image:
		for j in i:
			if(j > 100):
				squaresMore += 1
			if(j < 20):
				squaresLess +=1
	print(image)
	print("high change")
	print(squaresMore)
	print("low change")
	print(squaresLess)

	if(squaresMore > 1 or (squaresLess == 64 or squaresLess < 60)):
		return False
	return True

def runTurnWithError():
	take1 = captureImage(False)
	take2 = captureImage(False)

	resultimage = compareChange(take1,take2)

	while(not validToCompare(resultimage)):
		time.sleep(5)
		take2 = captureImage(False)
		resultimage = compareChange(take1,take2)

	chessImageF = chessImage(resultimage)
	return(chessImageF)

	

def runTurn():
	take1 = captureImage(True)
	take2 = captureImage(True)
	cv2.imwrite("take1.png", take1)
	cv2.imwrite("take2.png", take2)

	resultimage = compareChange(take1,take2)
	cv2.imwrite("compare.png", resultimage)
	showImage(resultimage)
	chessImageF = chessImage(resultimage)
	showImage(chessImageF)
	return(chessImageF)


if __name__ == '__main__':
	if(len(sys.argv) != 1):
		if(sys.argv[1] == "capture"):
			captureVideo()
	else:
		runTurnWithError()


	#meanSquareError(take1,take2)
