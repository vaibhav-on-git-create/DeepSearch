import get_folder_list
import match_words
import classify_dir
import search_layer_generator

def get_max_num(num_array : list):
    max_val = 0
    i = 0 
    while i < len(num_array):
        if num_array[i] > max_val:
            max_val = num_array[i]
        i+=1

    return max_val

def sort_num_array(num_array : list , sort_index = False):
    i =0 
    array = num_array.copy()
    index_list = list(range(len(array)))
    while i < len(array):
        sub_list = array[i:]
        max_element = get_max_num(sub_list)
        max_index = sub_list.index(max_element) + i

        array[i] , array[max_index] = array[max_index] , array[i]
        index_list[i] , index_list[max_index] = index_list[max_index] , index_list[i]

        i+=1

    if sort_index:
        return index_list
    else:
        return array

# list_1 = [3,4,1,2,3,4,9,6,7]

# print(sort_num_array(num_array=list_1,sort_index=True))

# print(get_max_num(list_1))

def list_highest_num(num_array : list , max_count : int = 2):
    
    num_array = get_folder_list.remove_duplicates(target=num_array)
    if max_count > len(num_array):
        max_count = len(num_array)

    max_list = []
    for i in range(max_count):

        max_num = get_max_num(num_array=num_array)
        max_list.append(max_num)
        num_array.remove(max_num)
        

    return max_list

# print(list_highest_num(num_array=[1,1,2,2,0.5,0.5] , max_count=10))

def fetch_all_files(parent_dir : str):

    # parent_dir = "e:\\movies"
    all_files = []
    all_folder_list = get_folder_list.remove_duplicates(search_layer_generator.generate_search_layers(parent_path=parent_dir))
    for folders in all_folder_list:
        files = get_folder_list.remove_duplicates(get_folder_list.remove_duplicates([file for file in get_folder_list.list_dir(folder_path = folders) if classify_dir.check_if_folder(path=file) is not True]))
        for i in files:
            if i not in all_files:
                all_files.append(i)
    return all_files

def create_match_score_data(file_names : list, word : str):
    data = {}
    for files in file_names:
        file_name = classify_dir.convert_to_name(path=files).lower()
        data[f"{file_name}_{file_names.index(files)}"] = [
            match_words.match_words(main_word=file_name , match_word=word) , files]
        
    return data

# print(create_match_score_data(file_names=fetch_all_files(parent_dir="e:\\movies") , word="peaky blinders"))
# >> returns {key_with_serial : [score , path]}

def list_top_scores(data_dict : dict , num_tops : int):
    all_keys = list(data_dict.keys())
    all_score_list = []
    
    for i in all_keys:
        all_score_list.append(data_dict[i][0])

    high_nums = list_highest_num(num_array=all_score_list , max_count=num_tops)

    return high_nums

# list_top_scores(data_dict=create_match_score_data(file_names=fetch_all_files(parent_dir="e:\\movies") , word="peaky blinders"),
#                  num_tops=100)

def pre_search_file(parent_dir : str , search_key_word : str , top_results : int = 1 ,max_row_wigth : int = 27 , display : bool = True):
        
    all_files_dicts = create_match_score_data(file_names=fetch_all_files(parent_dir=parent_dir) , word=search_key_word)
    all_files_names = list(all_files_dicts.keys())
    num_top_results = top_results
    top_match_scores = list_top_scores(data_dict = all_files_dicts , num_tops=num_top_results)

    result_array_keys = []
    score_array = []
    # fetching matched results also sorting the scores and recording the indexs and later 
    # using the sequence to arrage the result dict keys to
    # make display list of match results

    for i in all_files_names:
        iter_data = all_files_dicts[i]
        score = iter_data[0]
        if score in top_match_scores:
            result_array_keys.append(i)
            score_array.append(score)

    arranged_keys = []
    sorted_score_seq = sort_num_array(num_array=score_array , sort_index=True)

    for index in sorted_score_seq:
        arranged_keys.append(result_array_keys[index])

    final_arrays = [["serial","file names","match score" , "paths"]]
    actual_array = [["serial","file names","match score" , "paths"]]
    serial = 1
    for key in arranged_keys:
        print(key)

        key_element = all_files_dicts[key]
        key_score = key_element[0]
        key_path = key_element[-1]
        folder_path = "\\".join([ _ for _ in key_path.split("\\")][0:-1])

        actual_array.append( [str(serial) ,classify_dir.get_file_name(key)[0:max_row_wigth-3] , f"{key_score} %" , key_path])

        if len(folder_path) < 27:
            final_arrays.append([str(serial) ,classify_dir.get_file_name(key)[0:max_row_wigth] , f"{key_score} %" , folder_path])
        else:
            final_arrays.append([str(serial) ,classify_dir.get_file_name(key)[0:max_row_wigth] , f"{key_score} %" , folder_path[0:max_row_wigth+1]])
        serial+=1

    if display:  
        return final_arrays #to display folder only
    
    else:
        return [final_arrays , actual_array] #to fetch full path of the file
    
# results = pre_search_file(parent_dir=r"C:\Users\Vaibhav\Desktop" ,search_key_word="friday" , top_results=1 , max_row_wigth=40)
# print(tabulate.tabulate(results , headers="firstrow",tablefmt="fancy_grids" ,maxcolwidths=[None , 100] ))









