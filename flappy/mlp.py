import keras 
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np 
import random
from keras.constraints import max_norm

MUTATION_RANGE = 0.1
MUTATION_CHANCE = 0.1 


class Mlp():

	def __init__(self):
		self.model = Sequential([
			Dense(2, input_shape=(2,), activation="relu", kernel_constraint=max_norm(1.)),
			Dense(6, activation="relu", kernel_constraint=max_norm(1.)),
			Dense(2, activation="softmax", kernel_constraint=max_norm(1.))
			])
		#print(self.model.summary())
		self.model.compile(Adam(lr=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
		#w = self.model.layers[0].get_weights()
		#print('------------w-----------------')
		#w = self.model.get_weights()
		#print(w)
		#print(w)

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
		test = np.array([test[0][0], test[0][1]], dtype=np.float)
		test = test.reshape(1,-1) 
		test = np.vstack((test, [-500, -300]))
		test = np.vstack((test, [500, 300]))

		#print(test)
		scaled_test = scaler.fit_transform(test)
		print('parameterssss scaled', scaled_test[0].reshape(1,-1))
		rounded_predictions = self.model.predict_classes(scaled_test[0].reshape(1,-1), batch_size=1, verbose=0)
		#rounded_predictions = self.model.predict(scaled_test, batch_size=10, verbose=0)
		#print('rounded', rounded_predictions)
		#if(rounded_predictions[0][0] > rounded_predictions[0][1]):
		#	rounded_predictions = [0]
		#else:
		#		rounded_predictions = [1]
		return rounded_predictions

	def weight_mutation(self):
		number_of_layers = int(len(self.model.get_weights())/2)
		layer_len = [2]
		layer_len += [len(self.model.layers[i].get_weights()[0][0]) for i in range(number_of_layers)]  
		#print(layer_len)
		#print(self.model.layers[0].get_weights())
		#print(self.model.layers[0].get_weights()[0][0][0])
		for layer in range(1, number_of_layers+1):
			for i in range(int(layer_len[layer]*layer_len[layer-1]*MUTATION_RANGE)):
				var = random.randint(1,100)
				if (var <= 100*MUTATION_CHANCE):
					new_weigth = self.model.layers[layer-1].get_weights()
					index_i = random.randint(0, layer_len[layer-1]-1)
					index_j = random.randint(0, layer_len[layer]-1)
					#print('layer', layer, layer_len[layer]-1, layer_len[layer-1]-1)
					value = random.uniform(-1,1)
					#print(new_weigth)
					new_weigth[0][index_i][index_j] = value
					self.model.layers[layer-1].set_weights(new_weigth)
			self.bias_mutation(layer-1, layer_len[1:])


	def bias_mutation(self, layer, layer_len):
		for i in range(int(layer_len[layer]*MUTATION_RANGE)):
			var = random.randint(1,100)
			if (var <= 100*MUTATION_CHANCE*5):
				new_weigth = self.model.layers[layer].get_weights()
				index = random.randint(0, layer_len[layer]-1)
				value = random.uniform(-1,1)
				new_weigth[1][index] = value
				self.model.layers[layer].set_weights(new_weigth)
		#print('layer 2', self.model.layers[3].get_weights())

	def crossover(self, mlp):
		number_of_layers = int(len(self.model.get_weights())/2)
		layer_len = [2]
		layer_len += [len(self.model.layers[i].get_weights()[0][0]) for i in range(number_of_layers)]  

		for layer in range(1, number_of_layers+1):
			for i in range(int(layer_len[layer]*layer_len[layer-1]*MUTATION_RANGE)):
				var = random.randint(1,100)
				if (var <= 100*MUTATION_CHANCE):
					new_weigth = self.model.layers[layer-1].get_weights()
					parent_weight = mlp.model.layers[layer-1].get_weights()
					index_i = random.randint(0, layer_len[layer-1]-1)
					index_j = random.randint(0, layer_len[layer]-1)
					#print('layer', layer, layer_len[layer]-1, layer_len[layer-1]-1)
					#print(new_weigth)
					print(new_weigth[0])
					print('--')
					print(parent_weight[0])
					new_weigth[0][index_i][index_j] = (new_weigth[0][index_i][index_j]+
														parent_weight[0][index_i][index_j])/2
					self.model.layers[layer-1].set_weights(new_weigth)
			layerb = layer-1
			layer_lenb = layer_len[1:]
			for i in range(int(layer_lenb[layerb]*MUTATION_RANGE)):
				var = random.randint(1,100)
				if (var <= 100*MUTATION_CHANCE*5):
					new_weigth = self.model.layers[layerb].get_weights()
					parent_weight = mlp.model.layers[layerb].get_weights()
					index = random.randint(0, layer_lenb[layerb]-1)

					new_weigth[1][index] = (new_weigth[1][index]+parent_weight[1][index])/2
					self.model.layers[layerb].set_weights(new_weigth)