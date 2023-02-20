#idade,sexo,tensão,colesterol,batimento,temDoença
from tabulate import tabulate
import matplotlib as plt

def add_dict(d, v):
    if v in d:
        d[v] += 1
    else: d[v] = 1

def create_dist_by_column(data, column, period):
    d = {}
    for l in data:
        x = l[column]
        if period != 0:
            x = get_interval(int(l[column]), period)
        if int(l[-1]) == 1:
            add_dict(d, x)
    return d

def get_interval(value, k):
    min_range = value - value % k 
    max_range = min_range + k-1
    return f"[{str(min_range)}-{str(max_range)}]"

# Displays a given distribution (dictionary) as a table, followed by it's headers
def display_dist(d, headers):
    all_data = []
    total = sum(d.values())
    for key in d.keys():
        all_data.append([key, d[key], round(d[key] / total * 100, 2)])
     
    all_data.sort(key=lambda x: x[1], reverse=True)
    headers.append("rf (%)")
    print(tabulate(all_data, headers=headers, tablefmt='grid'))
    

data = []
with open("myheart.csv", 'r') as file:
    for l in file:
        row = []
        for param in l.strip().split(','):
            row.append(param)
        data.append(row)
    data.pop(0)

print("-----------")
print("     ------- TPC1 -------")
print("                   -----------")
while True:
    op = int(input('Type of Distribution:\n1 - Gender\n2 - Age\n3 - Cholesterol\n4 - Exit\nOption: '))
    if op == 1:
        display_dist(create_dist_by_column(data, 1, 0), ['Gender', 'Number of ill persons (af)'])
    elif op == 2:
        display_dist(create_dist_by_column(data, 0, 5), ['Age', 'Number of ill persons (af)'])
    elif op == 3:
        display_dist(create_dist_by_column(data, 3, 10), ['Cholesterol Levels', 'Number of ill persons (af)'])
    elif op == 4:
        break

