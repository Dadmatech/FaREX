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

testResult = [16, 16, 22, 22, 22, 22, 22, 22, 22, 22, 22, 23, 23, 43, 15, 39, 6, 44, 10, 10, 10, 0, 10, 28, 10, 10, 10, 10, 18, 28, 28, 7, 15, 15, 15, 15, 15, 10, 15, 16, 15, 17, 17, 17, 17, 17, 17, 17, 17, 0, 23, 23, 23, 23, 23, 23, 23, 23, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 32, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 0, 5, 5, 5, 5, 5, 5, 5, 5, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5, 5, 5, 5, 5, 5, 40, 44, 44, 44, 44, 44, 14, 40, 3, 40, 40, 0, 0, 14, 12, 3, 14, 0, 12, 0, 40, 12, 10, 0, 0, 0, 40, 14, 1, 25, 40, 25, 25, 25, 12, 40, 14, 40, 40, 3, 25, 40, 0, 40, 0, 40, 40, 0, 12, 40, 40, 0, 0, 0, 3, 0, 12, 40, 28, 40, 40, 0, 17, 14, 17, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 25, 25, 40, 40, 12, 3, 32, 10, 10, 10, 28, 10, 10, 10, 10, 10, 28, 10, 10, 10, 10, 10, 10, 10, 10, 30, 30, 30, 30, 30, 30, 30, 7, 6, 27, 12, 27, 27, 43, 23, 30, 43, 20, 20, 20, 0, 23, 43, 20, 23, 20, 23, 43, 28, 28, 28, 28, 28, 28, 28, 9, 28, 28, 28, 28, 28, 0, 28, 28, 28, 28, 28, 19, 28, 13, 12, 10, 10, 10, 16, 10, 10, 16, 16, 16, 16, 16, 16, 2, 12, 26, 26, 12, 12, 26, 12, 17, 26, 26, 26, 26, 26, 28, 10, 10, 16, 16, 2, 16, 28, 42, 28, 28, 13, 33, 13, 33, 31, 9, 42, 23, 3, 24, 40, 3, 0, 40, 3, 0, 3, 40, 4, 3, 0, 3, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 41, 28, 28, 0, 7, 19, 16, 12, 26, 27, 26, 10, 9, 26, 28, 19, 41, 12, 0, 31, 27, 22, 22, 22, 5, 22, 22, 0, 22, 22, 22, 24, 24, 24, 24, 24, 24, 24, 0, 0, 24, 24, 7, 39, 39, 39, 39, 39, 39, 39, 10, 16, 39, 10, 6, 39, 39, 10, 7, 10, 9, 10, 9, 9, 39, 10, 39, 10, 16, 39, 10, 39, 39, 39, 39, 39, 39, 39, 39, 10, 10, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 19, 19, 19, 19, 19, 19, 19, 0, 19, 19, 19, 19, 27, 19, 19, 7, 19, 41, 19, 19, 19, 19, 19, 27, 7, 19, 41, 19, 19, 19, 41, 19, 19, 19, 19, 19, 19, 19, 19, 5, 7, 19, 33, 0, 13, 20, 40, 12, 23, 25, 40, 29, 0, 0, 14, 30, 12, 0, 0, 40, 14, 40, 0, 0, 0, 3, 40, 40, 40, 3, 14, 40, 40, 10, 40, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 27, 19, 27, 27, 10, 0, 0, 27, 0, 27, 41, 0, 27, 12, 27, 9, 41, 0, 12, 12, 19, 27, 19, 41, 19, 27, 41, 27, 12, 12, 12, 0, 12, 0, 14, 0, 0, 12, 12, 40, 0, 0, 12, 12, 0, 12, 12, 0, 12, 12, 0, 12, 12, 0, 12, 12, 12, 0, 0, 12, 0, 0, 0, 12, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 0, 0, 7, 5, 5, 0, 5, 5, 7, 5, 5, 7, 7, 0, 8, 0, 5, 31, 8, 5, 0, 31, 31, 8, 0, 5, 0, 5, 7, 0, 0, 39, 5, 0, 5, 0, 5, 5, 5, 0, 36, 5, 23, 23, 7, 36, 23, 5, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 33, 8, 8, 8, 8, 8, 8, 8, 31, 44, 8, 8, 8, 8, 8, 31, 8, 8, 8, 8, 8, 8, 9, 33, 8, 14, 24, 40, 0, 12, 0, 40, 25, 25, 40, 40, 40, 0, 39, 9, 9, 9, 16, 6, 9, 6, 6, 10, 44, 9, 9, 9, 6, 9, 15, 13, 39, 39, 9, 18, 39, 39, 16, 39, 39, 10, 39, 9, 10, 39, 9, 31, 31, 12, 9, 18, 14, 9, 31, 18, 44, 12, 9, 9, 31, 9, 9, 9, 9, 31, 0, 33, 31, 31, 9, 9, 9, 9, 0, 0, 12, 33, 15, 9, 0, 33, 33, 9, 33, 9, 9, 9, 9, 9, 0, 13, 33, 9, 31, 9, 9, 9, 44, 31, 9, 9, 10, 31, 9, 26, 7, 9, 9, 10, 33, 44, 9, 32, 32, 32, 17, 32, 32, 32, 17, 17, 32, 32, 32, 32, 5, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 17, 32, 5, 32, 32, 17, 32, 32, 32, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 31, 7, 7, 7, 7, 7, 12, 7, 7, 9, 7, 9, 7, 7, 7, 7, 7, 7, 18, 18, 7, 7, 7, 23, 23, 7, 7, 23, 7, 7, 15, 7, 7, 7, 7, 7, 7, 7, 7, 31, 7, 7, 7, 7, 7, 23, 7, 9, 7, 7, 7, 7, 7, 7, 33, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 7, 7, 7, 7, 7, 15, 7, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 15, 7, 15, 7, 15, 15, 15, 15, 7, 22, 9, 23, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 13, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 22, 22, 22, 40, 3, 0, 10, 42, 42, 42, 9, 29, 16, 0, 22, 22, 16, 10, 43, 43, 23, 23, 39, 39, 39, 39, 9, 6, 44, 9, 9, 9, 0, 10, 10, 10, 30, 2, 15, 15, 6, 9, 15, 30, 32, 17, 17, 17, 17, 17, 23, 23, 20, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 44, 20, 3, 28, 0, 40, 25, 14, 12, 25, 12, 40, 0, 0, 28, 40, 28, 0, 3, 28, 28, 0, 0, 12, 14, 0, 0, 3, 12, 0, 0, 0, 40, 0, 25, 0, 14, 25, 12, 3, 40, 12, 0, 40, 12, 25, 0, 25, 40, 40, 40, 25, 23, 20, 32, 0, 3, 3, 0, 0, 0, 0, 0, 25, 14, 0, 12, 12, 23, 0, 25, 40, 25, 0, 40, 25, 25, 0, 40, 25, 0, 40, 0, 40, 14, 0, 32, 17, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 9, 42, 10, 42, 42, 42, 42, 10, 42, 10, 10, 42, 33, 10, 30, 30, 30, 30, 31, 30, 30, 30, 30, 30, 7, 30, 30, 30, 30, 30, 30, 30, 19, 12, 19, 41, 27, 12, 41, 23, 20, 23, 20, 43, 43, 20, 42, 42, 10, 13, 42, 28, 28, 28, 28, 28, 28, 28, 42, 42, 12, 7, 0, 16, 31, 10, 2, 39, 16, 16, 10, 16, 10, 16, 16, 9, 12, 26, 26, 0, 26, 26, 26, 26, 17, 26, 23, 26, 26, 26, 26, 26, 23, 17, 26, 42, 10, 16, 28, 28, 10, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 39, 39, 10, 28, 13, 42, 28, 33, 33, 33, 33, 13, 31, 24, 3, 0, 0, 0, 3, 0, 0, 5, 16, 28, 9, 36, 12, 7, 16, 36, 16, 23, 10, 9, 16, 16, 0, 20, 16, 0, 10, 10, 0, 9, 12, 0, 16, 10, 10, 0, 0, 22, 0, 5, 26, 26, 26, 22, 27, 22, 22, 22, 22, 22, 22, 22, 22, 11, 11, 0, 23, 12, 2, 30, 22, 12, 24, 24, 0, 24, 0, 0, 7, 16, 39, 39, 39, 10, 39, 16, 10, 10, 10, 39, 39, 10, 39, 39, 39, 39, 10, 30, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 39, 10, 39, 19, 19, 19, 31, 31, 19, 19, 0, 19, 19, 9, 0, 19, 0, 0, 19, 12, 19, 19, 19, 31, 19, 19, 19, 19, 0, 12, 12, 40, 0, 0, 12, 12, 40, 0, 40, 40, 40, 0, 12, 40, 0, 40, 40, 40, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 41, 41, 41, 19, 41, 0, 27, 19, 41, 41, 27, 41, 19, 27, 12, 0, 41, 41, 0, 41, 43, 41, 26, 27, 41, 27, 12, 0, 41, 12, 12, 41, 31, 19, 19, 0, 19, 27, 19, 41, 41, 7, 12, 12, 0, 0, 0, 12, 0, 12, 0, 12, 0, 12, 12, 0, 12, 0, 0, 12, 12, 0, 0, 0, 12, 0, 12, 0, 0, 0, 0, 0, 0, 0, 12, 12, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 5, 0, 5, 0, 0, 0, 0, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 31, 5, 31, 0, 31, 5, 5, 18, 7, 36, 9, 8, 7, 5, 5, 0, 9, 0, 5, 5, 5, 5, 5, 5, 5, 5, 9, 15, 5, 36, 5, 36, 5, 5, 36, 26, 7, 7, 0, 0, 0, 5, 5, 0, 8, 8, 8, 3, 8, 5, 5, 8, 8, 8, 8, 8, 8, 8, 8, 20, 8, 8, 8, 8, 8, 0, 9, 8, 8, 8, 8, 8, 8, 8, 8, 2, 8, 8, 8, 8, 33, 8, 8, 3, 3, 3, 3, 3, 40, 25, 0, 40, 40, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 12, 24, 14, 25, 24, 25, 24, 0, 25, 25, 28, 4, 40, 9, 31, 6, 6, 6, 16, 9, 44, 39, 16, 9, 39, 39, 16, 39, 9, 10, 9, 16, 10, 16, 39, 39, 10, 39, 39, 10, 10, 9, 9, 6, 9, 10, 10, 10, 33, 16, 9, 39, 39, 33, 18, 33, 31, 31, 31, 12, 26, 12, 7, 7, 31, 31, 20, 31, 31, 31, 7, 23, 23, 16, 31, 31, 31, 31, 9, 9, 31, 9, 31, 9, 33, 9, 31, 9, 9, 31, 9, 9, 33, 31, 6, 10, 33, 33, 9, 31, 18, 18, 31, 9, 31, 9, 31, 31, 31, 33, 18, 9, 33, 33, 31, 33, 9, 31, 31, 33, 31, 0, 9, 12, 9, 9, 31, 0, 18, 31, 31, 9, 9, 18, 9, 18, 31, 18, 32, 32, 12, 17, 17, 32, 32, 32, 17, 17, 17, 0, 17, 32, 32, 32, 32, 32, 32, 17, 32, 17, 32, 32, 32, 32, 17, 32, 32, 5, 5, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 5, 32, 5, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 5, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 17, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 0, 32, 32, 5, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 0, 32, 32, 32, 32, 32, 32, 32, 32, 32, 7, 5, 7, 0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 7, 7, 7, 7, 7, 7, 7, 39, 7, 7, 7, 7, 7, 7, 7, 7, 23, 7, 7, 7, 7, 7, 7, 7, 15, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 12, 7, 10, 7, 9, 9, 7, 7, 19, 18, 9, 9, 7, 7, 12, 8, 7, 7, 15, 7, 7, 7, 0, 7, 7, 7, 7, 19, 18, 12, 0, 0, 12, 0, 12, 12, 0, 21, 12]
realLabels = []
generatedTextLabels = []

generatedText = {
    "http://fkg.iust.ac.ir/ontology/birthPlace": 0,
    "http://fkg.iust.ac.ir/ontology/county": 1,
    "http://fkg.iust.ac.ir/ontology/starring": 2,
    "http://fkg.iust.ac.ir/ontology/province": 3,
    "http://fkg.iust.ac.ir/ontology/district": 4,
    "http://fkg.iust.ac.ir/ontology/nationality": 5,
    "http://fkg.iust.ac.ir/ontology/musicalArtist": 6,
    "http://fkg.iust.ac.ir/ontology/occupation": 7,
    "http://fkg.iust.ac.ir/ontology/language": 8,
    "http://fkg.iust.ac.ir/ontology/writer": 9,
    "http://fkg.iust.ac.ir/ontology/producer": 10,
    "http://fkg.iust.ac.ir/ontology/leaderName": 11,
    "http://fkg.iust.ac.ir/ontology/deathPlace": 12,
    "http://fkg.iust.ac.ir/ontology/family": 13,
    "http://fkg.iust.ac.ir/ontology/location": 14,
    "http://fkg.iust.ac.ir/ontology/musicComposer": 15,
    "http://fkg.iust.ac.ir/ontology/cinematography": 16,
    "http://fkg.iust.ac.ir/ontology/managerClub": 17,
    "http://fkg.iust.ac.ir/ontology/editing": 18,
    "http://fkg.iust.ac.ir/ontology/spouse": 19,
    "http://fkg.iust.ac.ir/ontology/almaMater": 20,
    "http://fkg.iust.ac.ir/ontology/residence": 21,
    "http://fkg.iust.ac.ir/ontology/mayor": 22,
    "http://fkg.iust.ac.ir/ontology/institution": 23,
    "http://fkg.iust.ac.ir/ontology/capital": 24,
    "http://fkg.iust.ac.ir/ontology/city": 25,
    "http://fkg.iust.ac.ir/ontology/party": 26,
    "http://fkg.iust.ac.ir/ontology/parent": 27,
    "http://fkg.iust.ac.ir/ontology/manufacturer": 28,
    "http://fkg.iust.ac.ir/ontology/productionCompany": 29,
    "http://fkg.iust.ac.ir/ontology/award": 30,
    "http://fkg.iust.ac.ir/ontology/notableWork": 31,
    "http://fkg.iust.ac.ir/ontology/team": 32,
    "http://fkg.iust.ac.ir/ontology/genre": 33,
    "http://fkg.iust.ac.ir/ontology/distributor": 34,
    "http://fkg.iust.ac.ir/ontology/foundedBy": 36,
    "http://fkg.iust.ac.ir/ontology/club": 37,
    "http://fkg.iust.ac.ir/ontology/hometown": 38,
    "http://fkg.iust.ac.ir/ontology/director": 39,
    "http://fkg.iust.ac.ir/ontology/country": 40,
    "http://fkg.iust.ac.ir/ontology/child": 41,
    "http://fkg.iust.ac.ir/ontology/recordLabel": 42,
    "http://fkg.iust.ac.ir/ontology/university": 43,
    "http://fkg.iust.ac.ir/ontology/album": 44
}

list_of_keys = list(generatedText.keys())
for i in range(0, len(list_of_keys)):
	generatedTextLabels.append(list_of_keys[i].split("/")[-1])

with open('gold_tagged_test_format_in_patterns.json', encoding='utf-8') as file:
    readFile = file.read()
    valid = json.loads(readFile)

labels = []
for i in range (0, len(valid)):
	realLabels.append(generatedText[valid[i]['relation']])
	labels.append(valid[i]['relation'])

# usedLabels = []
# for i in range(0, len(testResult)):
# 	for x in range(0, len(generatedText)):
# 		if (getKeyFromValue(generatedText, x) == testResult[i]):
# 			usedLabels.append(getKeyFromValue(generatedText, x))

# for y in range(0, len(labels)):
# 	if(not labels[i] in usedLabels):
# 		print(labels[i])

print(len(testResult))
print(len(realLabels))
print(len(generatedTextLabels))

print(testResult[1])
print(realLabels[1])

used = set()
unique = [x for x in testResult if x not in used and (used.add(x) or True)]
print(len(unique))

used = set()
unique = [x for x in realLabels if x not in used and (used.add(x) or True)]
print(len(unique))



print(generatedTextLabels)
print(classification_report(realLabels, testResult, target_names=generatedTextLabels))

