import random

monster_counter = 0
hp = random.randint(10, 999)
attack = random.randint(10, 999)


def game():
    while monster_counter < 10:
        move = random.randint(0, 2)
        if move == 1:
            apple()
        elif move == 2:
            sword()
        else:
            monster()
    print('ПОБЕДА!')


def apple():
    global hp
    apple_hp = random.randint(10, 999)
    hp += apple_hp
    print(f'РЫЦАРЬ СЪЕЛ ЯБЛОКО-КОЛИЧЕСТВО ЖИЗНЕЙ УВЕЛИЧЕНО НА {apple_hp}, У РЫЦАРЯ {hp} жизней')


def sword():
    global attack
    sword_attack = random.randint(10, 999)
    while True:
        user_answer = input(f'ТЫ НАШЕЛ МЕЧ. СИЛА АТАКИ {sword_attack}, 1 - ЗАБРАТЬ МЕЧ, 2 - ПРОЙТИ МИМО')
        if user_answer == '1':
            attack = sword_attack
            break
        elif user_answer == '2':
            break
        else:
            print('НЕПРАВИЛЬНЫЙ ВВОД-КРИВЫЕ РУЧОНКИ')


def monster():
    global hp
    global monster_counter
    monster_hp = random.randint(10, 999)
    monster_attack = random.randint(10, 999)
    while True:
        user_answer = input(f'БОЙ У МОНСТРА {monster_hp} ЗДОРОВЬЯ И {monster_attack} АТАКИ. 1 - АТАКОВАТЬ, 2 - СБЕЖАТЬ')
        if user_answer == '1':
            monster_hp -= attack
            hp -= monster_attack
            if hp < 1:
                print("ПОРАЖЕНИЕ")
                return
            elif monster_hp < 1:
                monster_counter += 1
                return
        elif user_answer == '2':
            break
        else:
            print('НЕПРАВИЛЬНЫЙ ВВОД-КРИВЫЕ РУЧОНКИ')


game()