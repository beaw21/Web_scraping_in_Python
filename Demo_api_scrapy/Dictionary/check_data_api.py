import ast
import pandas as pd
import numpy as np
import requests
from pandas import json_normalize
import json

# Opening JSON file
with open('pull_closed1.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    data = json.dumps(json_object)

    print("The type of object is: ", type(openfile))
    print("The type of object is: ", type(json_object))
    print("The type of object is: ", type(data))

# df = ast.literal_eval(openfile)
#     with open('readme.json', 'w') as f:
#         f.write(data)

# x = open('readme.json')
# print("The type of object is: ", type(x))

    test = json.dumps(data)
    print("The type of object is: ", type(test))
    # convert string to  object
    json_object_test = json.loads(test)
    print("The type of object is: ", type(json_object_test))

