import json
f = open('format.json')

data = json.load(f)

def getList(dict):
    return dict.values()

List = getList(data['form2'])

List = list(List)

score = 0
for i in range(len(List)):
    if List[i] == 1:
        score+=1

f.close()
