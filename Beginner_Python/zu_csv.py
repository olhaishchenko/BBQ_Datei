import csv

my_dict = {"test": 1, "testing": 2}

with open("mycsvfile.csv", "w", newline="") as f:
    w = csv.DictWriter(f, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)