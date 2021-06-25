import os
os.system("date")

#os.mkdir(r"/Users/dhanunjaikumar/Desktop/KarrthikWhiteHat/C99/Anything")
print(os.getcwd())
path="/Users/dhanunjaikumar/Desktop/KarrthikWhiteHat/C99/main.py"
isExist=os.path.exists(path)
print(isExist)

root_ext=os.path.splitext(path)
print("root part :-",root_ext[0])
print("ext part :- ",root_ext[1])

print(os.listdir())

import shutil
source="/Users/dhanunjaikumar/Desktop/KarrthikWhiteHat/C99/abc.txt"
dest="/Users/dhanunjaikumar/Desktop/KarrthikWhiteHat/C99/abc1.txt"
destination=shutil.copy(source,dest)