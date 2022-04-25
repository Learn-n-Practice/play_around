import os

base_path = 'E:/videos/tv_series/family guy/S17'

# os.chdir('E:\\videos\\tv_series\\family guy\\S17')
os.chdir(base_path) # Changes the directory to the path specified

os.getcwd() # returns the path of the current working directory

for f in os.listdir():
    f_name, f_ext = os.path.splitext(f)
    family, guy, snef, guy_2, sep, speed, quality, web, psa = f_name.split('.')
    new_name = f'{family.strip()}.{guy.strip()}.{sep.strip()}.{quality.strip()}{f_ext.strip()}'
    os.rename(f, new_name)
