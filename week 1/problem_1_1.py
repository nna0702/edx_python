if __name__ == '__main__':
    # Create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Define string
    s = 'renuoghfcgij'

    # Separate characters of s into a list
    string = list(s)

    # List the vowels in string
    output = []
    for i in range(0, len(string)):
        if string[i] in vowels:
            output.append(string[i])
    print(output)

    # Number of vowels in the s
    num = len(output)

    # Turn num into a string to print
    num = str(num)

    # Print output
    print("Number of vowels: " + num)