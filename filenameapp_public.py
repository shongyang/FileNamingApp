import os 
 
path = input("Enter target directory, e.g. C:/DESKTOP/FOLDER: ")
wadisit = input("Input suffix, i.e. WHAT to add to file name: ")

# https://www.quora.com/How-do-I-rename-a-file-in-python
if wadisit != "":
    for filename in os.listdir(path): 
        filename_without_ext = os.path.splitext(filename)[0] 
        extension = os.path.splitext(filename)[1] 
        new_file_name = filename_without_ext+wadisit 
        new_file_name_with_ext = new_file_name+extension 
        print(new_file_name_with_ext) 
        os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext)) 
else: 
    wadisit = input("LENGTH (in characters) to remove from rear: ")
    wadisit = int("-"+wadisit)
    for filename in os.listdir(path): 
        filename_without_ext = os.path.splitext(filename)[0] 
        extension = os.path.splitext(filename)[1] 
        new_file_name = filename_without_ext[:wadisit]
        new_file_name_with_ext = new_file_name+extension 
        print(new_file_name_with_ext) 
        os.rename(os.path.join(path,filename),os.path.join(path,new_file_name_with_ext)) 
    
