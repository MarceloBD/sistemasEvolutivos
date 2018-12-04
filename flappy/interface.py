import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Menu(GridLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.cols = 1
		get_train_data_but = Button(text='Get train data')
		get_train_data_but.bind(on_press = self.get_train_data)
		self.add_widget(get_train_data_but)
		train_but = Button(text='Train')
		train_but.bind(on_press = self.train)
		self.add_widget(train_but)
		run_but = Button(text='Run')
		run_but.bind(on_press = self.run)
		self.add_widget(run_but)

	def get_train_data(self, instance):
		print('here')

	def train(self, instance):
		print('train')

	def run(self, instance):
		print('run')

class Interface(App):
	def build(self):
		return Menu()



Interface().run()