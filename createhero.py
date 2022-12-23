from random import choice, randint
import os

first_name = ("Жран", "Жмых", "Бром", "Дин", "Ван", "Грим")
last_name = ("Дикий", "Ужасный", "Яросный", "Угрюмый", "Вонючий", "Свирепый", "Старый")


def make_hero(
name=None,
hp_curret=None,
hp_max=20,
lvl=0,
xp_next=None,
xp_curret=0,
ATK_base=3,
ATK_weapon=None,
weapon=None,
defense_base=0,
defense_shield=0,
defense_armor=0,
shield=None,
armor=None,
luck=1,
inventory=None,
money=None,
mage=None,
mp_max=None,
mp_curret=None,
stamina_max=None,
stamina_curret=None
) -> list:
    if not name:
        name = choice(first_name) + " " + choice(last_name)
    if not money:
        money = randint(1, (5 + 10 * lvl))
    defense_curret = defense_base + defense_shield + defense_armor
    if not inventory:
        inventory = []
    if not xp_next:
        xp_next = 234 + 234 * (lvl * 2)
    if not hp_max:
        hp_max = 20 + 5 * lvl
    if not hp_curret:
        hp_curret = hp_max
    if not ATK_weapon and not weapon:
        ATK_weapon = 0
    ATK_curret = ATK_base + ATK_weapon
    if not mage:
        mage = choice([True, False])
    if mage == True and not mp_max:
        mp_max = 20 + 5 * lvl
    if not stamina_max:
        stamina_max = 20 + 5 * lvl
    if not mp_curret:
        mp_curret = mp_max
    if not stamina_curret:
        stamina_curret = stamina_max



    return [
        name,
        hp_max,
        hp_curret,
        lvl,
        xp_next,
        xp_curret,
        ATK_base,
        ATK_weapon,
        ATK_curret,
        weapon,
        defense_base,
        defense_shield,
        defense_armor,
        defense_curret,
        shield,
        armor,
        luck,
        inventory,
        money,
        mage,
        mp_max,
        mp_curret,
        stamina_max,
        stamina_curret
    ]

def show_hero(hero):
    name = hero[0]
    hp_max = hero[1]
    hp_curret = hero[2]
    lvl = hero[3]
    xp_next = hero[4]
    xp_curret = hero[5]
    ATK_base = hero[6]
    ATK_weapon = hero[7]
    ATK_curret = hero[8]
    weapon = hero[9]
    defense_base = hero[10]
    defense_shield = hero[11]
    defense_armor = hero[12]
    defense_curret = hero[13]
    shield = hero[14]
    armor = hero[15]
    luck = hero[16]
    inventory = hero[17]
    money = hero[18]
    mage = hero[19]
    mp_max = hero[20]
    mp_curret = hero[21]
    stamina_max = hero[22]
    stamina_curret = hero[23]

    print("Персонаж:\n")
    print(f"Имя: {name}")
    if mage == True:
        print("Имеет талант к магии")
    elif mage == False:
        print("Таланта к магии нет")
    print(f"HP: {hp_curret}/{hp_max}")
    if mage == True:
        print(f"MP: {mp_curret}/{mp_max}")
    print(f"Выносливость: {stamina_curret}/{stamina_max}")
    print(f"ATK: {ATK_curret} ({ATK_base} + {ATK_weapon})")
    print(f"Защита: {defense_curret} ({defense_base} + {defense_armor} + {defense_shield})")
    print(f"Удача: {luck}")
    print(f"XP: {xp_curret}/{xp_next}")
    print(f"Уровень: {lvl}")
    print(f"Оружие: {weapon}")
    print(f"Доспехи: {armor}")
    print(f"Щит: {shield}")
    print(f"Монеты: {money}\n")

def levelup(hero: list) -> None:
    while hero[5] >= hero[4]:
        hero[3] += 1
        for i in range(3):
            hero[4] = 234 + 234 * (hero[3])
            print(f"Поздравляем! {hero[0]} достиг {hero[3]} уровня.\n")
            print("Распределите характеристики:\n")
            print(f"1.Увеличить HP {hero[2]}/{hero[1]} + 5")
            print(f"2.Увеличить ATK {hero[6]} + 3")
            print(f"3.Увеличить Защиту {hero[10]} +")
            print(f"4.Увеличить удачу {hero[16]} + 1")
            print(f"5.Увеличть выносливость {hero[23]}/{hero[22]} + 5")
            if hero[19] == True:
                print(f"6.Увеличить ману {hero[21]}/{hero[20]} + 5")
            plus = input("Введите номер выбора и нажмите ENTER: ")
            if plus == "1":
                hero[1] += 5
                hero[2] += 5
            elif plus == "2":
                hero[6] += 3
            elif plus == "3":
                hero[10] += 2
            elif plus == "4":
                hero[16] += 1
            elif plus == "5":
                hero[22] += 5
            elif plus == "6" and hero[19]:
                hero[20] += 5
            if not hero[7]:
                hero[8] = hero[6]
            os.system("cls")
            
def buy_item(hero: list, item, price: int) -> None:
    if hero[18] >= price:
        hero[18] -= price
        hero[17].append(item)
        print(f"\n{hero[0]} купил {item} за {price} монет!")
    else:
        print(f"\n{hero[0]} не хватило {price - hero[18]} монет!\n")
    input("\nНажмите ENTER чтобы продолжить: ")

def consume_item(hero: list) -> None:
    if not hero[17]:
        print("\nИнвентарь:\n\nПустой")
    elif hero[17]:
        print("\nИнвентарь:\n")
        options = hero[17]
        show_option(hero, options)
        idx = choose_option(hero, options)
        if idx is not None:
            if idx <= len(hero[17]) - 1 and idx > -1:
                if hero[17][idx] == "Малое зелье лечения":
                    hero[17].pop(idx)
                    hero[2] += 10
                    if hero[2] > hero[1]:
                        hero[2] = hero[1]
                    print(f"\n{hero[0]} употребил {hero[17][idx]}\n")
                elif hero[17][idx] == "Малое зелье маны" and hero[20] is not None:
                    hero[17].pop(idx)
                    hero[21] += 10
                    if hero[21] > hero[20]:
                        hero[21] = hero[20]
                    print(f"\n{hero[0]} употребил {hero[17][idx]}\n")
                elif not hero[20]:
                        print("У вас нет таланта к магии чтобы употребить зелье\n")
                elif hero[17][idx] == "Малое зелье выносливости":
                    hero[17].pop(idx)
                    hero[23] += 10
                    if hero[23] > hero[22]:
                        hero[23] = hero[22]
                    print(f"\n{hero[0]} употребил {hero[17][idx]}\n")
                elif hero[17][idx] == "Кружка пива":
                    hero[17].pop(idx)
                    hero[2] += 3
                    if hero[2] > hero[1]:
                        hero[2] = hero[1]
                    hero[23] += 5
                    if hero[23] > hero[22]:
                        hero[23] = hero[22]
                    print(f"\n{hero[0]} употребил {hero[17][idx]}\n")
                elif hero[17][idx] == "Яблоко":
                    pass
                else:
                    print("Предмет нельзя употребить\n")
            else:
                print("Нет такого предмета")

def play_dice(hero: list, bet: int) -> None:
    if bet > 0:
        if hero[18] >= bet:
            hero_score = randint (2, 12)
            casino_score = randint(2, 12)
            print(f"\n{hero[0]} выбросил {hero_score}")
            print(f"Ваш противник выбросил {casino_score}\n")
            if hero_score > casino_score:
                hero[18] += bet
                print(f"{hero[0]} победил и забирает {bet} монет!\n")
            elif hero_score < casino_score:
                hero[18] -= bet
                print(f"{hero[0]} проиграл {bet} монет\n")
            else:
                print("Ничья\n")

        else:
            print(f" У {hero[0]} нет столько монет!\n")
    else:
        print("Такая ставка не возможна! Ставки начинааются от 1 монеты!")
    input("Нажмите ENTER чтобы продолжить.")

def start_fight(hero: list, enemy: list) -> None:
    text = "Выберите действие:\n"
    while hero[2] > 0 and enemy[2] > 0:
        os.system("cls")
        show_hero(hero)
        show_hero(enemy)
        print(text)
        options = [
            "Атаковать противника",
            "Использовать предмет из инвентаря"
        ]
        show_option(hero, options)
        option = choose_option(hero, options)
        if option == 0:
            combat_turn(hero, enemy)
        elif option == 1 and hero[17]:
            os.system("cls")
            print("Инвентарь:\n")
            consume_item(hero)
        elif option == 1 and not hero[17]:
            os.system("cls")
            print("\nИнвентарь пустой\n")
            input("Нажмите ENTER чтобы продолжить бой")
            return start_fight(hero, enemy)
        combat_turn(enemy, hero)
        input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)

def combat_turn(attacker: list, defender: list) -> None:
    if attacker[2] > 0:
        damage = (attacker[8] + randint(0, (attacker[3] + 1)) - defender[13])
        defender[2] -= damage
        print(f"{attacker[0]} атаковал {defender[0]} на {damage}!")

def combat_result(hero: list, enemy: list) -> None:
    os.system("cls")
    if hero[2] > 0 and enemy[2] <= 0:
        xp = 100 + 100 * enemy[3]
        print(f"{hero[0]} победил {enemy[0]} и в награду получает:")
        hero[5] += xp
        print(f"{xp} опыта")
        hero[18] += enemy[18]
        print(f"{enemy[18]} монет")
        print(f"И забирает предметы: ", end="")
        for item in enemy[17]:
            print(item, end=", ")
        hero[17] += enemy[17]
        input("Нажмите ENTER чтобы продолжить: ")
        levelup(hero)
    else:
        print("Вы умерли")

def choose_option(hero: list, options: list) -> int:
    option = input("\nВведите номер варианта и нажмите ENTER: ")
    try:
        option = int(option)
    except ValueError:
        print("\nВвод должен быть целым неотрицательным числом")
        return choose_option(hero, options)
    else: 
        if option <= len(options) - 1 and option > -1:
            return option
        else:
            print("Нет такого выбора")
            return choose_option(hero, options)

def show_option(hero:list, options: list) -> None:
    for num, option in enumerate(options):
        print(f"{num}. {option}")

def visit_hub(hero: list) -> None:
    text = f"{hero[0]} приехал в город. Чем займёте себя дальше?\n"
    options= [
        "Открыть инвентарь",
        "Зайти к алхимику",
        "Зайти в таверну",
        "Выйти за городские стены",
        "Использовать расходуваемый предмет",
        "Выйти в главное меню"    
    ]
    option = visit(hero, text, options)
    if option == 0:
        return show_inventory(hero)
    if option == 1:
        return visit_alhimist(hero)
    if option == 2:
        return visit_taverna(hero)
    elif option == 3:
        return magic_forest(hero)
    if option == 4:
        consume_item(hero)
    if option == 5:
        print("By")
    input("\nНажмите ENTER чтобы продолжить")

def visit_alhimist(hero: list) -> None:
    text = f"{hero[0]} зашёл в лавку ахимика. Здесь продаются зелья и ингридиенты.\n\nАлхимик: Прибыл прикупить зелья? Всё на витрине, выбирай:\n"
    options = [
        "Купить малое зелье лечения за 5 монет",
        "Купить малое зелье выносливости за 5 монет",
        "Купить малое зелье маны за 10 монет",
        "Купить лечебную траву за 3 монеты",
        "Выйти из лавки обратно в город"
    ]
    option = visit(hero, text, options)
    if option == 0:
        buy_item(hero, "Малое зелье лечения", 5)
        return visit_alhimist(hero)
    if option == 1:
        buy_item(hero, "Малое зелье выносливости", 5)
        return visit_alhimist(hero)
    if option == 2:
        buy_item(hero, "Малое зелье маны", 10)
        return visit_alhimist(hero)
    if option == 3:
        buy_item(hero, "Лечебная трава", 3)
        return visit_alhimist(hero)
    if option == 4:
        print(f"\n{hero[0]} вышел из лавки алхимика.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_hub(hero)

def visit_taverna(hero: list) -> None:
    text = f"{hero[0]} зашёл в таверну. Здесь можно поговорить с посетителями, сыграть в кости и арендовать комнату."
    options = [
        "Сыграть в кости",
        "Поговорить с хозяином таверны",
        "Поговорить с Эльфом за правым столиком",
        "Поговорить с незнакомцем в чёрном капишоне за столиков в углу",
        "Поговорить с рыцарями на втором этаже",
        "Поговорить с пьяным гномом за барной стойкой",
        "Поговорить с человеком за левым столиком",
        "Использовать расходуваемый предмет",
        "Выйти из таверны обратно в город"
    ]
    option = visit(hero, text, options)
    if option == 0:
        bet = int(input("Введите желаемую ставку: "))
        play_dice(hero, bet)
        return visit_taverna(hero)
    if option == 1:
        text = "Вы начали диалог с хозяином таверны:\n\nХозяин таверны: Здравствуй путник, в этой таверне ты можешь выпить или же арендовать себе комнату.\n"
        options = [
            "Купить выпивку",
            "Арендовать комнату",
            "Закончить диалог"
        ]
        option = visit(hero, text, options)
        if option == 0:
            buy_pivo(hero)
        if option == 1:
            arenda(hero)
        if option == 2:
            return visit_taverna(hero)
    if option == 2:
        print(f"\n{hero[0]} поговорил с Эльфом.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 3:
        print(f"\n{hero[0]} поговорил с незнакомцем.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 4:
        print(f"\n{hero[0]} поговорил с рыцарями")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 5:
        print(f"\n{hero[0]} поговорил с гномом.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 6:
        print(f"\n{hero[0]} поговорил с человеком.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 7:
        if not hero[17]:
            text = "Инвентарь:\n\nПусто"
        else:
            text = "Инвентарь:\n"
        options = hero[17]
        idx = visit(hero, text, options)
        if idx:
            consume_item(hero, idx)
    if option == 8:
        print(f"\n{hero[0]} вышел из таверны.")
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_hub(hero)

def buy_pivo(hero: list) -> None:
    text = "Хозяин таверны: что будете брать?\n"
    options = [
        "Купить кружку пива за 5 монет",
        "Купить медовуху за 10 монет",
        "Купить бутылку эля за 7 монет",
        "Купить бутылку вина за 10 монет",
        "Закончить диалог"
    ]
    option = visit(hero, text, options)
    if option == 0:
        buy_item(hero, "Кружка пива", 5)
        return buy_pivo(hero)
    if option == 1:
        buy_item(hero, "Медовуха", 10)
        return buy_pivo(hero)
    if option == 2:
        buy_item(hero, "Бутылка эля", 7)
        return buy_pivo(hero)
    if option == 3:
        buy_item(hero, "Бутылка вина", 10)
        return buy_pivo(hero)
    if option == 4:
        return visit_taverna(hero)

def arenda(hero: list) -> None:
    print(f"\n{hero[0]} арендовал комнату.")
    input("\nНажмите ENTER чтобы продолжить: ")
    return visit_taverna(hero)

def show_inventory(hero: list) -> None:
    os.system("cls")
    print("Инвентарь:\n")
    for num, option in enumerate(hero[17]):
        print(f"{num}.{option}")
    if not hero[17]:
        print("Пустой\n")
    else:
        print(" ")
    input("Нажмите ENTER чтобы закрыть инвентарь: ")
    return visit_hub(hero)

def magic_forest(hero:list) -> None:
    text = f"\n{hero[0]} прибыл ко входу в лес.\n"
    options = [
        "Вернуться в город",
        "Пойти в холмистые поля(lvl 0-3)",
        "Пойти в окрестности зелёного леса(lvl 2-5)"
    ]
    if hero[3] > 3:
        options.append(
            "Пойти в глубь зелёного леса(lvl 4-6)"
        )
    if hero[3] > 5:
        options.append(
            "Пойти в горы(lvl 5-8)"
        )
    if hero[3] > 7:
        options.append(
            "Пойти в горные пещеры(lvl 7-10)"
        )
    if hero[3] > 9:
        options.append(
            "Пойти в окрестности опасного магического леса(lvl 9-12)"
        )
    if hero[3] > 11:
        options.append(
            "Пойти в глубь магического леса(lvl 11-14)"
        )
    if hero[3] > 13:
        options.append(
            "Пойти в подземелье в глубине леса(lvl 13-???)"
        )
    option = visit(hero, text, options)
    if option == 0:
        return visit_hub(hero)
    elif option == 1:
        os.system("cls")
        print(f"{hero[0]} пришёл в холмистые поля\n")
        print("На вас напала слизь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        slime = make_hero(name="Слизь", hp_max=20, lvl=randint(0, 3), stamina_max=20, mage=False)
        start_fight(hero, slime)
        return magic_forest(hero)

    elif option == 2:
        os.system("cls")
        print(f"{hero[0]} зашёл в окрестности зелёного леса\n")
        print("На вас напал гоблин!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        goblin = make_hero(name="Гоблин", hp_max=35, lvl=randint(2, 5), stamina_max=35, defense_base=1, mage=False)
        start_fight(hero, goblin)
        return magic_forest(hero)
    elif option == 3 and hero[3] > 3:
        os.system("cls")
        print(f"{hero[0]} зашёл в глубь зелёного леса\n")
        print("На вас напал хоб гоблин!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        hob_goblin = make_hero(name="Хоб гоблин", hp_max=50, lvl=randint(4, 6), stamina_max=50, defense_base=3, ATK_weapon=2, mage=False)
        start_fight(hero, hob_goblin)
        return magic_forest(hero)
    elif option == 4 and hero[3] > 5:
        os.system("cls")
        print(f"{hero[0]} пришёл в горы\n")
        print("На вас напал циклоп!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        Cyclops = make_hero(name="Циклоп", hp_max=65, lvl=randint(5, 8), stamina_max=65, defense_base=5, ATK_weapon=5, mage=False)
        start_fight(hero, Cyclops)
        return magic_forest(hero)
    elif option == 5 and hero[3] > 7:
        os.system("cls")
        print(f"{hero[0]} вы зашли в пещеры\n")
        print("На вас напала гиганская летучая мышь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        bat = make_hero(name="Гиганская летучая мышь", hp_max=85, lvl=randint(7, 10), stamina_max=85, defense_base=3, ATK_weapon=10)
        start_fight(hero, bat)
        return magic_forest(hero)
    elif option == 6 and hero[3] > 9:
        os.system("cls")
        print(f"{hero[0]} зашёл в окрестности опасного магического леса\n")
        print("На вас напал лютый волк!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        wolf = make_hero(name="Лютый волк", hp_max=100, lvl=randint(9, 12), stamina_max=100, defense_base=7, ATK_weapon= 10)
        start_fight(hero, wolf)
        return magic_forest(hero)
    elif option == 7 and hero[3] > 11:
        os.system("cls")
        print(f"{hero[0]} зашёл в глубь магического леса\n")
        print("На вас напал шипастый медведь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        bear = make_hero(name="Шипастый медведь", hp_max=150, lvl=randint(11, 14), stamina_max=150, defense_base=15, ATK_weapon=20)
        start_fight(hero,bear)
        return magic_forest(hero)
    elif option == 8 and hero[3] > 13:
        os.system("cls")
        print(f"{hero[0]} зашёл в подземелье в глубине леса\n")
        print("На вас напала горгулья!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        gargoyle = make_hero(name="Каменная горгулья", hp_max=150, lvl=randint(13, 17), stamina_max=150, defense_base=20, ATK_weapon=10)
        start_fight(hero, gargoyle)
        """
        TODO: БОСС
        """
        return magic_forest(hero)

def visit(hero: list, text: str, options: list) -> None:
    os.system("cls")
    show_hero(hero)
    print(text)
    show_option(hero, options)
    option = choose_option(hero, options)
    return option
