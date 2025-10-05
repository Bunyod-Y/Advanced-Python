import csv
name=input("Name: ")
number=input("Number: ")
with open("/home/bunyodyokubov/PROJECTS/Advanced_Python/Advanced-Python/Chapter 1 - Python review/phonebook.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "number"])
        writer.writerow({"name":name, "number":number})

    

    

