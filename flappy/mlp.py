import keras 
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
import numpy as np 

class Mlp():

	def __init__(self):
		self.model = Sequential([
			Dense(2, input_shape=(2,), activation="relu"),
			Dense(6, activation="relu"),
			Dense(2, activation="softmax")
			])
		print(self.model.summary())
		self.model.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		
	def set_train(self, train, labels):
		print(train)
		scaler = MinMaxScaler(feature_range=(0,1))
		scaled_train = scaler.fit_transform((train))
		self.scaled_train = scaled_train
		self.train_labels = labels


	def train(self):
		self.model.fit(self.scaled_train, self.train_labels, batch_size=1, epochs=1, shuffle=True, verbose=2) 
		w = self.model.layers[0].get_weights()
		print(w)
		new_w = []
		new_w.append(np.array([[1, 2], [3,4]], float))
		new_w.append(w[1])
		self.model.layers[0].set_weights(new_w)
		w = self.model.layers[0].get_weights()
		print(w)

	def predict(self, test):
		#predictions = self.model.predict(self.scaled_train, batch_size=10, verbose=0)
		scaler = MinMaxScaler(feature_range=(0,1))
		scaled_test = scaler.fit_transform((test))
		rounded_predictions = self.model.predict_classes(scaled_test, batch_size=10, verbose=0)
		print(rounded_predictions)