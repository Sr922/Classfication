import json

def write_to_file(file_name, data):
	with open(file_name, 'w') as outfile:
		json.dump(data, outfile)


with open('./keywords/java_easy.json') as json_data:
    easy_words = json.load(json_data)
    filtered_words = []
    for word in easy_words:
    	if word not in filtered_words:
    		filtered_words.append(word)

    if(len(easy_words) != len(filtered_words)):
    	write_to_file('./keywords/java_easy.json', filtered_words)

    print(len(easy_words))
    print(len(filtered_words))

with open('./keywords/java_medium.json') as json_data:
    medium_words = json.load(json_data)
    filtered_words = []
    for word in medium_words:
    	if word not in filtered_words:
    		filtered_words.append(word)

    if(len(medium_words) != len(filtered_words)):
		write_to_file('./keywords/java_medium.json', filtered_words)
    
    print(len(medium_words))
    print(len(filtered_words))

with open('./keywords/java_difficult.json') as json_data:
    difficult_words = json.load(json_data)
    filtered_words = []
    for word in difficult_words:
    	if word not in filtered_words:
    		filtered_words.append(word)

    if(len(difficult_words) != len(filtered_words)):
    	write_to_file('./keywords/java_difficult.json', filtered_words)
    
    print(len(difficult_words))
    print(len(filtered_words))
