def main():
    k = 10  # number of spaces
    d = 20  # number of stars

    # Loop for 10 lines
    for i in range(10):
        # Loop to print spaces
        for l in range(k, 1, -1):
            print("  ", end="")  # two spaces

        # Loop to print stars
        for j in range(d):
            print("*", end="")

        print()

        k -= 1  # Decrease the number of spaces
        d += 4  # Increment the number of stars

if __name__ == "__main__":
    main()


