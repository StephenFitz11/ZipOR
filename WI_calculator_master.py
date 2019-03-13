import json

from wi_modules import *
# TODO: Learn JSON dump from a GUI

data = open_dataset('data.json')
calculate_royac(data)
companies = list_companies(data)
companies_weightednri = []
for company in companies:
    x = find_weighted_nri(company, data)
    update_kvalue = {company: x, 'total_ac': get_total_acres(company, data)}
    companies_weightednri.append(update_kvalue)

print(companies_weightednri)