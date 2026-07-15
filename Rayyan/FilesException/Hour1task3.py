with open("Diary.txt","a") as file:
    file.write("I study in Sir Syed University of Engineering\n")
    file.write("I am currently in 6th Semester")

with open("Diary.txt","r") as file:
    content = file.read()
    print(content)