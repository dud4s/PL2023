import re
import json

def toJSON(d):
    with open("myjson.json", "w") as file:
        json.dump(d, file, indent=4, ensure_ascii=False)
        print("JSON Created!")



csv_lines = open("test2.csv", "r").readlines()
headers = csv_lines[0].rstrip('\n').split(',')
lines = csv_lines[1:]

d = []


toJSON(d)