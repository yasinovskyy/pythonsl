class Animal():
    def __init__(self, name):
        self._name = name
    
    def __str__(self):
        return self._name
    
    def __repr__(self):
        return "Animal({})".format(self._name)

names = ["Alice", "Bob", "Chuck"]

zoo = [Animal(name) for name in names]

print(zoo)
