# FILE HANDLING
file = open("./WEEK 4/ASSIGNMENT/names.pdf", "w")
file.write("Michelle, Margaret\n")


with open("./WEEK 4/ASSIGNMENT/names.pdf", 'r') as file:
    content = file.read()

modify = content.replace("Michelle", "Nana")

with open("./WEEK 4/ASSIGNMENT/names.pdf", 'w') as file:
    file.write(modify)

# ERROR HANDLING
try:
    file = input("Enter the file name: ")
    with open(file, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("The file does not exist. Please check the file path.")
except IOError:
    print("File cannot be read. Please try again.")        