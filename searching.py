import os
import json
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name) #vypise cestu k souboru

    with open(file_path) as data_file:
        data = json.load(data_file)

    if field in data.keys():
        return data[field]
    else:
        return None


    return data[field]


def linear_search(sequence, number):
    pass



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)


if __name__ == '__main__':
    main()