import os
import json


def __create_first_draw():
    all_dirs = os.listdir(os.path.join(os.getcwd(), "data/stanford-car-dataset-by-classes-folder/car_data/car_data/test"))
    json_output_file_path = os.path.join(os.getcwd(), "data_reader/_json_data/car_data.json")

    three_element_path = [data for data in all_dirs if len(data.split(" ")) == 3]
    other_len_element_path = [data for data in all_dirs if len(data.split(" ")) != 3]

    dict_data = {"stanford-car-dataset-by-classes-folder": {}}

    with open(os.path.join(os.getcwd(), "data/stanford-car-dataset-by-classes-folder/names.csv"), "r") as csv_file:
        lines_in_csv = csv_file.readlines()

    for dir_name in three_element_path:
        car_type, car_model, _ = dir_name.split(" ")
        for line in lines_in_csv:
            if dir_name in line:
                production_year = line.split(" ")[-1]
                break
        else:
            production_year = 9999

        dict_data["stanford-car-dataset-by-classes-folder"][dir_name] = {
            "car_type": car_type,
            "car_model": car_model,
            "production_year": int(production_year)
        }
    for dir_name in other_len_element_path:
        for line in lines_in_csv:
            if dir_name in line:
                production_year = line.split(" ")[-1]
                break
        else:
            production_year = 9999
        dict_data["stanford-car-dataset-by-classes-folder"][dir_name] = {
            "car_type": "",
            "car_model": "",
            "production_year": int(production_year)
        }

    with open(json_output_file_path, 'w') as outfile:
        json.dump(dict_data, outfile)


def add_indexes_to_cars():
    with open(os.path.join(os.path.dirname(__file__), "car_data.json"), "r") as infile:
        json_data = json.load(infile)

    for i, car_name in enumerate(json_data["stanford-car-dataset-by-classes-folder"].keys()):
        json_data["stanford-car-dataset-by-classes-folder"][car_name]["num_value"] = i

    with open(os.path.join(os.path.dirname(__file__), "car_data.json"), "w") as outfile:
        json.dump(json_data, outfile)


if __name__ == "__main__":
    add_indexes_to_cars()
