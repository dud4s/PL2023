import re

while True:
    user_input = input('>> ')
    
    if not user_input:
        break

    result = re.findall(r'(?i)on|off|\d|=', user_input)
    to_sum = True
    total = 0
    for r in result:
        if r.lower() == 'on':
            to_sum = True
        elif r.lower() == 'off': 
            to_sum = False
        elif r == '=':
            print('Current Sum:', total)
        else:
            if to_sum:
                total += int(r)

    print('Sum:', total)
