import shutil
import os

##Function to move a file from Source to Destination using shutil library (shutil.move) with exeption handeled
def move_file(source_path, destination_path):
    """
    Moves a file from the source path to the destination path.

    Args:
        source_path (str): The path to the file you want to move.
        destination_path (str): The path to the destination folder.
    """

    try:
        shutil.move(source_path, destination_path) 
        print(f"File moved from '{source_path}' to '{destination_path}'")
    except FileNotFoundError:
        print(f"Error: File not found at '{source_path}'")
    except Exception as e:
        print(f"Error moving file: {e}")

#It will move and arrange all the files from the directory given into the
#new directory named Organized and will make seperate folders for each file type
directory = 'unorganizedFolder'
for filename in os.listdir(directory):           ##It will Itterate one by one on each file in the dictory given
    f = os.path.join(directory, filename)        ##It combines the directory and filename into a single path in a way that is compatible with the operating system
    
    # checking if it is a file
    if os.path.isfile(f):
        filetype = f.split(".")[-1]              ##Seperated the file path string into parts of list and take the first index( eg: hello.txt will be seperated in [hello,txt] so filetype = txt)
        source_path = f                         ##the path of file from unorganized folder will one by on
        destination_path = f"organized\{filetype}"
        os.makedirs(destination_path,exist_ok=True)
        
    
    move_file(source_path,destination_path)



#Explanation of Line 26
# directory = "organized"
# filename = "file.txt"
# f = os.path.join(directory, filename)
# print(f)
# # Output: organized\file.txt
