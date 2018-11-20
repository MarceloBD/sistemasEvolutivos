import cv2
import copy

class Simulation():

	#before jump -9
	#after jump -89
	# total jump 80 
	#total vertical 60
	#total horizontal 70
	# 5 frames to climb
	# 6 frames to back 	
	def __init__(self):
		self.pos = 390
		self.frame = 23 
		self.vel = 0
		self.acel = 4.85
		return

	def reset(self):
		self.pos = 390
		self.frame = 23 
		self.vel = 0
		self.acel = 4.85

	def jump(self):
		self.vel = -25
		return

# acel > 0
# vel > 0 
# vel < 0 

	def update(self): 
		self.pos += self.vel
		self.vel += self.acel
		self.frame += 1
		#print(self.frame)
		self.draw_square(self)


	def draw_square(self, i):
		left_border = 11
		length = 472
		img = cv2.imread('images/'+str(self.frame)+'.png')
		cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		for x in range(70):
			for y in range(60):
				px = int(left_border+length/2.0-x)+4
				py = int(len(img)/2)-9+y+ int(self.pos) - 390
				img[py, px] = [255, 0,0]
		#cv2.imshow('teste', img)
		#cv2.waitKey(0)
		print('simultation py', py)
		print('last_x_pixel', px)
		return px 
			
	def draw(self, img, color):
		left_border = 11
		length = 472
		for x in range(70):
			for y in range(60):
				px = int(left_border+length/2.0-x)+4
				py = int(len(img)/2)-9+y+ int(self.pos) - 390
				img[py, px] = copy.copy(color)
		return img 

	def get_dist_to_center(self, center):
		return center-self.pos

	def print(self):
		print(self.pos)
