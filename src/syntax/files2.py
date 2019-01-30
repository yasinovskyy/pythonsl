filename = "files.in"

with open(filename, "r") as input_file:
    roster = input_file.read().split("\n")[1:-1]
print(roster)
print(sorted(roster, reverse=True))
