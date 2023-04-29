import csv


members_88R_d = []

members_88R_r = []

with open("88R members party.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    header = False
    header_indexes = {}

    for row in reader:
        if header is False:
            header = True

            for i, header_label in enumerate(row):
                header_indexes[header_label] = i

        else:
            print(row)

            if row[1] == "D":
                members_88R_d.append(row[0].replace(" ", ""))
            else:
                members_88R_r.append(row[0].replace(" ", ""))

print("DEMS:", members_88R_d)

print("REPS:", members_88R_r)