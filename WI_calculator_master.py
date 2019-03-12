import pprint as pp

def get_royalty_acres(list_data):
    x = [i['Acres'] * i['Royalty'] for i in list_data]
    return sum(x)


def get_total_acres(list_data):
    total_acres = 0
    for i in list_data:
        total_acres = total_acres + i['acres']
    return total_acres


input_names = ['CHK', 'CHK', 'CHK', 'Roan', 'Roan', 'Buffalo', 'Buffalo', 'Buffalo']
input_acreages = [80, 80, 160, 80, 80, 80, 40, 40]
input_nris = [.75, .875, .75, .8125, .625, .75, .785, .8369]
royalty_acres = [a * b for a, b in zip(input_acreages, input_nris)]





# Finds the royalty acres for each index and appends the royalty acreage to dict.
# DON'T DELETE
# for row in input_list:
#     roy_acre = row['acres'] * row['NRI']
#     row['royalty acres'] = roy_acre




#     Create the backend program that does the math.
#     main_list = [{'Name': v,'acres': v,'NRI': v}, {'Name': v,'acres': v,'NRI': v}, {'Name': v,'acres': v,'NRI': v,}]
#     royalty_acres = [''
#     Each row will be stored as a dictionary with the column headers as the keys.
#     Take each row and append it to the main_list
#     for i(row) in main_list
#         roy_acre = 'NRI' key * 'acre key'
#         royalty_acres.append(i)
#         royalty_acres['roy_acres'] = roy_acre

