import os, shutil

base_dir = 'E:/videos/tv_series/family guy'

base_dst_dir = 'E:/videos/tv_series/family guy'

os.chdir(base_dir)

for f in os.listdir():
    if not os.path.isdir(f):
        season = f.split('.')[2][:3].title()
        destination = base_dst_dir+'/'+season
        shutil.move(f, destination)
    
