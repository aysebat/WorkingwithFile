from pathlib import Path
from datetime import datetime

def rename_file(name="new"):
  """This takes the argument that provided and the files as an prefix"""

  root_dir =Path('files')
  file_paths = root_dir.iterdir()
  
  print(f"Current Working Directory: {Path.cwd()}")
  print("--------------------------")
  
  for path in file_paths:
    print("Current Files in the Path")
    print(path)
    new_file_name = name +'-'+ path.stem +path.suffix
    new_file_path = path.with_name(new_file_name)
    print("New File Path")
    print(new_file_path)
    path.rename(new_file_path)
    print("--------------------------")

def rename_with_folder():
  root_dir = Path('files2')
  #take all folder and files
  file_path =  root_dir.glob("**/*")
  for path in file_path:
    #check the path has file and continue
    if path.is_file():
      #take aprt the parts and takes  lates -2 as a folder name
      folder_name = path.parts[-2]
      new_file_name = folder_name +'-'+ path.name
      new_folder_name = path.with_name(new_file_name)
      path.rename(new_folder_name)

def rename_sub_sub_folder():
  """THIS FUNCTION RENAME WITH TWO SUB DIRECTORIES"""
  root_dir= Path('files3')
  #go into two sun directory
  file_path = root_dir.glob("**/**/*") 
  for path in file_path:
    #do somethig if the it is file skip the just folder
    if path.is_file():
      print(f"Existing files and path \n {path}")
      folder_names = path.parts[-3] +"-"+  path.parts[-2]
      new_file_name= folder_names+'-'+path.name
      new_folder_name = path.with_name(new_file_name)
      print(f"Renamed file path \n  {new_folder_name}")
      path.rename(new_folder_name)

def rename_file_with_date():
  """When the function run it add the todays date infront of the file"""

  root_dir =Path('files')
  file_paths = root_dir.iterdir()
  
  print(f"Current Working Directory: {Path.cwd()}")
  print("--------------------------")
  
  for path in file_paths:
    print("Current Files in the Path")
    print(path)
    now =  datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    new_file_name =  now +'-'+ path.stem +path.suffix
    new_file_path = path.with_name(new_file_name)
    print("New File Path")
    print(new_file_path)
    path.rename(new_file_path)
    print("--------------------------")


rename_file_with_date()
#rename_file(name="abat-")
#rename_with_folder()
#rename_sub_sub_folder()



  



