import json
import pandas as pd

with open('Final_FarsBase_DS_Gold-With-Babelfy.json.fixed.reid.constituency', encoding='utf-8') as file:
	readFile = file.read()
	aaa = json.loads(readFile)

# print(len(aaa))
# print(aaa['numberOfDistinctRelations'])
# print(aaa['sizeMismatch'])
# print(aaa['notMatchedTokenization'])
# print(aaa['notAdjacentSubObj'])
# print(aaa['unknownException'])
# print(len(aaa['allStats']))
# print(aaa['allStats'].keys())
# print(aaa['allStats']['numberOfPositiveRelations'])
# print(aaa['allStats']['numberOfNegativeRelations'])
# print(len(aaa['relationStats']))
# print(aaa['relationStats']['fkgo:metabolism'])
# print(len(aaa['relationStats']['fkgo:county']))
# # print(aaa['relationStats'].keys())

dfs = pd.read_excel('Properties_refined_two_side_entity_filterd.xlsx', sheet_name='Sheet1')

print(dfs.keys())

relationsKeys = aaa['relations']
allRelations = []
exceptions = []
for rel in relationsKeys:
	for sentenceIndex in range (0, len(aaa['relations'][rel]['positives'])):
		try:
			relSubjectURI = aaa['relations'][rel]['positives'][sentenceIndex]['subject']
			relSubjectWord = ''
			relSubjectFounded = False
			relObjectURI = aaa['relations'][rel]['positives'][sentenceIndex]['object']
			relObjectWord = ''
			relObjectFounded = False
			predicate = aaa['relations'][rel]['positives'][sentenceIndex]['predicates'][0]
			# if ('بتمن' in relSubjectURI and 'بروس_وین' in relObjectURI and ('name' in predicate)):
				# print(aaa['relations'][rel]['positives'][sentenceIndex]['tokens'])
			relSentence = ''
			for i in range(0, len(aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0])):
				relSentence += aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['word']
				relSentence += ' '
				try:
					if (aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['relationArgNumber'] == 1):
						tempRelSubjectWord = relSubjectWord + aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['word'] + ' '
						if (tempRelSubjectWord in relSentence):
							relSubjectWord += aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['word']
							relSubjectWord += ' '
							relSubjectFounded = True

					elif (aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['relationArgNumber'] == 2):
						tempRelObjectWord = relObjectWord + aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['word'] + ' '
						if (tempRelObjectWord in relSentence):
							relObjectWord += aaa['relations'][rel]['positives'][sentenceIndex]['tokens'][0][i]['word']
							relObjectWord += ' '
							relObjectFounded = True
				except:
					if (not aaa['relations'][rel]['positives'][sentenceIndex] in exceptions):
						exceptions.append(aaa['relations'][rel]['positives'][sentenceIndex])

			relSubjectStart = relSentence.find(relSubjectWord)
			relObjectStart = relSentence.find(relObjectWord)

			head = {}
			head['id'] = relSubjectURI
			head['word'] = relSubjectWord[:-1]
			head['start'] = relSubjectStart
			head['length'] = len(relSubjectWord)-1

			tail = {}
			tail['id'] = relObjectURI
			tail['word'] = relObjectWord[:-1]
			tail['start'] = relObjectStart
			tail['length'] = len(relObjectWord)-1

			relation = {}
			relation['head'] = head
			relation['tail'] = tail
			relation['sentence'] = relSentence[:-1]
			relation['relation'] = 'http://fkg.iust.ac.ir/ontology/' + predicate.split(':')[1]

			if (relSubjectFounded and relObjectFounded):
				allRelations.append(relation)

			# print(aaa['relations']['fkgo:editor']['positives'][0])
			# print(relSentence)
			# print(relSubjectWord)
			# print(relSubjectURI)
			# print(relObjectWord)
			# print(relObjectURI)
			# print(predicate)

		except:
			print(aaa['relations'][rel]['positives'][sentenceIndex])
			print("An exception occurred")


print("numOfCorrectFormat = ", len(allRelations))

ourURLs = []
for i in range(0, 104):
	ourURLs.append(dfs['URL'][i])

ourRelations = []

for i in range (0, len(allRelations)):
	if (allRelations[i]['relation'] in ourURLs):
		ourRelations.append(allRelations[i])

print("numOfOurRelations = ", len(ourRelations))

ourRelationsSmallSentences = []

for i in range (0, len(ourRelations)):
	if (len(ourRelations[i]['sentence'].split(" ")) > 21 and len(ourRelations[i]['sentence'].split(" ")) < 31):
		ourRelationsSmallSentences.append(ourRelations[i])

print("numOfOurRelations = ", len(ourRelationsSmallSentences))

savedFile = open("Final_FarsBase_DS_Gold.json", "w", encoding='utf-8')
savedFile.write(str(json.dumps(allRelations, indent=4, sort_keys=True, ensure_ascii=False)))
savedFile.close()


savedFile = open("exceptions.json", "w", encoding='utf-8')
savedFile.write(str(json.dumps(exceptions, indent=4, sort_keys=True, ensure_ascii=False)))
savedFile.close()

savedFile = open("ourRelations.json", "w", encoding='utf-8')
savedFile.write(str(json.dumps(ourRelations, indent=4, sort_keys=True, ensure_ascii=False)))
savedFile.close()

savedFile = open("ourRelationsSmallSentences.json", "w", encoding='utf-8')
savedFile.write(str(json.dumps(ourRelationsSmallSentences, indent=4, sort_keys=True, ensure_ascii=False)))
savedFile.close()

