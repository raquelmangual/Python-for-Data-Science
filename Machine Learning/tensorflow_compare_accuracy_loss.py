# Use this script to compare training and validation data accuracy and loss of a TensorFlow model.
# You can use this script by passing the history object returned by model.fit() during the training of your model. 
# It will generate plots showing the training and validation accuracy and loss over epochs. 
# This visualization allows you to compare the performance of the model on both the training and validation datasets.

import matplotlib.pyplot as plt
import numpy as np

def plot_metrics(history):
    # Extracting accuracy and loss values from the history object
    accuracy = history.history['accuracy']
    val_accuracy = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs = range(1, len(accuracy) + 1)

    # Plotting accuracy
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(epochs, accuracy, 'bo', label='Training accuracy')
    plt.plot(epochs, val_accuracy, 'b', label='Validation accuracy')
    plt.title('Training and Validation Accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    # Plotting loss
    plt.subplot(1, 2, 2)
    plt.plot(epochs, loss, 'bo', label='Training loss')
    plt.plot(epochs, val_loss, 'b', label='Validation loss')
    plt.title('Training and Validation Loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()

    plt.show()

# Example usage:
# history is the history object returned from model.fit()
# plot_metrics(history)