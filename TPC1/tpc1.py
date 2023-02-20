#idade,sexo,tensão,colesterol,batimento,temDoença
from tabulate import tabulate
import matplotlib as plt

# Creates a gender distribution
def gender_dist(data):
    d = {}
    for l in data:
        if int(l[-1]) == 1:
            if l[1] in d:
                d[l[1]] += 1
            else:
                d[l[1]] = 1
    return d

def get_interval(value, k):
    min_range = value - value % k 
    max_range = min_range + k-1
    return f"[{str(min_range)}-{str(max_range)}]"

# Creates an age distribution 
def age_dist(data, k):
    d = {}
    for l in data:
        age = int(l[0])
        s = get_interval(age, k)
        if int(l[-1]) == 1:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
    return d

# Creates a cholesterol distribution, with a given k as an age interval
def cholesterol_dist(data, k):
    d = {}
    for l in data:
        cholesterol = int(l[0])
        s = get_interval(cholesterol, k)
        if int(l[-1]) == 1:
            if s in d:
                d[s] += 1
            else: d[s] = 1
    return d


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
        for param in l.split(','):
            row.append(param)
        data.append(row)
    data.pop(0)

print("-----------")
print("     ------- TPC1 -------")
print("                   -----------")
while True:
    op = int(input('Type of Distribution:\n1 - Gender\n2 - Age\n3 - Cholesterol\n4 - Exit\nOption: '))
    if op == 1:
        display_dist(gender_dist(data), ['Gender', 'Number of ill persons (af)'])
    elif op == 2:
        display_dist(age_dist(data, 5), ['Age', 'Number of ill persons (af)'])
    elif op == 3:
        display_dist(cholesterol_dist(data, 10), ['Cholesterol Levels', 'Number of ill persons (af)'])
    elif op == 4:
        break

