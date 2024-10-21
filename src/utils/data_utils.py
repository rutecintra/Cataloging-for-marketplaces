import json

def save_data_to_json(filename, data):

    with open(filename, 'w', encoding='utf-8') as json_file:
        
        json.dump(data, json_file, ensure_ascii=False, indent=4)

