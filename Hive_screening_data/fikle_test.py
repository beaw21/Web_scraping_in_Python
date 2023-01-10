import pandas as pd
import time
import loop_files
import requests

# commit = ['item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'break', 'item_6', 'break', 'item_7', 'item_8', 'break',
#           'item_9', 'break', 'item_10', 'item_11', 'item_12', 'item_13', 'break', 'item_14', 'item_15']

# df = pd.DataFrame(commit, columns=['items'])


def call_api(api_name):
    # api name is the name of url
    print(api_name)
    json_0bj = {}
    return json_0bj


def write_file(prefix, suffix, type_file, content):
    # create the file which name is prefix_suffix.csv
    # with open(str(prefix) + str(suffix) + str(type_file), 'w') as f:
    #     f.write(content)
    #     f.close()
    print("f")


def countdown(t):
    while t:
        print(t)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('countdown complete!!')


def loop_items(api_list):
    counter = 1
    for api_name in api_list:
        return_obj = call_api(api_name)
        if return_obj == "end":
            break;
        # write out return obj
        write_file("/commit", counter, "/.csv", return_obj)
        counter += 1
        if counter % 4 == 0:
            countdown(2)


# loop_items(df['items'])