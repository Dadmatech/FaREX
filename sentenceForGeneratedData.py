import json

with open('wiki_sents_cleaned_30.txt', encoding='utf-8') as file:
    for line in file:
    	sentence = line.rstrip()
    	tokenizedSentence = sentence.split(' ')
    	if (len(tokenizedSentence) > 7 and len(tokenizedSentence) < 13):
        	print(sentence)