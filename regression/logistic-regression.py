import numpy as np


response = np.array([1, 1, 1, 1, 0, 0, 0, 0])

regressors = np.array([
    [1, .95],
    [1, .90],
    [1, .97],
    [1, .84],
    [1, 1.05],
    [1, 1.00],
    [1, 1.10],
    [1, 1.12],
])

parameters = np.array([[0, 0]])
n = len(regressors)


def cost(response, regressors, parameters):
    cost = 0

    for i in range(n):
        actual = response[i]
        predicted = parameters[0][0] + (parameters[0][1] * regressors[i][1])

        print(actual, predicted)

        log_loss = (actual * np.log(predicted)) + \
            ((1 - actual) * np.log(1 - predicted))
        cost += log_loss
    return (-1 / n) * cost


def gradient(response, regressors, parameters):
    partial_0 = partial_1 = 0

    for i in range(n):
        actual = response[i]
        predicted = parameters[0][0] + (parameters[0][1] * regressors[i][1])

        partial_0 += (predicted - actual) * regressors[i][0]
        partial_1 += (predicted - actual) * regressors[i][1]

    grad = (2 / n) * np.array([partial_0, partial_1])
    print('gradient:', grad)
    return grad


def train(parameters, response, regressors, cycles=500, alpha=0.1):
    for _ in range(cycles):
        parameters = parameters - \
            (alpha * gradient(response, regressors, parameters))
        print('parameters:', parameters)
        print('error:', cost(response, regressors, parameters))


train(parameters, response, regressors)
