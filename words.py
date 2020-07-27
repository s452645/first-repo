import os
import json

ranking = dict()

# pełna ścieżka do inboxa (+ '\\' na końcu)
path = "C:\\Users\\Dell\\Desktop\\Facebook Stats\\main\\messages\\inbox\\"

for directory_name in os.listdir(path):
    i = 1
    counter = 0

    file_name = path + directory_name + "\\message_" + str(i) + ".json"

    while os.path.isfile(file_name):
        with open(file_name, "r") as read_file:
            data = json.load(read_file)

        for message in data['messages']:
            if 'content' in message:
                words = message['content'].split()

                for word in words:
                    if word in ranking.keys():
                        ranking[word] += 1
                    else:
                        ranking[word] = 1

        i += 1
        file_name = path + directory_name + "\\message_" + str(i) + ".json"

sorted_ranking = sorted(ranking.items(), key=lambda x: x[1], reverse=True)

n = 1

# PyCharm nie wyświetli setek tysięcy linii, skończysz z około 40k ostatnich xD
limit = 40000
for element in sorted_ranking:
    if limit > 0:
        print(str(n) + ". '" + element[0] + "' ->  " + str(element[1]))
        n += 1
        limit -= 1
    else:
        break

