import json

spadLabels = {
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

with open('all_gold_valids_test_format.json', encoding='utf-8') as file:
    readFile = file.read()
    valid = json.loads(readFile)

spadLabelsKeys = spadLabels.keys()

print(valid[0])
withSpadLabel = []
for i in range (0, len(valid)):
	if (valid[i]['relation'] in spadLabelsKeys):
		withSpadLabel.append(valid[i])

print(len(valid))
print(len(withSpadLabel))

savedFile = open("gold_valids_test_format_in_spad.json", "w", encoding='utf-8')
savedFile.write(str(json.dumps(withSpadLabel, sort_keys=True, ensure_ascii=False)))
savedFile.close()