import get_folder_list

def check_if_folder(path : str ):
    
    path_split = [i for i in path.split("\\")][-1]
    
    if "." not in path_split:
        return True
    else:
        return False
    
def get_file_name(file_path : str):
    pros_name = [i for i in file_path.split("\\")][-1]
    if "/" not in pros_name:
        return pros_name
    else:
        return [j for j in pros_name.split("/")][-1]

def list_all_folder(paths_list : list):
    try:

        return_list = []
        for files in paths_list:
            if check_if_folder(path=files):
                return_list.append(files)
            else:
                pass

    except TypeError:
        return []



    return return_list

def check_if_folder_in_layer(layer_element : list):
    bool_seq = []
    for files in layer_element:
        dir_list = get_folder_list.list_dir(folder_path=files)
        count = 0
        for pointer in dir_list:
            if check_if_folder(path=pointer):
                count+=1
        if count > 0:
            bool_seq.append(True)
        else:
            bool_seq.append(False)
    
    return bool_seq

def convert_to_name(path : str):
    split_path = []
    if "/" in path:
        split_path = path.split("/")
    else:
        split_path = path.split("\\")
    return split_path[-1]

# print(convert_to_name(path=r"D:\My_projects\system_utility\DeepSearch/logs.text"))

# print(check_if_folder_in_layer(layer_element=[str(r"D:\My_projects\system_utility\DeepSearch\system"),
#                                         str(r"D:\My_projects\system_utility\DeepSearch\logs")]))
# print(check_if_folder(path=str(r"D:\My_projects\system_utility\DeepSearch\logs.")))
# print(list_all_folder(paths_list=[str(r"D:\My_projects\system_utility\DeepSearch\logs.text")]))

    






