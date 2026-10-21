from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

# Ladda datasetet
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Visa första bilden
plt.imshow(x_train[0], cmap="gray")

# Skriv vilken siffra det är
plt.title(f"Siffra: {y_train[0]}")

plt.show()