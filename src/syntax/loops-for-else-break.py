roster = ["Aardvark", "Beaver", "Cheetah"]
target = "Dolphin"

for animal in roster:
    if animal == target:
        break
else:
    print(target + " not found")
