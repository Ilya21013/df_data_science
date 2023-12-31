import numpy as np

def random_predict(number: int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Default to 1

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        
        count+=1
        predict_number=np.random.randint(1,101) # предполагаемое число

        if number == predict_number:
            break #вых из цикла если угадали

    return(count)

print(f'Количество __ попыток: {random_predict()}')