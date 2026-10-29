# code

from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten

# Bilderna är 28x28 pixlar.
# Matrismultiplikation / matrix multiplication
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 28,28, 1)
X_test = X_test.reshape(10000, 28,28, 1)

X_train = X_train.astype("float32")
X_test = X_test.astype("float32")

X_train = X_train / 255.0
X_test = X_test / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential()

model.add(Input(shape=(28,28,1)))

model.add(Conv2D(32, (3,3), activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Conv2D(4, (3,3), activation="relu"))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=64
)
loss, accuracy = model.evaluate(X_test, y_test)

print(accuracy)