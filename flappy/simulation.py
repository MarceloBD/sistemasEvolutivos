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
		self.reset()
		return

	def reset(self):
		self.pos = 390
		#self.frame = 23 
		self.frame = 0
		self.vel = 0
		self.acel = 4.85
		self.alive = True
		self.distance = 0
		self.fit = 0 

	def jump(self):
		self.vel = -25
		return

# acel > 0
# vel > 0 
# vel < 0 

	def update(self, distance):
		if(not self.alive):
			return
		self.distance = distance 
		self.pos += self.vel
		self.vel += self.acel
		self.frame += 1
		#print(self.frame)
		self.set_alive_state()
		self.calculate_fitness()
		if(self.alive):
			self.draw_square(self)

	def calculate_fitness(self):
		if(self.alive):
			self.fit = self.frame
		else:
			self.fit = 0

	def set_alive_state(self):
		if(self.pos-30 < 40):
			self.alive = False
		elif(self.pos+30 > 600):
			self.alive = False
		if(self.check_collision()):
			self.alive = False

	def check_collision(self):
		hole_len = 73
		if(self.distance-45 <= 0 and np.abs(self.dist_to_center)+30 > hole_len/2):
			self.alive = False
		return

	def is_alive(self):
		return self.alive

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
		self.dist_to_center = center-self.pos
		return center-self.pos

	def print(self):
		print(self.pos)
