from pathlib import Path
from datetime import datetime
import zipfile


def rename_file(name="new"):
  """This takes the argument that provided and the files as an prefix"""

  root_dir = Path('files')
  file_paths = root_dir.iterdir()

  print(f"Current Working Directory: {Path.cwd()}")
  print("--------------------------")

  for path in file_paths:
    print("Current Files in the Path")
    print(path)
    new_file_name = name + '-' + path.stem + path.suffix
    new_file_path = path.with_name(new_file_name)
    print("New File Path")
    print(new_file_path)
    path.rename(new_file_path)
    print("--------------------------")


def rename_with_folder():
  root_dir = Path('files2')
  #take all folder and files
  file_path = root_dir.glob("**/*")
  for path in file_path:
    #check the path has file and continue
    if path.is_file():
      #take aprt the parts and takes  lates -2 as a folder name
      folder_name = path.parts[-2]
      new_file_name = folder_name + '-' + path.name
      new_folder_name = path.with_name(new_file_name)
      path.rename(new_folder_name)


def rename_sub_sub_folder():
  """THIS FUNCTION RENAME WITH TWO SUB DIRECTORIES"""
  root_dir = Path('files3')
  #go into two sun directory
  file_path = root_dir.glob("**/**/*")
  for path in file_path:
    #do somethig if the it is file skip the just folder
    if path.is_file():
      print(f"Existing files and path \n {path}")
      folder_names = path.parts[-3] + "-" + path.parts[-2]
      new_file_name = folder_names + '-' + path.name
      new_folder_name = path.with_name(new_file_name)
      print(f"Renamed file path \n  {new_folder_name}")
      path.rename(new_folder_name)


def rename_file_with_date():
  """When the function run it add the todays date infront of the file"""

  root_dir = Path('files')
  file_paths = root_dir.iterdir()

  print(f"Current Working Directory: {Path.cwd()}")
  print("--------------------------")

  for path in file_paths:
    print("Current Files in the Path")
    print(path)
    now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    new_file_name = now + '-' + path.stem + path.suffix
    new_file_path = path.with_name(new_file_name)
    print("New File Path")
    print(new_file_path)
    path.rename(new_file_path)
    print("--------------------------")


def convert_timestamp_to_time(given_time):
  """Takes the timesamp argument and convert the time as following
  string format %Y-%m-%d-%H:%M:%S """
  return datetime.fromtimestamp(given_time).strftime("%Y-%m-%d-%H:%M:%S")


def rename_folder_with_created_datetime():
  root_dir = Path('files2')
  #take all folder and files
  file_path = root_dir.glob("**/*")
  for path in file_path:
    #check the path has file and continue
    if path.is_file():
      created_time = path.stat().st_ctime
      date_created_str = convert_timestamp_to_time(created_time)
      new_file_name = date_created_str + '-' + path.name
      new_folder_name = path.with_name(new_file_name)
      path.rename(new_folder_name)


def rename_the_suffix_of_file(suffix="csv"):
  root_dir = Path('files4')
  file_path = root_dir.iterdir()
  for path in file_path:
    new_file_name = path.parts[1].split(".")[0] + "." + suffix
    new_folder_name = path.with_name(new_file_name)
    path.rename(new_folder_name)


def change_the_suffix(cur_suffix, new_suffix):
  root_dir = Path('files4')
  #rglob searh for all sub folder
  for path in root_dir.rglob(f"*{cur_suffix}"):
    if path.is_file():
      name_with_new_suffix = path.with_suffix(new_suffix)
      path.rename(name_with_new_suffix)


def create_empty_files():
  """Create a empty txt files ranging from 10 to 20 and named with the same number"""
  root_dir = Path('files5')

  #loop over from 10 to the 20
  for i in range(10, 21):
    file_name = str(i) + '.txt'
    file_path = root_dir / Path(file_name)
    file_path.touch()


def create_zip_files(unlink=True):
  """Create a zip files in the folder with all the txt files
  if unlink=True, this will delete all the files in the folder
  if unlink=Flse, this will keep all files and create the zip file.
  """
  root_dir = Path('files5')
  archive_path = root_dir / Path("archive2.zip")

  with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.glob("*.txt"):
      zf.write(path)
      #if unlink is True this delete all txt files
      if unlink:
        path.unlink()


def unzip_file():
  root_dir = Path('files5')
  unzip_dir = Path('unzip')

  for path in root_dir.glob("*.zip"):

    #print(f"Path: {path}")
    final_path = root_dir / unzip_dir / Path(path.stem)
    print(final_path)
    with zipfile.ZipFile(path, 'r') as zf:
      print(zf)
      print(f"Path.stem: {Path(path.stem)}")
      zf.extractall(path=final_path)


#unzip_file()

#create_zip_files()

#create_empty_files()
#change_the_suffix(".txt",".csv")
#rename_the_suffix_of_file("csv")
#rename_file_with_date()
#rename_file(name="abat-")
#rename_with_folder()
#rename_sub_sub_folder()
#rename_folder_with_created_datetime()
