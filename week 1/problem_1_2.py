if __name__ == '__main__':
    # Define special string
    s = 'bob'

    # Split string into list
    string = list(s)

    # List the starting point of 'bob' in string
    output = []
    for i in range(0, len(string)-2):
        concat = string[i] + string[i+1] + string[i+2]
        if concat == s:
            output.append(i)

    # Count number of times 'bob' occurs
    num = len(output)

    # Turn num into string to print
    num = str(num)

    # Print output
    print("Number of times bob occurs is: " + num)