import numpy as np
import nnfs
from nnfs.datasets import spiral_data

import matplotlib.pyplot as plt

nnfs.init()

class LayerDense:
    def __init__(self, InputNum, NeuronNum):
        self.weights = 0.10 * np.random.randn(InputNum, NeuronNum)
        self.biases = np.zeros((1, NeuronNum))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class ActivationReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)

class ActivationSoftMax:
    def forward(self, inputs):
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
        probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)
        self.output = probabilities

class Loss:
    def calculate(self, output, y):
        sampleLoss = self.forward(output, y)
        dataLoss = np.mean(sampleLoss)

        return dataLoss
    
# CCE = Categorical Cross E ntropy

class CCE(Loss):
    def forward(self, yPred, yTrue):
        samples = len(yPred)

        yPredClipped = np.clip(yPred, 1e-7, 1 - 1e-7)

        if len(yTrue.shape) == 1:
            correctConf = yPredClipped[
                range(samples),
                yTrue
            ]
        elif len(yTrue.shape) == 2:
            correctConf = np.sum(
                yPredClipped * yTrue,
                axis=1
            )

        negativeLogProb = -np.log(correctConf)
        return negativeLogProb


X,y = spiral_data(samples=100, classes=3)

layer1 = LayerDense(2,3)
act1 = ActivationReLU()

layer2 = LayerDense(3,3)
act2 = ActivationSoftMax()

lossF = CCE()

layer1.forward(X)
act1.forward(layer1.output)

layer2.forward(act1.output)
act2.forward(layer2.output)

# print(act2.output[:5])

# loss = lossF.calculate(act2.output, y)
# print("loss: ", loss)

# predictions = np.argmax(act2.output, axis=1)
# if len(y.shape) == 2:
#     y = np.argmax(y, axis=1)
# accuracy = np.mean(predictions==y)

# print("acc: ", accuracy)

def f(x):
    return 2 * x ** 2

x = np.arange(0, 5, 0.0001)
y = f(x)

plt.plot(x,y)

p2_delta = 0.0001
x1 = 2
x2 = x1 + p2_delta

y1 = f(x1)
y2 = f(x2)

Gradient = (y2 - y1) / (x2 - x1)
b = y2 - Gradient*x2

def tangentLine(x):
    return Gradient*x + b

to_plot = [x1-0.9, x1, x1+0.9]
plt.plot(to_plot, [tangentLine[i] for i in to_plot])
plt.show()