import os
print(__file__)
abspath=os.path.abspath(__file__)
print(abspath)
dir_path=os.path.dirname(abspath)
print(dir_path)
file_path=dir_path+"\sample.html"
print(file_path)
print(os.path.join(dir_path,"sample.html"))
