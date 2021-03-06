#NumPy
import numpy as np
np.random.seed(123)
import keras
# Keras model module
from keras.models import Sequential
# Keras core layers
from keras.layers import Dense, Dropout, Activation, Flatten
# Keras CNN layers
from keras.layers import MaxPooling2D
from keras.layers.convolutional import Conv2D
# Utilities
from keras.utils import np_utils
print(keras.__version__)
from keras import backend as K
K.set_image_dim_ordering('th')

# Load MNIST data
from keras.datasets import mnist

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(X_train.shape)

# Plotting first sample of X_train
import matplotlib.pyplot as plt
plt.imshow(X_train[0])

# Reshape input data
X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)

print("Reshaped data ", X_train.shape)

# Covert data type and normalize values
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Preprocess class labels for Keras

print(y_train.shape)

print(y_train[:10])

# Convert 1-dimensional class arrays to 10-dimensional class matrices
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

print(Y_train.shape)

# Define model architecture

# Declare Sequential model

model = Sequential()

# Input layer
# CNN Input layer

model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=(1,28,28)))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
 
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

# Complie model
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# Fit Keras model
model.fit(X_train, Y_train, 
          batch_size=32, nb_epoch=10, verbose=1)

# Evaluate keras model
score = model.evaluate(X_test, Y_test, verbose=0)
print(score)