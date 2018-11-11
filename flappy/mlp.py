import keras 
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

class Mlp():

	def __init__(self):
		self.model = Sequential([
			Dense(2, input_shape=(1,), activation="relu"),
			Dense(6, activation="relu"),
			Dense(1, activation="softmax")
			])
		print(self.model.summary())
		self.model.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		
	def set_train(self, train, labels):
		scaler = MinMaxScaler(feature_range=(0,1))
		scaled_train = scaler.fit_transform((train).reshape(-1,1))
		self.scaled_train = scaled_train
		self.train_labels = labels

	def train(self):
		self.model.fit(self.scaled_train, self.train_labels, batch_size=10, epochs=20, shuffle=True, verbose=2) 

	def predict(self, test):
		#predictions = self.model.predict(self.scaled_train, batch_size=10, verbose=0)
		rounded_predictions = self.model.predict_classes(test, batch_size=10, verbose=0)