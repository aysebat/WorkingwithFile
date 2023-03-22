from pathlib import Path

def rename_file(name="new"):
  """This takes the argument that provided and the files as an prefix"""

  root_dir =Path('files')
  file_paths = root_dir.iterdir()
  
  print(f"Current Working Directory: {Path.cwd()}")
  print("--------------------------")
  
  for path in file_paths:
    print("Current Files in the Path")
    print(path)
    new_file_name = name+ path.stem +path.suffix
    new_file_path = path.with_name(new_file_name)
    print("New File Path")
    print(new_file_path)
    path.rename(new_file_path)
    print("--------------------------")

rename_file(name="abat-")