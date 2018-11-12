from pynput.keyboard import Key, Controller
import time
import pyautogui
import cv2
import numpy as np
import copy 

NUMBER_OF_IMAGES = 20
SAMPLE_TIME = 0.2

class Vision():

	def __init__(self):
		self.keyboard = Controller()
		return
	

	def simulate_space_bar(self):
		time.sleep(2)
		for i in range(100):
			self.keyboard.press(" ")
			self.keyboard.release(" ")
			time.sleep(0.12)

	def take_screen_shot(self):
		return pyautogui.screenshot()

	def get_train_imgs(self):
		screen = []
		for i in range(NUMBER_OF_IMAGES):
			time.sleep(SAMPLE_TIME)
			screen.append(self.take_screen_shot())

		for i in range(NUMBER_OF_IMAGES):
			image = cv2.cvtColor(np.array(screen[i]), cv2.COLOR_RGB2BGR)
			cv2.imwrite('images/'+str(i)+'.png', image)
	
	def get_all_parameters(self):
		for i in range(NUMBER_OF_IMAGES):
			self.take_img_parameters(i)


	def take_img_parameters(self, number):
		img = cv2.imread('images/'+str(number)+'.png')
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
		lower = np.array([40,50,50])	
		upper = np.array([60,255,255])
		mask = cv2.inRange(img, lower, upper)
		green = cv2.bitwise_and(img, img, mask= mask)
		kernel = np.ones((5,5),np.uint8)
		green = cv2.erode(green, kernel,iterations = 1)
		m, green = cv2.threshold(green, 10, 255, cv2.THRESH_BINARY)
		greencolor = np.array([0, 255, 0])
		green = cv2.bitwise_and(green, greencolor)
		cv2.imshow('teste', green)
		cv2.waitKey(0)
		cv2.imwrite('images/processed/'+str(number)+'.png', green)

	def get_bird(self, filename):
		#deprecated 
		img = cv2.imread(filename)
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
		lower = np.array([10,10,50])
		upper = np.array([40,255,255])
		kernel = np.ones((10,10),np.uint8)
		yellow = cv2.erode(img, kernel,iterations = 1)
		mask = cv2.inRange(yellow, lower, upper)
		yellow = cv2.bitwise_and(img, img, mask= mask)
		m, yellow = cv2.threshold(yellow, 10, 255, cv2.THRESH_BINARY)
		yellowcolor = np.array([0, 255, 255])
		yellow = cv2.bitwise_and(yellow, yellowcolor)
		cv2.imshow('teste', yellow)
		cv2.waitKey(0)
		cv2.imwrite('images/bird.png', yellow)
		print(len(yellow), len(yellow[0]))

	def get_borders(self, filename):
		img = cv2.imread(filename)
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		
		lower = np.array([10,0,0])
		upper = np.array([180,255,255])
		kernel = np.ones((10,10),np.uint8)
		yellow = cv2.erode(img, kernel,iterations = 1)
		mask = cv2.inRange(yellow, lower, upper)
		yellow = cv2.bitwise_and(img, img, mask= mask)
		m, yellow = cv2.threshold(yellow, 10, 255, cv2.THRESH_BINARY)
		yellowcolor = np.array([0, 255, 255])
		yellow = cv2.bitwise_and(yellow, yellowcolor)
		#cv2.imshow('teste', yellow)
		#cv2.waitKey(0)
		cv2.imwrite('images/borders.png', yellow)
		print(len(yellow), len(yellow[0]))


	def find_borders_values(self):
		img = cv2.imread('images/borders.png')
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		px = int(len(img)/2)
		py = int(len(img[0])/2)+100

		print(img[px, py])
		pxleft = copy.copy(px)
		while(np.array_equal(img[pxleft, py], [0,0,0])):
			pxleft -= 1

		pxright = copy.copy(px)
		while(np.array_equal(img[pxright, py], [0,0,0])):
			pxright += 1
		print(px, pxleft/2+pxright/2)





