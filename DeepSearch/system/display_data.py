
import search_mechanism
import get_folder_list

def get_max_num(num_array : list):
    max_val = 0
    i = 0 
    while i < len(num_array):
        if num_array[i] > max_val:
            max_val = num_array[i]
        i+=1

    return max_val

# test = [
#     ["Item",  "Price"],
#     ["Pizza", 850],
#     ["Burger", 500],
#     ["Salad", 475],
#     ["Pasta", 725],
# ]

def display_data(sheet_data : list,display : bool = True , max_wight_limit : int = 40):

    data_sheet = sheet_data #search_mechanism.results
    header_lengths = len(data_sheet[0])

    for pros_length in data_sheet:
        if len(pros_length) < header_lengths:
            diff = header_lengths - pros_length
            for appendature in range(diff):
                data_sheet[data_sheet.index(pros_length)].append("NULL")

    counter_1 = 0
    max_wights = []
    while counter_1 < header_lengths:
        max_at_index = []

        for len_1 in data_sheet:
            # print(len_1)
            at_index_len = len(str(len_1[counter_1]))
            max_at_index.append(at_index_len)

        max_wights.append(get_max_num(num_array=max_at_index))

        counter_1+=1

    # max_wights

    counter_2 = 0

    while counter_2 < len(max_wights):
        for element in data_sheet:
            if counter_2 == 0:

                if len(element[counter_2]) <= max_wight_limit:
                    element[counter_2] = element[counter_2]
                else:
                    element[counter_2] = element[counter_2][0:max_wight_limit]

                diff_2 = max_wights[counter_2] - len(element[counter_2])
                if diff_2 == 0:
                    element[counter_2] = f"| {element[counter_2]}{(diff_2+1)*' '}|"
                else:
                    element[counter_2] = f"| {element[counter_2]}{(diff_2+1)*' '}|"

            else:
                diff_2 = max_wights[counter_2] - len(str(element[counter_2]))
                element[counter_2] = f" {element[counter_2]}{(diff_2+1)*' '}|"

        counter_2 +=1

    # print(data_sheet)
    display_sheet = []

    for data in data_sheet:
        display_sheet.append("".join(data))
    seperator_line_elements = []
    line = [sep for sep in display_sheet[0]]
    for line_element in line:
        if "|" in line_element:
            seperator_line_elements.append("+")
        else:
            seperator_line_elements.append("-")

    seperator_line = "".join(seperator_line_elements)

    display_sheet.insert(0,seperator_line)
    display_sheet.insert(2,seperator_line)
    display_sheet.append(seperator_line)

    # print(max_wights)
    if display:
            
        for i in display_sheet:
            print(i)
    else:
        return display_sheet

# display_data(search_mechanism.results)


                






        
        

        


        


    
    

        

