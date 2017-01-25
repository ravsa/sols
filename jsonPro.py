import sys

import json
import random
import string

ran = lambda x: ''.join([random.choice(string.ascii_uppercase)
                         for _ in range(x * 10)])


def is_json(myjson):
    try:
        json.loads(myjson)
    except:
        return -1
    return 1
json_string = input()
new_string = ""

for count, token in enumerate(json_string):
    if token == ":" and json_string[count + 1] not in ["[", "{"]:
        new_string = new_string + '"' + \
            ran(count) + '"' + token + '"' + ran(count) + '"'
    elif token == ":":
        new_string = new_string + '"' + ran(count) + '"' + token
    elif token == "[" and json_string[count + 1] == "]":
        print(-1)
        sys.exit()
    elif token == "{" and json_string[count+1]=="[":
        new_string = new_string + '"' + ran(count) + '"' + token
    else:
        new_string = ''.join([new_string + token])
print(is_json(new_string))
