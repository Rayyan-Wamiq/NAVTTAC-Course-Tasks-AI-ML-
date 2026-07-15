with open("Diary.txt","w") as file:
    file.write("I am Rayyan Wamiq!\n")
    file.write("I am a Software Engineer\n")
    file.write("I am 21 years old")
    

with open("Diary.txt","r") as file:
    content = file.read()
    print(content)


with open("Diary.txt", "r") as file:
    lines = file.readlines()
print(len(lines))