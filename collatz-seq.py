def collatz(number):
    try:
        number = int(number)
    except:
        print('You must enter an integer')

    if number == 1:
        return 1
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1
    

num = input()
returnedVal = collatz(num)
while returnedVal != 1:
    returnedVal = collatz(returnedVal)



