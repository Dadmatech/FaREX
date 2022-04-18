import json
import pandas as pd
import operator
import collections

with open('trainSpad.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]


with open('semeval_test.txt') as file:
    linesTest = file.readlines()
    linesTest = [line.rstrip() for line in linesTest]


print(len(lines))


foundedRels = []
rels = {}
counter = 0
alltries = 0
for i in range(0, len(lines)):
	try:
		rel = json.loads(lines[i].replace('\'', '\"'))['relation']
		alltries += 1
		if (not rel in foundedRels):
			foundedRels.append(rel)
			rels[rel] = counter
			counter += 1
	except Exception as e:
		pass


linesTestFoundedRels = []
linesTestRels = {}
linesTestCounter = 0
linesTestAlltries = 0
for i in range(0, len(linesTest)):
	try:
		rel = json.loads(linesTest[i].replace('\'', '\"'))['relation']
		linesTestAlltries += 1
		if (not rel in linesTestFoundedRels):
			linesTestFoundedRels.append(rel)
			linesTestRels[rel] = linesTestCounter
			linesTestCounter += 1
	except Exception as e:
		pass


for j in range(0, len(linesTestFoundedRels)):
	if (not linesTestFoundedRels[j] in foundedRels):
		print(linesTestFoundedRels[j])


# rels = sorted(rels.items(), key=lambda kv: kv[1])

# savedFile = open("relation_ids_in_spad_train.json", "w", encoding='utf-8')
# savedFile.write(str(json.dumps(rels, indent=4, sort_keys=True, ensure_ascii=False)))
# savedFile.close()
