if __name__ == '__main__':
    names = ["Jennifer", "Emily", "Kendra"]

    # While loop
    print("WHILE:")
    i = 0
    while True:
        name = names[i]
        print(f"\tHi {name}")
        i += 1
        if i == len(names):
            break

    # For loop
    print("FOR:")
    for name in names:
        print(f"\tHi {name}")

    # List comprehension
    print("LIST COMPREHENSION")
    [print(f"\tHi {name}") for name in names]

    # Generator
    print("GENERATOR")
    x = (print(f"\tHi {name}") for name in names)
    print("I'll print first")
    list(x)

