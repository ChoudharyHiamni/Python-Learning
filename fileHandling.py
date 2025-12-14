# FILES ARE OF TWO TYPE:TEXT FILES AND BINARY FILES
# TEXT FILES-CONSIST OF CHARACTERS (LETTERS,NUMBERS,SYMBOLS,WHITESPACES) (.PY,.TXT,.CSV)
# BINARY FILES-CONSIST OF BYTES (IMAGE FILES,AUDIO FILES,VIDEO FILES) (.JPG,.PNG,.MP3,.MP4)


# f=open("sample.txt","r")
# data=f.read()
# print(data)


                           #READING A FILE AND SEARCHING FOR A WORD
# f=open("sample.txt","r")
# data=f.read()
# if "them" in data:
#     print("Found")
# else:
#     print("Not found")

                             #CHECKING IF FILE NOT EXIST THEN WHAT HAPPEN THAT TIME-IT WILL GIVE ERROR 
# f=open("abc.txt","r")
# data=f.read()
# print(data)
  

#IN WRITE MODE IF WE OPEN A FILE WHICH IS NOT EXIST THEN IT WILL CREATE A NEW FILE
# f=open("sample.txt","w")
# f.write("Python is an interesting Language")


#IN APPEND MODE IF WE OPEN A FILE WHICH IS NOT EXIST THEN IT WILL CREATE A NEW FILE

# f=open("sample.txt","a")
# f.write("\nI love to code in Python")
# f.close()


# f=open("sample.txt","x")       ##IF FILE IS NOT EXIST THEN IT WILL CREATE A NEW FILE,IF FILE IS ALREADY EXIST THEN IT WILL GIVE ERROR


#READ ENTIRE FILE
# with open("sample.txt","r") as f:   #AUTO CLOSE THE FILE AFTER WORK IS DONE
#     data=f.read()
#     print(data)

#READ LINE BY LINE
# with open("sample.txt","r") as f:
#     for line in f:
#         print(line)

# with open("sample.txt","r") as f:
#     lines=f.readlines()   #READ ALL LINES AND STORE IN LIST
#     print(lines)

#TO READ FIRST LINE
# with open("sample.txt","r") as f:
#     first_line=f.readline()
#     print(first_line)

#printt HOW MANY LINES ARE THERE IN A FILE
# with open("sample.txt","r") as f:
#     lines=f.readlines()
#     print("Number of lines:",len(lines))


# import os
# os.remove("sample.txt")   #TO DELETE A FILE
# os.rename("sample.txt","newfile.txt")  #TO RENAME A FILE
# os.path.exists("newfile.txt")  #TO CHECK A FILE IS EXIST OR NOT


import shutil
# shutil.copy("newfile.txt","copyfile.txt")  #TO COPY A FILE
# shutil.move("copyfile.txt","movedfile.txt")  #TO MOVE A FILE
# shutil.rmtree("foldername")   #TO DELETE A FOLDER AND ALL ITS CONTENTS
# os.mkdir("foldername")   #TO CREATE A FOLDER

