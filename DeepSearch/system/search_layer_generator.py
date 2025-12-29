import get_folder_list
import classify_dir

# import ctypes
# import sys



# def is_admin():
#     try:
#         return ctypes.windll.shell32.IsUserAnAdmin()
#     except:
#         return False


# if not is_admin():
# # Relaunch as admin
#     params = " ".join([f'"{arg}"' for arg in sys.argv])
# ctypes.windll.shell32.ShellExecuteW(
#     None,
#     "runas",
#     sys.executable,
#     params,
#     None,
#     1
# )
# sys.exit(0)


def generate_search_layers(parent_path : str):


    layers = [[parent_path]]
    it = 0
   

    while it <= 1:
    
        layer_element = []

        for layer in layers[-1]:
    
            if type(layer) == list:

                all_file_list = get_folder_list.convert_to_single_set([get_folder_list.list_dir(i) for i in layer])
            else:
                all_file_list = get_folder_list.list_dir(folder_path=layer)

            all_folder_list = classify_dir.list_all_folder(paths_list=all_file_list)
            
            if all_folder_list not in layer_element:
                layer_element.append(all_folder_list)

            for folder in all_folder_list:
                sub_file_list = get_folder_list.list_dir(folder_path=folder)
                sub_folders_list = classify_dir.list_all_folder(paths_list=sub_file_list)
                layer_element.append(sub_folders_list)

        layer_element = get_folder_list.remove_duplicates(target=layer_element)
        single_layer_data = get_folder_list.convert_to_single_set(nested_list=layer_element)
        layer_element.append(single_layer_data)
        layers.append(layer_element)
        for iter_ in layers:
            if iter_ == [parent_path]:
                layers.remove([parent_path])
        it+=1
    
    final_search_layers = []
    for lyer in layers:
        temp_list = get_folder_list.convert_to_single_set(lyer)
        final_search_layers.append(temp_list)
    
    final_search_layers = get_folder_list.convert_to_single_set(final_search_layers)
    final_search_layers = get_folder_list.remove_duplicates(final_search_layers)
    
    return get_folder_list.remove_duplicates(final_search_layers)

    
    
