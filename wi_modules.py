import json


def open_dataset(string_filename):
    """Opens the dataset as f_obj"""
    with open(string_filename) as f_obj:
        data = json.load(f_obj)
    return data


def list_companies(dataset):
    all_companies = []
    for company in dataset['companies']:
        all_companies.append(company['Name'])
    all_companies = list(dict.fromkeys(all_companies))
    return all_companies


def calculate_royac(dataset):
    """Appends the royalty acres to each dictionary"""
    for company in dataset['companies']:
        roy_acre = company['Acres'] * company['NRI']
        company['royalty_acres'] = roy_acre


def get_royalty_acres(key, dataset):
    """Sums the royalty acres of a given [key] in JSON file"""
    total_royac = 0
    for company in dataset['companies']:
        if company['Name'] == key:
            total_royac += company['royalty_acres']
    return total_royac


def get_total_acres(key, dataset):
    """Sums the royalty acres of a given [key] in JSON file"""
    total_royac = 0
    for company in dataset['companies']:
        if company['Name'] == key:
            total_royac += company['Acres']
    return total_royac


def find_weighted_nri(key, dataset):
    """Computes the weighted NRI of a given key from JSON"""
    return get_royalty_acres(key, dataset) / get_total_acres(key, dataset)
