from sklearn.metrics import classification_report
import numpy as np
import json
import sys
import os
import argparse
import logging


def getKeyFromValue(dictionary, value):
	inv_dict = {value:key for key, value in dictionary.items()}
	return inv_dict[value]

testResult = [3, 60, 21, 60, 67, 52, 52, 16, 52, 59, 21, 59, 63, 63, 63, 63, 32, 69, 54, 41, 41, 41, 41, 41, 41, 41, 3, 41, 41, 24, 66, 21, 74, 21, 18, 50, 50, 50, 50, 21, 63, 75, 75, 66, 60, 60, 75, 31, 75, 60, 75, 60, 63, 59, 13, 13, 3, 13, 3, 3, 13, 13, 6, 9, 26, 26, 34, 16, 52, 51, 16, 51, 51, 52, 52, 16, 34, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 34, 31, 34, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 34, 31, 31, 16, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 20, 31, 31, 31, 31, 31, 31, 31, 31, 31, 34, 34, 31, 31, 31, 31, 31, 34, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 25, 20, 20, 20, 3, 20, 3, 20, 20, 20, 31, 20, 20, 20, 20, 20, 3, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 31, 20, 20, 20, 20, 20, 20, 20, 31, 41, 13, 41, 31, 41, 5, 41, 3, 41, 41, 41, 3, 20, 41, 20, 41, 41, 34, 35, 31, 35, 35, 35, 35, 35, 35, 34, 10, 2, 30, 30, 30, 43, 30, 30, 58, 58, 15, 13, 58, 1, 33, 38, 1, 0, 1, 38, 49, 68, 76, 74, 68, 76, 22, 17, 22, 22, 22, 6, 6, 8, 49, 6, 9, 6, 6, 6, 36, 2, 6, 6, 6, 6, 20, 34, 11, 11, 0, 8, 0, 6, 7, 49, 7, 7, 15, 2, 2, 11, 11, 6, 8, 6, 6, 15, 15, 0, 6, 14, 6, 34, 15, 0, 6, 34, 6, 6, 6, 6, 6, 0, 0, 6, 26, 11, 11, 11, 15, 15, 6, 49, 15, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 6, 26, 6, 3, 11, 11, 43, 43, 63, 60, 62, 63, 63, 22, 61, 43, 60, 60, 60, 61, 60, 63, 60, 2, 60, 54, 60, 60, 60, 43, 17, 17, 17, 17, 70, 70, 70, 70, 70, 70, 38, 70, 64, 24, 4, 4, 64, 51, 10, 10, 10, 10, 10, 15, 28, 28, 28, 28, 28, 15, 2, 60, 27, 65, 60, 60, 37, 61, 60, 52, 43, 27, 3, 43, 16, 52, 16, 16, 16, 52, 16, 16, 49, 16, 16, 16, 16, 16, 16, 60, 60, 61, 61, 60, 61, 60, 63, 62, 40, 60, 60, 61, 3, 61, 65, 60, 60, 60, 21, 60, 60, 3, 61, 12, 12, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 4, 4, 23, 4, 23, 23, 23, 23, 23, 23, 23, 23, 5, 5, 5, 5, 5, 5, 5, 5, 5, 11, 21, 21, 21, 21, 21, 24, 21, 21, 21, 63, 21, 63, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 65, 33, 28, 68, 29, 17, 60, 2, 0, 8, 4, 8, 6, 8, 14, 31, 8, 9, 14, 7, 8, 8, 31, 31, 20, 31, 31, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 31, 31, 31, 20, 31, 31, 31, 31, 31, 31, 43, 43, 43, 60, 60, 43, 43, 12, 48, 43, 22, 43, 27, 48, 43, 48, 53, 53, 53, 53, 53, 53, 16, 53, 53, 67, 53, 53, 53, 20, 50, 53, 53, 53, 53, 53, 53, 53, 53, 12, 24, 48, 48, 48, 48, 12, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 12, 12, 12, 12, 12, 12, 12, 7, 12, 48, 12, 12, 12, 24, 7, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 7, 9, 9, 9, 9, 9, 9, 9, 9, 7, 9, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 63, 24, 63, 63, 54, 43, 63, 43, 63, 63, 63, 63, 63, 63, 54, 63, 54, 21, 63, 21, 21, 21, 63, 69, 63, 63, 63, 63, 63, 63, 21, 21, 63, 63, 63, 21, 63, 63, 63, 63, 63, 21, 63, 63, 63, 21, 63, 21, 63, 21, 63, 69, 63, 63, 21, 21, 63, 63, 21, 63, 21, 21, 21, 63, 21, 21, 63, 62, 62, 62, 23, 15, 15, 62, 15, 62, 62, 15, 62, 62, 62, 15, 15, 15, 15, 62, 15, 62, 62, 15, 62, 15, 15, 15, 15, 15, 15, 62, 15, 62, 15, 15, 15, 15, 15, 15, 15, 62, 62, 15, 15, 15, 15, 15, 15, 15, 62, 62, 62, 62, 62, 34, 34, 2, 34, 2, 2, 2, 2, 2, 2, 2, 30, 43, 30, 43, 43, 30, 30, 30, 37, 37, 48, 24, 22, 30, 37, 30, 37, 30, 10, 30, 24, 37, 30, 21, 21, 21, 48, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 10, 21, 21, 21, 21, 21, 10, 10, 10, 45, 21, 21, 21, 45, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 31, 34, 34, 15, 15, 15, 15, 15, 15, 9, 25, 26, 15, 6, 2, 15, 4, 34, 6, 0, 6, 15, 15, 34, 7, 15, 15, 15, 15, 7, 15, 7, 34, 6, 14, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 14, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 7, 39, 7, 39, 39, 39, 39, 39, 39, 21, 21, 10, 45, 45, 45, 45, 10, 10, 42, 10, 45, 10, 10, 42, 21, 42, 31, 10, 10, 45, 10, 45, 45, 42, 42, 42, 10, 34, 34, 34, 34, 34, 34, 35, 35, 31, 34, 34, 31, 34, 34, 34, 34, 34, 17, 35, 34, 34, 34, 34, 35, 34, 34, 34, 34, 34, 31, 34, 34, 20, 34, 34, 34, 1, 1, 1, 1, 1, 1, 1, 1, 33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 34, 20, 20, 20, 20, 20, 20, 20, 34, 20, 20, 20, 20, 20, 20, 20, 20, 20, 28, 28, 20, 20, 20, 38, 31, 20, 34, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 34, 20, 31, 20, 34, 20, 52, 20, 20, 20, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 2, 28, 28, 28, 28, 28, 28, 28, 28, 28, 14, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 49, 28, 15, 49, 49, 49, 0, 0, 0, 21, 63, 63, 63, 63, 63, 63, 63, 63, 63, 74, 63, 63, 29, 63, 67, 63, 31, 63, 63, 63, 24, 21, 21, 63, 21, 21, 63, 21, 63, 63, 21, 63, 29, 29, 29, 50, 29, 17, 29, 29, 21, 29, 31, 54, 29, 29, 29, 50, 21, 29, 29, 32, 29, 29, 29, 31, 29, 29, 29, 29, 29, 54, 29, 29, 29, 54, 29, 29, 29, 29, 29, 21, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 50, 29, 29, 29, 28, 4, 32, 29, 29, 21, 21, 29, 29, 3, 3, 3, 3, 3, 3, 3, 3, 13, 18, 18, 18, 18, 41, 31, 18, 18, 18, 3, 18, 3, 18, 18, 3, 18, 18, 18, 18, 18, 3, 3, 18, 18, 18, 18, 18, 3, 3, 3, 3, 18, 3, 3, 3, 18, 20, 20, 54, 39, 20, 20, 54, 54, 54, 54, 31, 54, 54, 21, 54, 20, 54, 20, 20, 34, 54, 54, 54, 54, 54, 29, 29, 20, 31, 31, 35, 21, 63, 20, 54, 54, 54, 54, 54, 54, 51, 20, 31, 38, 54, 54, 20, 29, 20, 20, 20, 50, 54, 50, 54, 54, 20, 50, 25, 54, 50, 54, 20, 21, 31, 54, 32, 20, 20, 54, 54, 54, 54, 54, 54, 31, 54, 54, 54, 21, 54, 54, 54, 32, 32, 32, 20, 54, 38, 20, 38, 53, 38, 54, 53, 20, 31, 54, 53, 32, 53, 53, 74, 10, 54, 54, 74, 54, 74, 54, 38, 23, 29, 30, 31, 31, 31, 31, 31, 31, 54, 31, 20, 3, 3, 20, 29, 31, 20, 20, 31, 20, 20, 31, 31, 31, 20, 31, 20, 20, 20, 20, 20, 32, 20, 20, 31, 20, 20, 20, 20, 20, 31, 34, 31, 0, 34, 31, 31, 0, 0, 0, 31, 8, 20, 66, 59, 15, 60, 38, 53, 66, 66, 52, 16, 16, 16, 63, 21, 22, 21, 63, 28, 29, 63, 63, 74, 21, 74, 74, 74, 63, 50, 74, 74, 50, 50, 68, 68, 75, 60, 21, 3, 3, 3, 3, 3, 3, 26, 6, 26, 7, 26, 11, 6, 26, 26, 51, 51, 16, 16, 31, 31, 31, 31, 31, 31, 34, 31, 31, 31, 34, 31, 31, 31, 31, 31, 34, 34, 31, 31, 31, 31, 20, 31, 31, 31, 31, 31, 31, 31, 34, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 31, 20, 20, 31, 31, 31, 31, 31, 31, 31, 20, 31, 31, 31, 41, 41, 54, 41, 3, 3, 41, 3, 34, 35, 35, 35, 35, 35, 35, 34, 35, 35, 30, 30, 30, 30, 30, 30, 30, 30, 58, 15, 58, 58, 58, 58, 58, 15, 58, 58, 58, 21, 58, 58, 63, 58, 58, 58, 33, 33, 0, 59, 76, 76, 66, 29, 76, 59, 68, 76, 59, 59, 68, 59, 68, 22, 22, 9, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 2, 8, 34, 31, 6, 6, 6, 6, 6, 6, 6, 6, 6, 2, 6, 34, 6, 6, 2, 2, 6, 6, 6, 6, 2, 8, 14, 28, 6, 6, 15, 7, 7, 2, 2, 11, 6, 26, 6, 49, 9, 6, 15, 35, 0, 0, 2, 2, 2, 7, 6, 7, 16, 11, 6, 6, 6, 6, 6, 6, 6, 6, 0, 6, 15, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 2, 6, 6, 6, 11, 6, 6, 6, 11, 6, 3, 3, 3, 18, 3, 3, 3, 18, 3, 18, 3, 3, 18, 11, 14, 7, 11, 43, 65, 28, 63, 63, 63, 63, 22, 22, 61, 63, 43, 43, 60, 60, 60, 60, 60, 30, 28, 60, 60, 60, 58, 43, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 54, 70, 70, 70, 70, 70, 7, 70, 70, 70, 70, 70, 70, 7, 64, 70, 2, 38, 4, 4, 4, 4, 4, 4, 4, 64, 4, 32, 32, 24, 32, 32, 21, 10, 10, 21, 10, 10, 10, 15, 28, 8, 2, 2, 15, 2, 63, 60, 60, 60, 61, 60, 61, 60, 65, 43, 43, 43, 43, 63, 43, 43, 16, 16, 16, 52, 16, 52, 16, 65, 65, 27, 65, 61, 60, 60, 61, 61, 60, 60, 60, 61, 61, 39, 39, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 5, 5, 5, 5, 5, 5, 5, 5, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 41, 3, 5, 5, 5, 5, 5, 5, 5, 21, 32, 21, 21, 63, 9, 63, 63, 22, 22, 63, 21, 21, 21, 63, 63, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 68, 28, 38, 29, 60, 38, 14, 8, 0, 31, 31, 8, 31, 31, 20, 60, 60, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 43, 60, 7, 63, 48, 12, 43, 21, 43, 63, 43, 30, 43, 43, 43, 53, 53, 53, 53, 74, 53, 38, 53, 53, 53, 54, 53, 53, 53, 53, 53, 53, 12, 48, 12, 48, 43, 48, 48, 48, 48, 48, 48, 48, 22, 22, 22, 48, 24, 48, 32, 48, 48, 48, 48, 48, 12, 48, 12, 12, 12, 12, 12, 12, 12, 48, 12, 12, 12, 12, 43, 12, 24, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 43, 24, 9, 9, 9, 9, 9, 9, 9, 63, 63, 63, 21, 63, 63, 63, 63, 63, 24, 28, 50, 24, 21, 21, 21, 21, 63, 63, 21, 60, 43, 43, 54, 21, 63, 63, 63, 63, 63, 63, 63, 69, 63, 21, 21, 63, 63, 63, 21, 63, 63, 63, 21, 63, 63, 21, 63, 63, 63, 21, 63, 30, 21, 21, 63, 63, 15, 62, 62, 62, 62, 62, 15, 61, 15, 34, 34, 6, 6, 2, 2, 2, 9, 2, 60, 43, 43, 30, 43, 30, 43, 43, 30, 30, 30, 37, 37, 30, 30, 43, 71, 30, 30, 60, 60, 43, 43, 43, 30, 30, 43, 30, 21, 10, 21, 10, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 15, 15, 6, 15, 15, 15, 2, 15, 15, 15, 6, 20, 15, 6, 2, 2, 34, 6, 15, 39, 14, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 45, 10, 10, 10, 45, 45, 10, 42, 45, 42, 10, 45, 42, 10, 10, 45, 45, 10, 45, 10, 45, 42, 10, 10, 10, 10, 48, 32, 45, 48, 45, 45, 10, 21, 10, 45, 45, 42, 42, 10, 10, 10, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 31, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 31, 20, 34, 34, 34, 34, 34, 34, 34, 35, 34, 34, 34, 34, 34, 0, 34, 34, 34, 34, 34, 34, 20, 34, 20, 34, 34, 34, 34, 33, 1, 33, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 20, 20, 20, 20, 28, 20, 20, 20, 20, 20, 20, 28, 20, 28, 25, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 38, 20, 20, 20, 20, 20, 25, 20, 4, 20, 20, 20, 34, 34, 20, 20, 20, 28, 28, 28, 7, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 15, 28, 28, 28, 28, 28, 28, 28, 28, 2, 28, 28, 28, 28, 20, 28, 28, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 7, 6, 8, 6, 49, 49, 8, 28, 0, 49, 6, 0, 63, 63, 63, 74, 63, 21, 63, 63, 21, 63, 63, 63, 63, 21, 21, 63, 21, 63, 63, 63, 63, 21, 63, 63, 21, 21, 63, 21, 67, 63, 63, 29, 63, 63, 63, 21, 63, 63, 63, 21, 63, 54, 29, 29, 29, 29, 29, 4, 56, 54, 54, 29, 29, 50, 29, 29, 29, 4, 20, 50, 21, 29, 29, 29, 29, 29, 29, 29, 50, 50, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 28, 32, 29, 29, 29, 28, 54, 54, 29, 29, 29, 29, 4, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 20, 29, 29, 29, 29, 29, 54, 21, 29, 29, 29, 29, 29, 29, 29, 29, 18, 18, 3, 3, 3, 3, 3, 3, 3, 3, 3, 34, 3, 18, 18, 3, 3, 3, 3, 3, 3, 3, 18, 3, 3, 3, 13, 3, 18, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 18, 18, 18, 3, 18, 18, 18, 18, 18, 18, 18, 18, 18, 3, 18, 18, 18, 3, 3, 41, 18, 18, 3, 3, 3, 3, 3, 18, 18, 18, 18, 18, 18, 18, 3, 18, 3, 18, 18, 18, 3, 3, 3, 3, 3, 18, 70, 15, 20, 54, 54, 54, 54, 54, 54, 54, 54, 20, 20, 54, 54, 32, 29, 63, 54, 29, 54, 29, 54, 54, 21, 21, 21, 20, 20, 54, 20, 28, 21, 20, 52, 20, 53, 50, 20, 54, 20, 20, 54, 29, 20, 20, 20, 20, 20, 20, 20, 20, 21, 23, 21, 24, 21, 54, 54, 54, 54, 54, 29, 54, 54, 54, 54, 54, 32, 54, 20, 53, 53, 53, 54, 54, 52, 54, 34, 54, 31, 21, 21, 21, 31, 31, 16, 31, 16, 35, 8, 25, 34, 19]
realLabels = []
generatedTextLabels = []

generatedText = {
    "http://fkg.iust.ac.ir/ontology/region" : 0,
    "http://fkg.iust.ac.ir/ontology/family" : 1,
    "http://fkg.iust.ac.ir/ontology/headquarter" : 2,
    "http://fkg.iust.ac.ir/ontology/team" : 3,
    "http://fkg.iust.ac.ir/ontology/party" : 4,
    "http://fkg.iust.ac.ir/ontology/league" : 5,
    "http://fkg.iust.ac.ir/ontology/location" : 6,
    "http://fkg.iust.ac.ir/ontology/city" : 7,
    "http://fkg.iust.ac.ir/ontology/province" : 8,
    "http://fkg.iust.ac.ir/ontology/capital" : 9,
    "http://fkg.iust.ac.ir/ontology/child" : 10,
    "http://fkg.iust.ac.ir/ontology/ground" : 11,
    "http://fkg.iust.ac.ir/ontology/leaderName" : 12,
    "http://fkg.iust.ac.ir/ontology/managerClub" : 13,
    "http://fkg.iust.ac.ir/ontology/county" : 14,
    "http://fkg.iust.ac.ir/ontology/country" : 15,
    "http://fkg.iust.ac.ir/ontology/almaMater" : 16,
    "http://fkg.iust.ac.ir/ontology/battle" : 17,
    "http://fkg.iust.ac.ir/ontology/club" : 18,
    "http://fkg.iust.ac.ir/ontology/manager" : 19,
    "http://fkg.iust.ac.ir/ontology/nationality" : 20,
    "http://fkg.iust.ac.ir/ontology/spouse" : 21,
    "http://fkg.iust.ac.ir/ontology/commander" : 22,
    "http://fkg.iust.ac.ir/ontology/militaryBranch" : 23,
    "http://fkg.iust.ac.ir/ontology/president" : 24,
    "http://fkg.iust.ac.ir/ontology/residence" : 25,
    "http://fkg.iust.ac.ir/ontology/place" : 26,
    "http://fkg.iust.ac.ir/ontology/coach" : 27,
    "http://fkg.iust.ac.ir/ontology/language" : 28,
    "http://fkg.iust.ac.ir/ontology/notableWork" : 29,
    "http://fkg.iust.ac.ir/ontology/ceo" : 30,
    "http://fkg.iust.ac.ir/ontology/birthPlace" : 31,
    "http://fkg.iust.ac.ir/ontology/primeMinister" : 32,
    "http://fkg.iust.ac.ir/ontology/species" : 33,
    "http://fkg.iust.ac.ir/ontology/deathPlace" : 34,
    "http://fkg.iust.ac.ir/ontology/restingPlace" : 35,
    "http://fkg.iust.ac.ir/ontology/river" : 36,
    "http://fkg.iust.ac.ir/ontology/keyPerson" : 37,
    "http://fkg.iust.ac.ir/ontology/genre" : 38,
    "http://fkg.iust.ac.ir/ontology/district" : 39,
    "http://fkg.iust.ac.ir/ontology/regionServed" : 40,
    "http://fkg.iust.ac.ir/ontology/sport" : 41,
    "http://fkg.iust.ac.ir/ontology/monarch" : 42,
    "http://fkg.iust.ac.ir/ontology/foundedBy" : 43,
    "http://fkg.iust.ac.ir/ontology/event" : 44,
    "http://fkg.iust.ac.ir/ontology/parent" : 45,
    "http://fkg.iust.ac.ir/ontology/part" : 46 ,
    "http://fkg.iust.ac.ir/ontology/hometown" : 47,
    "http://fkg.iust.ac.ir/ontology/leader" : 48,
    "http://fkg.iust.ac.ir/ontology/state" : 49,
    "http://fkg.iust.ac.ir/ontology/student" : 50,
    "http://fkg.iust.ac.ir/ontology/institution" : 51,
    "http://fkg.iust.ac.ir/ontology/university" : 52,
    "http://fkg.iust.ac.ir/ontology/instrument" : 53,
    "http://fkg.iust.ac.ir/ontology/occupation" : 54,
    "http://fkg.iust.ac.ir/ontology/writer" : 55,
    "http://fkg.iust.ac.ir/ontology/colour" : 56,
    "http://fkg.iust.ac.ir/ontology/mission" : 57,
    "http://fkg.iust.ac.ir/ontology/network" : 58,
    "http://fkg.iust.ac.ir/ontology/recordLabel" : 59,
    "http://fkg.iust.ac.ir/ontology/owner" : 60,
    "http://fkg.iust.ac.ir/ontology/manufacturer" : 61,
    "http://fkg.iust.ac.ir/ontology/origin" : 62,
    "http://fkg.iust.ac.ir/ontology/author" : 63,
    "http://fkg.iust.ac.ir/ontology/affiliation" : 64,
    "http://fkg.iust.ac.ir/ontology/developer" : 65,
    "http://fkg.iust.ac.ir/ontology/associatedAct" : 66,
    "http://fkg.iust.ac.ir/ontology/bandMember" : 67,
    "http://fkg.iust.ac.ir/ontology/subsequentWork" : 68,
    "http://fkg.iust.ac.ir/ontology/designer" : 69,
    "http://fkg.iust.ac.ir/ontology/award" : 70,
    "http://fkg.iust.ac.ir/ontology/parentCompany" : 71,
    "http://fkg.iust.ac.ir/ontology/director" : 72,
    "http://fkg.iust.ac.ir/ontology/spokenIn" : 73,
    "http://fkg.iust.ac.ir/ontology/artist" : 74,
    "http://fkg.iust.ac.ir/ontology/productionCompany" : 75,
    "http://fkg.iust.ac.ir/ontology/album" : 76,
    "http://fkg.iust.ac.ir/ontology/starring" : 77
}
list_of_keys = list(generatedText.keys())
for i in range(0, len(list_of_keys)):
	generatedTextLabels.append(list_of_keys[i].split("/")[-1])

with open('gold_tagged_test_format_in_spad.json', encoding='utf-8') as file:
    readFile = file.read()
    valid = json.loads(readFile)


labels = []
for i in range (0, len(valid)):
	realLabels.append(generatedText[valid[i]['relation']])
	labels.append(valid[i]['relation'])
realLabels.append(19)

# usedLabels = []
# for i in range(0, len(testResult)):
# 	for x in range(0, len(generatedText)):
# 		if (getKeyFromValue(generatedText, x) == testResult[i]):
# 			usedLabels.append(getKeyFromValue(generatedText, x))

# for y in range(0, len(labels)):
# 	if(not labels[i] in usedLabels):
# 		print(labels[i])

print("testResult len = ", len(testResult))
print("realLabels len = ", len(realLabels))
print("Labels len = ", len(generatedTextLabels))

print("testResult[1] = ", testResult[1])
print("realLabels[1] = ", realLabels[1])

for i in range(0, len(generatedText)):
    if(i in testResult):
        pass
    else:
        print(i, " is not in testResult")

print("\n\n\n")
for i in range(0, len(generatedText)):
    if(i in realLabels):
        pass
    else:
        print(i, " is not in realLabels")

used = set()
unique = [x for x in testResult if x not in used and (used.add(x) or True)]
print("testResult unique labels len = ", len(unique))

used = set()
unique = [x for x in realLabels if x not in used and (used.add(x) or True)]
print("realLabels unique labels len = ", len(unique))



print("Labels = ", generatedTextLabels)
print(classification_report(realLabels, testResult, target_names=generatedTextLabels))

