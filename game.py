import numpy as np
number = np.random.randint(1,101) # загадываем число
count = 0

while True:
    count+=1
    predict_nimber = int(input("Угадай число от 1 до 100: "))

    if predict_nimber > number:
        print("Число должно быть меньше!")

    if predict_nimber < number:
        print("Число должно быть меньше!")
    
    else:
        print(f" Вы угадали число! Это число {number}, за  {count} попыток.")
        break