import os, shutil
from pathlib import Path

# Set the base directory
base_dir = 'E:/videos/tv_series/rick and morty'

# Change the current directory to the base directory
os.chdir(base_dir)

# print(Path(os.getcwd()).parent)
# print(os.path.dirname(os.getcwd()))

visited = list()
for f in os.listdir():
    if os.path.isdir(f) and f not in visited:
        # Set the directory to the subdirectory
        new_dir = os.path.join(base_dir, f)
        
        # Switch working directory to the new subdirectory
        os.chdir(new_dir)

        # Move the items to the parent diirectory
        for i in os.listdir():
           shutil.move(i, os.path.dirname(new_dir))
      
        # Switch back to the parent directory   
        os.chdir(os.path.dirname(new_dir))
        
           
for f in os.listdir():
    if not os.path.isdir(f):
        season = f.split('.')[3][:3]
        if not os.path.exists(season):
            os.mkdir(season)
        destination = base_dir+'/'+season
        shutil.move(f, destination)
        
            
        
