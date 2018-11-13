from pynput.keyboard import Key, Controller
import time
import pyautogui
import cv2
import numpy as np
import copy 
import pyscreenshot as ImageGrab
from datetime import datetime
from mss import mss


NUMBER_OF_IMAGES = 80
SAMPLE_TIME = 0.01

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
		#return ImageGrab.grab(bbox=(740,160, 490, 680))
	#	im.save(fname, 'png')
		mon = {"left": 740, "top": 160, "width": 490, "height":680}
		#mon':0, "top": 740, "left": 160, "width": 490, "height": 680}
		sct = mss()
		img = np.array(sct.grab(mon))
		return img
	#	print(filename)
	#	return pyautogui.screenshot(region=(740,160, 490, 680))

	def get_train_imgs(self):
		screen = []
		for i in range(NUMBER_OF_IMAGES):
			time.sleep(SAMPLE_TIME)
			screen.append(self.take_screen_shot())

		

		for i in range(NUMBER_OF_IMAGES):
			#image = cv2.cvtColor(np.array(screen[i]), cv2.COLOR_BGR2RGB)
			cv2.imwrite('images/'+str(i)+'.png', screen[i])
	
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
	#	cv2.imshow('teste', green)
	#	cv2.waitKey(0)
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
		px = int(len(img[0])/2)
		py = int(len(img)/2)-100
		print('img', px, py)

		print(img[py, px])
		pxleft = copy.copy(px)
		while(np.array_equal(img[py, pxleft], [0,0,0])):
			pxleft -= 1

		pxright = copy.copy(px)
		while(np.array_equal(img[py, pxright], [0,0,0])):
			pxright += 1
		print(px, pxleft, pxright-pxleft)
		last_px = self.draw_square(pxleft, pxright-pxleft)
		print('last_px, pxright', last_px, pxright)
		return last_px, pxright

	#before jump -9
	#after jump -89
	#total vertical 60
	#total horizontal 70
	def draw_square(self, left_border, length):
		img = cv2.imread('images/borders.png')
		print('left_boder, lengh', left_border, length)
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		for x in range(70):
			for y in range(60):
				px = int(left_border+length/2.0-x)+4
				py = int(len(img)/2)-9+y
				img[py, px] = [255, 0,0]
		cv2.imshow('teste', img)
		cv2.waitKey(0)
		print('simultation py', py)
		print('last_x_pixel', px)
		return px 

	def get_pipe_pixel(self, last_px, pxright, filename):
		img = cv2.imread(filename)
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

		img[570,last_px] = [255,255,255]
		cv2.imshow('teste', img)
		cv2.waitKey(0)

		pipe_pixel = pxright
		for i in range(last_px, pxright):
			if(np.array_equal(img[570, i], [0,255,0])):
				pipe_pixel = i
				break
		print('pipe', pipe_pixel)
		return pipe_pixel


	def get_distance(self, filename):
		return self.get_pipe_pixel(182, 483, filename)


	# pipe under pixel 318
	# pipe over pixel 295 (total len 23)
	# hole len 73 (295-122)
	def get_center(self, filename):
		img = cv2.imread(filename)
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		hole_len = 73
		pipe_inferior_len = 23

		last_px = 182
		pipe_pixel = self.get_pipe_pixel(182, 483, filename)
		print(pipe_pixel)

		pipe_inferior_pixel = 340 
		for i in range(570, 0 ,-1):
			if(np.array_equal(img[i, pipe_pixel], [0,255,0])):
				pipe_inferior_pixel = i 
				break
		#cv2.imshow('teste', img)
		#cv2.waitKey(0)
		return pipe_inferior_pixel + pipe_inferior_len + int(hole_len/2)



