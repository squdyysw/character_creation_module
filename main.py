from random import randint


def attack(char_name, char_class):
    attack = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return (f'{char_name} {attack} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {attack} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {attack} {5 + randint(-3, -1)}')
    return ''


def defence(char_name, char_class):
    block = 'блокировал'
    if char_class == 'warrior':
        return (f'{char_name} {block} {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} {block} {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} {block} {10 + randint(2, 5)} урона')
    return ''


def special(char_name, char_class):
    abillity_cast = 'применил специальное умение'
    if char_class == 'warrior':
        return (f'{char_name} {abillity_cast} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {abillity_cast} «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {abillity_cast} «Защита {10 + 30}»')
    return ''


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack', end=' ')
    print('— чтобы атаковать противника,', end=' ')
    print('defence — чтобы блокировать атаку ', end='')
    print('противника или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    approve_choice = None
    char_class = None
    enter = 'Введи название персонажа, за которого хочешь играть'
    classes = 'Воитель — warrior, Маг — mage, Лекарь — healer:'
    while approve_choice != 'y':
        char_class = input(f'{enter}: {classes} ')
        warrior_patterns = 'Сильный, выносливый и отважный.'
        mage_patterns = 'Обладает высоким интеллектом.'
        healer_patterns = 'Черпает силы из природы, веры и духов.'
        if char_class == 'warrior':
            print(f'Воитель — дерзкий воин ближнего боя. {warrior_patterns}')
        if char_class == 'mage':
            print(f'Маг — находчивый воин дальнего боя. {mage_patterns}')
        if char_class == 'healer':
            print(f'Лекарь — могущественный заклинатель. {healer_patterns}')
        instr = 'Нажми (Y), чтобы подтвердить выбор, или '
        uction = 'любую другую кнопку, чтобы выбрать другого персонажа '
        approve_choice = input(f'{instr}, {uction}').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))

    main()
