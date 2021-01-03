import csv
import sys

names = []
with open("demo.csv", "r") as demo:
    reader = csv.DictReader(demo)
    for dicT in reader:
        names.append(dicT["Name"])


def add():
    global names
    with open("demo.csv", "a", newline='') as demo:
        fieldnames = ["Name", "Age", "Country", "Gender"]
        writer = csv.DictWriter(demo, fieldnames=fieldnames)
        # writer.writeheader()
        Name = input("Name: ")
        if Name in names:
            print("Exists")
            sys.exit()
        else:
            pass
        Age = input("Age: ")
        Country = input("Country: ")
        Gender = input("Gender: ")
        writer.writerow({"Name": Name, "Age": Age,
                         "Country": Country, "Gender": Gender})
        print("Done!!")


add()
