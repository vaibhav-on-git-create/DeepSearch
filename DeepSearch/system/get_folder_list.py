import os


def list_dir(folder_path : str , target = None , path = True):
    try :
            
        if target == None:
                
            if os.path.exists(path = folder_path):
                file_names = os.listdir(path = folder_path)

                if path:
                    return [f"{folder_path}\\{i}" for i in file_names]
                if path is False :
                    return file_names
                
            else:
                print(f"The provided path : [{folder_path}] was not found")
                return None
            
        else:

            if os.path.exists(path = folder_path):
                file_names = os.listdir(path = folder_path)

                if path: 
                    return [f"{folder_path}/{i}" for i in file_names if target in i]
                if path is False:
                    return [i for i in file_names if target in i]
                
            else:
                print(f"The provided path : [{folder_path}] was not found")
                return []
    except PermissionError as e1:
        print(f" >> Permmission denied for path : {folder_path} -- Error : [{e1}]\n") 
        return [] 
    except NotADirectoryError as e2 :
        print(f">> folder path : [{folder_path}] is not a directory [skipping] -- [{e2}]\n")
        return []

def convert_to_single_set(nested_list : list):
    return_list = []
    for i in nested_list:
        for j in i:
            return_list.append(j)

    return return_list 

def remove_duplicates(target : list):
    return_list = []
    for i in target:
        if i not in return_list:
            return_list.append(i)
        else:
            pass
    return return_list

# print(remove_duplicates([1,2,33,33]))

import os

# drive = "C:"  # Change to "D:", "E:", etc.

# try:
#     folders = [item for item in os.listdir(drive) if os.path.isdir(os.path.join(drive, item))]
#     for folder in folders:
#         print(folder)
# except PermissionError:
#     print("Run as Administrator for full access")




    

