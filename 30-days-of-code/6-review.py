



count = int(input())
for y in range(count):
    string = input()
    first_string = ''
    second_string = ''
    for i in range(len(string)):    
        if i == 0:
            first_string += string[i]
        else:
            if i%2 == 0:
                first_string += string[i]
            else:
                second_string += string[i]    
    print(first_string, second_string)
