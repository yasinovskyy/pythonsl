filename = "files.in"

roster = []

with open(filename, "r") as input_file:
    input_file.readline()  # skip the first line
    for line in input_file:
        roster.append(line.strip())
print(roster)
print(sorted(roster, reverse=True))
