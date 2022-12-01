import pandas as pd
import time
import loop_files
import requests

commit = ['item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'break', 'item_6', 'break', 'item_7', 'item_8', 'break',
          'item_9', 'break', 'item_10', 'item_11', 'item_12', 'item_13', 'break', 'item_14', 'item_15']

df = pd.DataFrame(commit, columns=['items'])


# data_list_col = []
def call_api(api_name):
    # api name is the name of url
    # call
    print(api_name)
    jsonobj = {}
    return jsonobj


def write_file(prefix, suffix, content):
    # create the file which name is prefix_suffix.csv
    print('hello')


def countdown(t):
    while t:
        print(t)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Fire in the hole!!')


def loop_items(api_list):
    counter = 1
    for api_name in api_list:
        return_obj = call_api(api_name)
        # write out return obj
        write_file("/commit", counter, return_obj)
        counter += 1
        if counter % 2 == 0:
            countdown(10)

        # data_api = i
        # # data_list_col = data_api
        # print("api number :" + i)
        # # print("list :" + data_list_col)
        # if i == "break":
        #     break


loop_items(df['items'])

# define the countdown func.


# input time in seconds
# t = input("Enter the time in seconds: ")
# 35 * 60 = 2100
# t = 2
# function call
# countdown(int(t))
