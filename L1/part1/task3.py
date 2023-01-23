import argparse

parser = argparse.ArgumentParser()
parser.add_argument("str", nargs='?', default='')
args = parser.parse_args()

user_str = args.str
result = None
flag = False
arr = []
i = 0
sign = ''
while i < len(user_str):
    if i == 0:
        if '0' <= user_str[i] <= '9':
            sign = user_str[i]
        else:
            break
    else:
        if user_str[i] == '-' or user_str[i] == '+':
            if user_str[i - 1] == '-' or user_str[i - 1] == '+':
                arr = []
                break
            sign = ''
        elif '0' <= user_str[i] <= '9':
            if user_str[i - 1] == '-':
                sign = '-' + user_str[i]
            elif '0' <= sign <= '9':
                sign = sign + user_str[i]
            else:
                sign = user_str[i]
        else:
            arr = []
            break
    if sign != '' and (i + 1 < len(user_str) and user_str[i + 1] < '0'):
        arr.append(int(sign))
        sign = ''
    i += 1
if sign != '':
    arr.append(int(sign))
if arr:
    flag = True
    result = sum(arr)
print('user_input = \'' + user_str + '\' result = (' + str(flag) + ', ' + str(result) + ')')
