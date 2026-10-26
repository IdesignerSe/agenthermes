# MNIST

from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Input, Dense

# Bilderna är 28x28 pixlar.
# Matrismultiplikation / matrix multiplication
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# print("X_train")
# print(X_train.shape) # (60000, 28, 28)
# print("y_train")
# print(y_train.shape)
# print("X_test")
# print(X_test.shape) # (10000, 28, 28)
# print("y_test")
# print(y_test.shape)

# print(X_train[1])
# print(y_train[1])

# print(y_train[0]) # 5
# print(X_train[0])

# plt.imshow(X_train[1], cmap='gray')
# plt.show()

X_train = X_train.reshape(60000, 28 * 28)
X_test = X_test.reshape(10000, 28 * 28)

X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

X_train = X_train / 255.0
X_test = X_test / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential()

model.add( Input(shape=(784,)) )
model.add( Dense(32) )
model.add( Dense(16) )
model.add( Dense(10, activation="softmax") )

model.compile( optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"] )

model.fit( X_train, y_train, epochs=3 )

prediction = model.predict([X_train[0:1]])
print(prediction)