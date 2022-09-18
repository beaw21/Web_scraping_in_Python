import pandas as pd
import numpy as np
import requests

import json

# Opening JSON file
with open('pull.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    json_obj = json.dumps(json_object)

    # print(json_object)
    print(type(json_object))
    # print(json_obj)
    print("The type of object is: ", type(json_obj))

