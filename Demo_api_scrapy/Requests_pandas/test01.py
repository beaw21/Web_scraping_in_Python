import json

print("Started Reading JSON file")
with open("test01.json", "r") as read_file:
    print("Converting JSON encoded data into Python dictionary")
    developer = json.load(read_file)

    print("Decoded JSON Data From File")
    for key, value in developer.items():
        print(key, ":", value)
    print("Done reading json file")