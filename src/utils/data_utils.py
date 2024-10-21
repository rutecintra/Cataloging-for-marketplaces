import pandas as pd
import json

def load_data(file_path):

    return pd.read_excel(file_path).to_dict(orient='records')


def save_data_to_json(filename, data):

    with open(filename, 'w', encoding='utf-8') as json_file:
        
        json.dump(data, json_file, ensure_ascii=False, indent=4)

