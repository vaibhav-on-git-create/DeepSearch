import tkinter
from tkinter import filedialog
from search_mechanism import pre_search_file
from display_data import display_data

def select_path():
    root = tkinter.Tk(screenName="select folder or drive to serach in")
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select folder or drive")
    return folder_path
    
def safe_input(statement : str , datatype = str):
    while True:
        try:
            data = datatype(input(statement))
            return data

        except TypeError:
            print(f" >> [The input must be : '{datatype}']")
        



def select_path():
    """Folder selection dialog"""
    root = tkinter.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select folder")
    root.destroy()
    return folder if folder else None

def safe_input(statement, datatype=str):
    """Safe input with error handling"""
    while True:
        try:
            return datatype(input(statement))
        except ValueError:
            print("Invalid input, try again")


while True:
    print(display_data(sheet_data=[["Welcome User"],["INITIALIZING..."]], max_wight_limit=60))
    print(">> Write '404' to exit program...")
    input(">> Select folder to continue futher...\npress enter")
    folder_path = select_path()
    if not folder_path:
        print("No folder selected, try again")
        continue
        
    print(f">> Selected folder path : [{folder_path}]")
    
    user_1 = input(">> Enter your search key word : ")
    
    if "404" in user_1:
        break
        
    user_2 = input(">> do you want to confirm the path(Y/N) : ")
    
    if "y" in user_2.lower():
        user_3 = safe_input(statement=">> maximum number of match you want : ", datatype=int)
        print('>> searching...')
        
        result = pre_search_file(
            parent_dir=folder_path, 
            search_key_word=user_1, 
            top_results=user_3, 
            max_row_wigth=40, 
            display=False
        )
        
        display_data(sheet_data=result[0])
        
        user_ch = safe_input(statement="Enter the serial number you want to access : ", datatype=int)
        
        if 0 < user_ch <= len(result[1]):
            selected_path = result[1][user_ch][-1]  # Fixed index (1-based)
            print(f">> your file path for key word : {user_1} -- [{selected_path}]")
            
            user_4 = input(" >> Do you want to continue ? (Y/N) : ")
            if "y" not in user_4.lower():
                break
        else:
            print("Invalid serial number!")
    else:
        print("Path not confirmed, try again")

print("Goodbye!")



    

            
            






