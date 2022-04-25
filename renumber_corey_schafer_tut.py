import os

file_dir = 'e:/academic_resources/coe/tutorials/youtube_singles/Python_Tutorial_Corey_Schafer/'
os.chdir(file_dir)

numbers = set()
for f in os.listdir():
    if not os.path.isdir(f):
        fname, fext = os.path.splitext(f)
        fnum, *name, youtube = fname.split()
        fnum = int(fnum)
        if fnum in numbers:
            fnum = max(numbers) + 1
            name = str(fnum ).zfill(3) +' ' + ' '.join(name).strip(' -') + fext
            os.rename(f, name)
        else:
            name = str(fnum ).zfill(3) +' ' + ' '.join(name).strip(' -') + fext
            os.rename(f, name)

        numbers.add(int(fnum))