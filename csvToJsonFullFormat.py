import json
import pandas as pd
import csv

def findSunsequnce(sentence, sequence):
	splitedSentence = sentence.split(" ")
	splitedSequence = sequence.split(" ")
	for i in range (0, len(splitedSentence) - len(splitedSequence)):
		if (splitedSequence == splitedSentence[i: i + len(splitedSequence)]):
			return i
	return -1

allValidRelations = []

with open('Source4 (2).csv', mode='r') as csv_file:
	csvReader = csv.DictReader(csv_file)
	for row in csvReader:
		sentence = row['sentence']
		head = {}
		head['word'] = row['head_word']
		headStart = findSunsequnce(row['sentence'], row['head_word'])
		head['start'] = headStart
		head['length'] = len(row['head_word'])
		head['id'] = row['head_url']
		
		tail = {}
		tail['word'] = row['tail_word']
		tailStart = findSunsequnce(row['sentence'], row['tail_word'])
		tail['start'] = tailStart
		tail['length'] = len(row['tail_word'])
		tail['id'] = row['tail_url']

		relation = {}
		relation['word'] = row['property_caption']
		relation['id'] = row['property']

		entry = {}
		entry['head'] = head
		entry['tail'] = tail
		entry['relation'] = relation
		entry['sentence'] = sentence

		if (row['is_correct'] == "1"):
			allValidRelations.append(entry)

savedFile = open("Source4_valids_test_format_full_format.json", "w", encoding='utf-8')
savedFile.write(str(json.dumps(allValidRelations, indent=4, sort_keys=True, ensure_ascii=False)))
savedFile.close()

# patternRelations = ["http://fkg.iust.ac.ir/ontology/birthPlace", "http://fkg.iust.ac.ir/ontology/county", "http://fkg.iust.ac.ir/ontology/starring", "http://fkg.iust.ac.ir/ontology/province", "http://fkg.iust.ac.ir/ontology/district", "http://fkg.iust.ac.ir/ontology/nationality", "http://fkg.iust.ac.ir/ontology/musicalArtist", "http://fkg.iust.ac.ir/ontology/occupation", "http://fkg.iust.ac.ir/ontology/language", "http://fkg.iust.ac.ir/ontology/writer", "http://fkg.iust.ac.ir/ontology/producer", "http://fkg.iust.ac.ir/ontology/leaderName", "http://fkg.iust.ac.ir/ontology/deathPlace", "http://fkg.iust.ac.ir/ontology/family", "http://fkg.iust.ac.ir/ontology/location", "http://fkg.iust.ac.ir/ontology/musicComposer", "http://fkg.iust.ac.ir/ontology/cinematography", "http://fkg.iust.ac.ir/ontology/managerClub", "http://fkg.iust.ac.ir/ontology/editing", "http://fkg.iust.ac.ir/ontology/spouse", "http://fkg.iust.ac.ir/ontology/almaMater", "http://fkg.iust.ac.ir/ontology/residence", "http://fkg.iust.ac.ir/ontology/mayor", "http://fkg.iust.ac.ir/ontology/institution", "http://fkg.iust.ac.ir/ontology/capital", "http://fkg.iust.ac.ir/ontology/city", "http://fkg.iust.ac.ir/ontology/party", "http://fkg.iust.ac.ir/ontology/parent", "http://fkg.iust.ac.ir/ontology/manufacturer", "http://fkg.iust.ac.ir/ontology/productionCompany", "http://fkg.iust.ac.ir/ontology/award", "http://fkg.iust.ac.ir/ontology/notableWork", "http://fkg.iust.ac.ir/ontology/team", "http://fkg.iust.ac.ir/ontology/genre", "http://fkg.iust.ac.ir/ontology/distributor", "http://fkg.iust.ac.ir/ontology/largestCity", "http://fkg.iust.ac.ir/ontology/foundedBy", "http://fkg.iust.ac.ir/ontology/club", "http://fkg.iust.ac.ir/ontology/hometown", "http://fkg.iust.ac.ir/ontology/director", "http://fkg.iust.ac.ir/ontology/country", "http://fkg.iust.ac.ir/ontology/child", "http://fkg.iust.ac.ir/ontology/recordLabel", "http://fkg.iust.ac.ir/ontology/university", "http://fkg.iust.ac.ir/ontology/album"]

# allRelsInPatterns = []
# for i in range(0, len(allValidRelations)):
# 	if (allValidRelations[i]['relation'] in patternRelations):
# 		allRelsInPatterns.append(allValidRelations[i])

# print(len(allRelsInPatterns))

# savedFile = open("Source3_valids_test_format_in_patterns.json", "w", encoding='utf-8')
# savedFile.write(str(json.dumps(allRelsInPatterns, sort_keys=True, ensure_ascii=False)))
# savedFile.close()

