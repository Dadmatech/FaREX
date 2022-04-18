import csv
import json


with open('wiki_gold_our_relations_21-30_words.json', encoding='utf-8') as file:
    readFile = file.read()
    aaa = json.loads(readFile)


# with open('wiki_gold_our_relations_20_words.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL,delimiter='\n')
#     wr.writerow(aaa)

import pandas

goldWikiUpTo20WordsID = 3
goldWiki21To30WordsID = 4

df = pandas.DataFrame(columns=["sentence", "head_word", "head_url", "head_start", "head_length", 
    "tail_word", "tail_url", "tail_start", "tail_length", "property", "property_caption", "why", "source_data"])

dfs = pandas.read_excel('Properties_refined_two_side_entity_filterd.xlsx', sheet_name='Sheet1')

propertyCaptions = {}
for i in range(0, len(dfs['URL'])):
    propertyCaptions[dfs['URL'][i]] = dfs['translatedLabel'][i]

for i in range(0, len(aaa)):
    caption = propertyCaptions[aaa[i]['relation']]
    df.loc[i] = [aaa[i]['sentence'], aaa[i]['head']['word'], aaa[i]['head']['id'], aaa[i]['head']['start'], aaa[i]['head']['length'],
    aaa[i]['tail']['word'], aaa[i]['tail']['id'], aaa[i]['tail']['start'], aaa[i]['tail']['length'], aaa[i]['relation'], caption,
    "manually_tagged_data", goldWiki21To30WordsID]

df.to_csv("./wiki_gold_our_relations_21ـ30_words.csv", sep=',',index=False)


# newJsonFormat = []
# for i in range(0, len(aaa)):
#     relation = {}
#     relation['id'] = i
#     relation['sentence'] = aaa[i]['sentence']
#     relation['head_word'] = aaa[i]['head']['word']
#     relation['head_url'] = aaa[i]['head']['id']
#     relation['head_start'] = aaa[i]['head']['start']
#     relation['head_length'] = aaa[i]['head']['length']
#     relation['tail_word'] = aaa[i]['tail']['word']
#     relation['tail_url'] = aaa[i]['tail']['id']
#     relation['tail_start'] = aaa[i]['tail']['start']
#     relation['tail_length'] = aaa[i]['tail']['length']
#     relation['property'] = aaa[i]['relation']
#     relation['property_caption'] = propertyCaptions[aaa[i]['relation']]
#     relation['why'] = "manually_tagged_data"
#     relation['source_data'] = "wiki_gold_our_relations_20_words"

#     newJsonFormat.append(relation)

# savedFile = open("wiki_gold_our_relations_20_words_new_json_format.json", "w", encoding='utf-8')
# savedFile.write(str(json.dumps(newJsonFormat, indent=4, sort_keys=True, ensure_ascii=False)))
# savedFile.close()