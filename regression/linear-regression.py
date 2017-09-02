#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

response = np.array([1.25, 1.40, 1.30, 8.5, 6.5, 6.0])
regressors = np.array([
    [1, .95, 1.80],
    [1, .90, 1.85],
    [1, .97, 1.70],
    [1, 1.05, 1.25],
    [1, 1.10, 1.15],
    [1, 1.12, 1.15]
])

parameters = np.array([[0, 0, 0]])
N = len(regressors)


def error(response, regressors, parameters):
    error = 0
    for i in range(N):
        actual = response[i]
        predicted = parameters[0][0] + (
            parameters[0][1] * regressors[i][1]) + (
            parameters[0][2] * regressors[i][2])
        error += 1 / N * (actual - predicted)**2
    return error


def gradient(response, regressors, parameters):
    partial_0 = partial_1 = partial_2 = 0

    for i in range(N):
        actual = response[i]
        predicted = parameters[0][0] + (
            parameters[0][1] * regressors[i][1]) + (
            parameters[0][2] * regressors[i][2])

        # for j in range()
        partial_0 += (predicted - actual) * regressors[i][0]
        partial_1 += (predicted - actual) * regressors[i][1]
        partial_2 += (predicted - actual) * regressors[i][2]

    grad = (2 / N) * np.array([partial_0, partial_1, partial_2])
    print('gradient:', grad)
    return grad


def train(parameters, response, regressors, cycles=500000, alpha=0.1):
    for _ in range(cycles):
        parameters = parameters - \
            (alpha * gradient(response, regressors, parameters))
        print('parameters:', parameters)
        print('error:', error(response, regressors, parameters))


train(parameters, response, regressors)
