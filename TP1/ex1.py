#idade,sexo,tensão,colesterol,batimento,temDoença

def gender_dist(data):
    d = {}
    for l in data:
        if l[1] in d:
            d[l[1]] += 1
        else:
            d[l[1]] = 0
    return d

def get_interval(value, k):
    min_range = value - value % k 
    max_range = min_range + k-1
    return f"[{str(min_range)}-{str(max_range)}]"

def age_dist(data, k):
    d = {}
    for l in data:
        age = int(l[0])
        s = get_interval(age, k)
        if s in d:
            d[s] += 1
        else:
            d[s] = 0
    return d

def cholesterol_dist(data, k):
    d = {}
    for l in data:
        cholesterol = int(l[0])
        s = get_interval(cholesterol, k)
        if s in d:
            d[s] += 1
        else: d[s] = 0
    return d

data = []
with open("myheart.csv", 'r') as file:
    for l in file:
        row = []
        for param in l.split(','):
            row.append(param)
        row.pop(-1)
        data.append(row)
    data.pop(0)
print(gender_dist(data))
print(age_dist(data, 5))
print(cholesterol_dist(data, 10))
