user_number = None

numbers =[]
for number in range(0, 22):
    numbers.append(number)

while user_number != 99:
    user_number = int(input('введите число от 0 до 20 \nИли введи 99 что бы выти: '))
    print()

    if user_number in numbers[1:2]:
        print(f'{user_number} процен\n')

    elif user_number in numbers[2:5]:
        print(f'{user_number} процента\n')

    elif user_number in numbers[5:21] or user_number in numbers[0:1]:
        print(f'{user_number} процентов\n')

    elif user_number == 99:
        break

    else:
        print('попробуй снова\n')




