from suma import add
from resta import subs
from multiplicacion import mult
from division import div
from potenciacion import potrncia
from modulo import modulo



def game():
    score = 0
    while True:
        print('======== Menu ========'
            '\n1. Add'
            '\n2. substraction'
            '\n3. multiplication'
            '\n4. divition'
            '\n5. potenciation'
            '\n6. module'
            '\n0. Exit')
        option = int(input('\nChoice an option: '))
        if option == 0:
            break

        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter you answer: '))

        if option == 1:
            result = add(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')

            else:
                print('Incorrect')

        if option == 2:
            result = subs(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')

            else:
                print('Incorrect')
                
        if option == 3:
            result = mult(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')

            else:
                print('Incorrect')

        if option == 4:
            result = div(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')

            else:
                print('Incorrect')
        
        if option == 5:
            result = potrncia(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')

            else:
                print('Incorrect')

        if option == 6:
            result = modulo(num_1, num_2)
            if result == answer:
                score += 1
                print('Correct!!')

            else:
                print('Incorrect')

    print(f'======== Game Over ========'
            f'\nYou score is {score}'
            '\nKeep going!')
    
game()