def hello(name):
    print("Hello, " + name)


def bye(name):
    print("Bye, " + name)


def say(f, roster):
    for student in roster:
        f(student)


say(hello, ["Aardvark", "Beaver", "Cheetah"])
say(bye, ["Aardvark", "Beaver", "Cheetah"])
