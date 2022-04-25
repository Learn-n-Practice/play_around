import os

f_path = 'E:/videos/tv_series/family guy/S16'


os.chdir(f_path)

for f in os.listdir():
    family, guy, sep, *rem, ext =(f.split('.'))
    new_name = f'{family.strip()}.{guy.strip()}.{sep.strip()}.720p.{ext.strip()}'
    os.rename(f, new_name)
