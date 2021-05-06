user_number = int(input("введите число: "))

min = user_number // 60
hour = min // 60
day = hour // 24
mon = day // 30
year = mon // 12
ten_year = year // 10
hundred_year = ten_year // 10

if user_number < 60:
    print(f'{user_number} sec')

elif min < 60:
    print(f'{min} min {user_number % 60} sec')

elif hour < 60:
    print(f'{hour} hours {min % 60} min {user_number % 60} sec')

elif day < 30:
    print(f'{day} days {hour % 24} hours {min % 60} min {user_number % 60} sec')

elif mon < 12:
    print(f'{mon} mon {day % 30} days {hour % 24} hours {min % 60} min {user_number % 60} sec')

elif year < 10:
    print(f'{year} year {mon % 12} mon {day % 30} days {hour % 24} hours {min % 60} min {user_number % 60} sec')

elif ten_year < 10:
    print(f'{ten_year} decade {year % 10} year {mon % 12} mon {day % 30} days {hour % 24} hours {min % 60} min {user_number % 60} sec')

elif hundred_year < 10:
    print(f'{hundred_year} century {ten_year % 10} decade {year % 10} year {mon % 12} mon {day % 30} days {hour % 24} hours {min % 60} min {user_number % 60} sec')