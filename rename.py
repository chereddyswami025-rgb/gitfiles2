import os
folder="E:\\hp\\Documents\\rename"#here // is used becase if we / it will consider as escape sequences
for file in  os.listdir(folder):
    old_path=os.path.join(folder,file)
    new_fname="new_"+file
    new_path=os.path.join(folder,new_fname)
    os.rename(old_path,new_path)
print("files renamed with prefix")