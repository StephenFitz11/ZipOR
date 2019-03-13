import json


def open_dataset(string_filename):
    """Opens the dataset as f_obj"""
    with open(string_filename) as f_obj:
        data = json.load(f_obj)
    return data


data = open_dataset('data_sample.json')


for company in data['companies']:
    roy_acre = company['acres'] * company['nri']
    company['royalty acres'] = roy_acre
