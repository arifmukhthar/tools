import csv
import os

list1 = []
list2 = []
def remove_item_from_list(item, list_to_remove_from):
    if item in list_to_remove_from:
        list_to_remove_from.remove(item)


def remove_list1_item_from_list2(list1, list2):
    for item in list1:
        remove_item_from_list(item, list2)


def get_list_from_csv(_csv_file_path):
    with open(_csv_file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            list1.append(row["oldname"].lower().replace(".", " "))
            list2.append(row["newname"].lower().replace(".", " "))

    return list1, list2


def export_dict_as_csv(dict):
    if os.path.exists("/Users/uumarar/Desktop/newusers.csv"):
        os.remove("/Users/uumarar/Desktop/newusers.csv")
    with open("/Users/uumarar/Desktop/newusers.csv", 'a') as myfile:
        writer = csv.writer(myfile)
        writer.writerow(dict.keys())
        writer.writerows(zip(*dict.values()))
    myfile.close()


def convert_list_to_dict(list):
    new_user_dict = {"new_user": []}
    for value in list:
        value = value.title()
        new_user_dict["new_user"].append(value)
    return new_user_dict


csv_file_path = "/Users/uumarar/Desktop/test.csv"
list1, list2 = get_list_from_csv(csv_file_path)
remove_list1_item_from_list2(list1, list2)
export_dict_as_csv(convert_list_to_dict(list2))
print(len(list2))
