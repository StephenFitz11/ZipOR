import pprint as pp

def get_royalty_acres(list_data):
    x = [i['Acres'] * i['Royalty'] for i in list_data]
    return sum(x)


def get_total_acres(list_data):
    total_acres = 0
    for i in list_data:
        total_acres = total_acres + i['acres']
    return total_acres


input_list = [{'name': 'CHK', 'acres': 80, 'NRI': 0.75}, {'name': 'CHK', 'acres': 80, 'NRI': 0.875}, {'name': 'CHK', 'acres': 160, 'NRI': 0.75},
              {'name': 'Roan', 'acres': 80, 'NRI': 0.8125}, {'name': 'Roan', 'acres': 80, 'NRI': 0.625}, {'name': 'Buffalo', 'acres': 80, 'NRI': 0.75},
              {'name': 'Buffalo', 'acres': 40, 'NRI': 0.785}, {'name': 'Buffalo', 'acres': 40, 'NRI': 0.8369}]




for row in input_list:
    roy_acre = row['acres'] * row['NRI']
    row['royalty acres'] = roy_acre



index_value = -1
same_entity = []
sorted_input = sorted(input_list, key = lambda i: i['name'],reverse=True)





for i in sorted_input:
    index_value += 1
    name_sort = sorted_input[index_value]


    print(name_sort)
    # try:
    #     if name_sort == sorted_input[index_value + 1]['name']:
    #         same_entity.append(i)
    # except IndexError:
    #     pass











#     Create the backend program that does the math.
#     main_list = [{'Name': v,'acres': v,'NRI': v}, {'Name': v,'acres': v,'NRI': v}, {'Name': v,'acres': v,'NRI': v,}]
#     royalty_acres = [''
#     Each row will be stored as a dictionary with the column headers as the keys.
#     Take each row and append it to the main_list
#     for i(row) in main_list
#         roy_acre = 'NRI' key * 'acre key'
#         royalty_acres.append(i)
#         royalty_acres['roy_acres'] = roy_acre

