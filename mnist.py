# ==========================
# 1. IMPORTERA BIBLIOTEK
# ==========================

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.utils import to_categorical

# ==========================
# 2. LADDA DATA
# ==========================

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Train:", x_train.shape)
print("Test:", x_test.shape)

# ==========================
# 3. FÖRBERED DATA
# ==========================

# 28x28 -> 784

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# Normalisera 0-255 -> 0-1

x_train = x_train / 255.0
x_test = x_test / 255.0

# One-Hot Encoding

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# ==========================
# 4. SKAPA MODELLEN
# ==========================

model = Sequential()

model.add(Input(shape=(784,)))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

# ==========================
# 5. KOMPILERA MODELLEN
# ==========================

model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# ==========================
# 6. TRÄNA MODELLEN
# ==========================

model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32
)

# ==========================
# 7. TESTA MODELLEN
# ==========================

loss, accuracy = model.evaluate(
    x_test,
    y_test
)

print("Accuracy:", accuracy)

# ==========================
# 8. GÖR EN PREDIKTION
# ==========================

prediction = model.predict(x_test[:1])

print("Prediktion:")
print(prediction)

print("Modellen tror att siffran är:")

import numpy as np

print(np.argmax(prediction))