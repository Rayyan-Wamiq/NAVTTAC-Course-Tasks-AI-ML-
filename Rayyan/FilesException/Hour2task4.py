import os
with open("Diary.txt","r") as file:
    content = file.read()
    print(content)


if os.path.exists("Diary.txt"):
    print("Found!")

else:
    print("Not Found")