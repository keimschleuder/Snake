from random import randint

def randomSlogan()-> str:
    nr = randint(1, 11)
    if nr == 1:
        slogan = "FAILURE!!!!"
    elif nr == 2:
        slogan = "Your cousin did better"
    elif nr == 3:
        slogan = "The neighbours kid did better"
    elif nr == 4:
        intense = randint(1, 6)
        if intense == 1:
            slogan = "ULTRA EMOTIONAL DAMAGE!!!!"
        elif intense == 2:
            slogan = "EXTRA EMOTIONAL DAMAGE!!!!"
        elif intense == 3:
            slogan = "ULTRA EMOTIONAL DAMAGE!!!!"
        else:
            slogan = "EMOTIONAL DAMAGE!!!!"
    elif nr == 5:
        slogan = "SOCIAL ANXIETY!!!!"
    elif nr == 6:
        slogan = "I will send you to Jesus"
    elif nr == 6:
        slogan = "WHAT DA HAIL!!!!"
    elif nr == 7:
        slogan = "You've got as much talent as a celery"
    elif nr == 8:
        slogan = "STOOOPID!!!!"
    elif nr == 9:
        slogan = "Room temperature IQ"
    elif nr == 10:
        slogan = "Slight back pain"
    elif nr == 11:
        slogan = "EMOTIONAL DAMAGE!!!!"

    return slogan