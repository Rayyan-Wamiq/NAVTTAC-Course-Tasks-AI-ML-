import os

log = input("Enter a log message:")
with open("Diary.txt","a") as file:
    file.write(log)


if os.path.exists("Diary.txt"):
    print("Found!")

else:
    print("Not Found")