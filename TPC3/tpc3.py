import re
import json
from collections import defaultdict

cases = []

def nProcessAYear():
    years = defaultdict(int)
    for case in cases:
        years[int(case["Year"])] += 1    
    
    syears = list(years.keys())
    syears.sort()
    [print(f"{sy}: {years[sy]}") for sy in syears]


def namesPerCentury():
    century_names = dict()
    most_used_names = [defaultdict(int), defaultdict(int)]
    for case in cases:
        #        FName   LName
        key = int(case["Year"])//100+1

        if key not in century_names:
            century_names[key] = [defaultdict(int), defaultdict(int)]
        
        century_names[key][0][case["FName"]] += 1
        century_names[key][1][case["LName"]] += 1
        
        most_used_names[0][case["FName"]] += 1
        most_used_names[1][case["LName"]] += 1
    
    centuries = list(century_names.keys())
    centuries.sort()
    for century in centuries:
        print(f"-------- Century:{century} --------\n---- Names: ----")
        [print(f"Name:{key} Fa:{century_names[century][0][key]}") for key in century_names[century][0]]
        print("---- Surnames ----")
        [print(f"Surname:{key} Fa:{century_names[century][1][key]}") for key in century_names[century][1]]

    top_5_names = sorted(most_used_names[0], key=most_used_names[0].get, reverse=True)[:5]
    top_5_surnames = sorted(most_used_names[1], key=most_used_names[1].get, reverse=True)[:5]

    print("--------- Top 5 Names ---------")
    [print(f"{n} -> {most_used_names[0][n]}") for n in top_5_names]

    print("--------- Top 5 Surnames ---------")
    [print(f"{n} -> {most_used_names[1][n]}") for n in top_5_surnames]

def kinship():
    kinships = defaultdict(int)
    ex = re.compile(",(?P<Kinship>[a-zA-Z ]*)\.")
    for case in cases:
        note = case["Notes"]
        if note:
            vs = ex.findall(case["Notes"])
            for v in vs:
                kinships[v] += 1
    print(kinships)

def toJSON():
    d = cases[:20]
    with open('processos.json', 'w') as file:
        json.dump(d, file, indent=4)
        print("JSON created!")


text = ["575::1900-11-08::Aarao Pereira Silva::Antonio Pereira Silva::Francisca Campos Silva::::",
        "575::2000-11-08::Aarao ::Antonio Pereira Silva::Francisca Campos Silva::::",
        "575::1918-11-08::Aarao ::Antonio Pereira Silva::Francisca Campos Silva::::"]

file = open("processos.txt", 'r')
 
p = re.compile('(?P<Folder>\d+)'
               '::'
               '(?P<Date>(?P<Year>\d{4})-(?P<Month>\d{1,2})-(?P<Day>\d{1,2}))'
               '::'
               '\W*(?P<Name>(?P<FName>\w+)(\W*\w+)*?(\W*(?P<LName>\w+))?)\W*'
               '::'
               '(?P<Dad>.+?)?'
               '::'
               '(?P<Mom>.+?)?'
               '::'
               '(?P<Notes>.+?)?'
               '::'
               )

cases = [ x.groupdict() for line in file.readlines() if (x := p.match(line))]
#cases = [ x.groupdict() for line in text if (x := p.match(line))]

kinship()

file.close()

