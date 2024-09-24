# Import necessary libraries
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
from keras.utils import to_categorical

# Load the MNIST dataset (handwritten digits)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data: Flatten the 28x28 images to 784-dimensional vectors and normalize pixel values
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255

# Convert class labels (0-9) to one-hot encoding for 10 classes
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# Create a sequential model
model = Sequential()

# Add input layer with 784 neurons (for 28x28 images)
model.add(Dense(64, activation='relu', input_shape=(784,)))

# Add hidden layer with 64 neurons
model.add(Dense(64, activation='relu'))

# Add output layer with 10 neurons (for 10 classes)
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model and display output
history = model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

# Print model summary
model.summary()

# Evaluate the model on test data
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print(f"\nTest loss: {test_loss}")
print(f"Test accuracy: {test_accuracy}")
dd5tb
