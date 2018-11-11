from pynput.keyboard import Key, Controller
import time


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
