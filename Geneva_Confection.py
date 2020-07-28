# -----------------  Geneva Confection  ----------------------

# Get number of tests from user
def getTests():
    while True:
        try:
            number_of_tests = int(input('Enter number of tests (1-10): '))
            if number_of_tests <= 0:
               print('Number must be higher than 0')
               continue
            if number_of_tests not in range(1, 11):
               print('Number must be between 1 and 10')
               continue
        except ValueError:
            print("Please enter numbers only")
            continue
        else:
            return number_of_tests
            break


# Get number of carts from user
def getNumberCarts(tests):
    for number in range(tests):
        while True:
            try:
                carts = int(input(f'Select a number of carts for test {number + 1}: '))
                if carts <= 1:
                    print('Number must be higher than 1')
                    continue
            except ValueError:
                print("Please enter numbers only")
                continue
            else:
                return carts
                break


# Get content of carts from user
def getContentsCarts(number_of_tests, number_of_carts):
    mountain = []
    for tests in range(number_of_tests):
        cart_contents = []
        for content in range(number_of_carts):
            while True:
                try:
                    cart_num = int(input(f'(Test {tests + 1}) Select a number for cart {content + 1}: '))
                    if cart_num <= 0:
                        print('Number must be higher than 0')
                        continue
                    if cart_num not in range(1, number_of_carts + 1):
                        print('Number is out of range')
                        continue
                    if cart_num in cart_contents:
                        print(f'{cart_num} has already been chosen')
                        continue
                except ValueError:
                    print("Please enter numbers only")
                    continue
                else:
                    cart_contents.append(cart_num)
                    break
        mountain.append(cart_contents)
    return mountain


# Check to see if carts can make it to lake using the branch
def checkMountain(mountain):
    branch = []
    for group in range(len(mountain)):
        current = 1
        successful = True
        while branch != [] or mountain[group] != []:
            if branch != []:
                if branch[-1] == current:
                    branch.pop(-1)
                    current += 1
                elif mountain[group][-1] == current:
                    mountain[group].pop(-1)
                    current += 1
                else:
                    successful = False
                    branch.clear()
                    mountain[group].clear()
                    break
            elif mountain[group][-1] == current:
                mountain[group].pop(-1)
                current += 1
            else:
                branch.append(mountain[group][-1])
                mountain[group].pop(-1)
        if successful == True:
            print('Yes')
        else:
            print('No')


# Main loop
def mainLoop():
    number_of_tests = getTests()
    number_of_carts = getNumberCarts(number_of_tests)
    cart_start_num = number_of_carts
    mountain = getContentsCarts(number_of_tests, number_of_carts)
    checkMountain(mountain)
    
    
# Check to see if user wants to try again
if __name__ == '__main__':
    while True:
        mainLoop()
        while True:
            answer = input('Play again? (Y/N): ')
            if answer.upper() in ('Y', 'N'):
                break
            print('\nInvalid input\n')
        if answer.upper() == 'Y':
            continue
        else:
            print('\nThanks for playing')
            break




