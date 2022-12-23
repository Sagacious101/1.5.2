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
 ) -> dict :
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
    if not weapon:
        weapon = {
            "type": "weapon",
            "name": "Ржавый меч",
            "stat": "ATK",
            "mod": 2,
            "price": 5

        }
    if weapon:
        ATK_weapon = weapon["mod"]
    elif not weapon:
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

    return {
        "name": name,
        "hp_max": hp_max,
        "hp_curret": hp_curret,
        "lvl": lvl,
        "xp_next": xp_next,
        "xp_curret": xp_curret,
        "ATK_base": ATK_base,
        "ATK_weapon": ATK_weapon,
        "ATK_curret": ATK_curret,
        "weapon": weapon,
        "defense_base": defense_base,
        "defense_shield": defense_shield,
        "defense_armor": defense_armor,
        "defense_curret": defense_curret,
        "shield": shield,
        "armor": armor,
        "luck": luck,
        "inventory": inventory,
        "money": money,
        "mage": mage,
        "mp_max": mp_max,
        "mp_curret": mp_curret,
        "stamina_max": stamina_max,
        "stamina_curret": stamina_curret
    }

def show_hero(hero):
    print("Персонаж:\n")
    print(f'Имя: {hero["name"]}')
    if hero["mage"] == True:
        print("Имеет талант к магии")
    elif hero["mage"] == False:
        print("Таланта к магии нет")
    print(f'HP: {hero["hp_curret"]}/{hero["hp_max"]}')
    if hero["mage"] == True:
        print(f'MP: {hero["mp_curret"]}/{hero["mp_max"]}')
    print(f'Выносливость: {hero["stamina_curret"]}/{hero["stamina_max"]}')
    print(f'ATK: {hero["ATK_curret"]} ({hero["ATK_base"]} + {hero["ATK_weapon"]})')
    print(f'Защита: {hero["defense_curret"]} ({hero["defense_base"]} + {hero["defense_armor"]} + {hero["defense_shield"]})')
    print(f'Удача: {hero["luck"]}')
    print(f'XP: {hero["xp_curret"]}/{hero["xp_next"]}')
    print(f'Уровень: {hero["lvl"]}')
    show_equipped(hero)
    print(f'Монеты: {hero["money"]}\n')

def levelup(hero: dict) -> None:
    while hero["xp_curret"] >= hero["xp_next"]:
        hero["lvl"] += 1
        for i in range(3):
            hero["xp_next"] = 234 + 234 * (hero["lvl"])
            print(f'Поздравляем! {hero["name"]} достиг {hero["lvl"]} уровня.\n')
            print("Распределите характеристики:\n")
            print(f'1.Увеличить HP {hero["hp_curret"]}/{hero["hp_max"]} + 5')
            print(f'2.Увеличить ATK {hero["ATK_base"]} + 3')
            print(f'3.Увеличить Защиту {hero["defense_base"]} +')
            print(f'4.Увеличить удачу {hero["luck"]} + 1')
            print(f'5.Увеличть выносливость {hero["stamina_curret"]}/{hero["stamina_max"]} + 5')
            if hero["mage"] == True:
                print(f'6.Увеличить ману {hero["mp_curret"]}/{hero["mp_max"]} + 5')
            plus = input("Введите номер выбора и нажмите ENTER: ")
            if plus == "1":
                hero["hp_max"] += 5
                hero["hp_curret"] += 5
            elif plus == "2":
                hero["ATK_base"] += 3
            elif plus == "3":
                hero["defense_base"] += 2
            elif plus == "4":
                hero["luck"] += 1
            elif plus == "5":
                hero["stamina_max"] += 5
            elif plus == "6" and hero["mage"]:
                hero["mp_max"] += 5
            if not hero["ATK_weapon"]:
                hero["ATK_curret"] = hero["ATK_base"]
            os.system("cls")
            
def buy_item(hero: dict, item, price: int) -> None:
    if hero["money"] >= price:
        hero["money"] -= price
        hero["inventory"].append(item)
        print(f'\n{hero["name"]} купил {item} за {price} монет!')
    else:
        print(f'\n{hero["name"]} не хватило {price - hero["money"]} монет!\n')
    input("\nНажмите ENTER чтобы продолжить: ")

def consume_item(hero: dict) -> None:
    if not hero["inventory"]:
        print("\nИнвентарь:\n\nПустой")
        input("\nНажмите ENTER чтобы продолжить: ")
    elif hero["inventory"]:
        print("\nИнвентарь:\n")
        options = hero["inventory"]
        show_option(hero, options)
        idx = choose_option(hero, options)
        if idx is not None:
            if idx <= len(hero["inventory"]) - 1 and idx > -1:
                if hero["inventory"][idx] == "Малое зелье лечения":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["hp_curret"] += 10
                    if hero["hp_curret"] > hero["hp_max"]:
                        hero["hp_curret"] = hero["hp_max"]
                elif hero["inventory"][idx] == "Малое зелье маны" and hero["mp_max"] is True:
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["mp_curret"] += 10
                    if hero["mp_curret"] > hero["mp_max"]:
                        hero["mp_curret"] = hero["mp_max"]
                elif hero["inventory"][idx] == "Малое зелье маны" and not hero["mp_max"]:
                        print("У вас нет таланта к магии чтобы употребить зелье\n")
                elif hero["inventory"][idx] == "Малое зелье выносливости":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["stamina_curret"] += 10
                    if hero["stamina_curret"] > hero["stamina_max"]:
                        hero["stamina_curret"] = hero["stamina_max"]
                elif hero["inventory"][idx] == "Кружка пива":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["hp_curret"] += 3
                    if hero["hp_curret"] > hero["hp_max"]:
                        hero["hp_curret"] = hero["hp_max"]
                    hero["stamina_curret"] += 5
                    if hero["stamina_curret"] > hero["stamina_max"]:
                        hero["stamina_curret"] = hero["stamina_max"]
                elif hero["inventory"][idx] == "Медовуха":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["hp_curret"] += 3
                    if hero["hp_curret"] > hero["hp_max"]:
                        hero["hp_curret"] = hero["hp_max"]
                    hero["stamina_curret"] += 5
                    if hero["stamina_curret"] > hero["stamina_max"]:
                        hero["stamina_curret"] = hero["stamina_max"]
                elif hero["inventory"][idx] == "Бутылка эля":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["hp_curret"] += 3
                    if hero["hp_curret"] > hero["hp_max"]:
                        hero["hp_curret"] = hero["hp_max"]
                    hero["stamina_curret"] += 5
                    if hero["stamina_curret"] > hero["stamina_max"]:
                        hero["stamina_curret"] = hero["stamina_max"]
                elif hero["inventory"][idx] == "Бутылка вина":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["hp_curret"] += 3
                    if hero["hp_curret"] > hero["hp_max"]:
                        hero["hp_curret"] = hero["hp_max"]
                    hero["stamina_curret"] += 5
                    if hero["stamina_curret"] > hero["stamina_max"]:
                        hero["stamina_curret"] = hero["stamina_max"]
                elif hero["inventory"][idx] == "Яблоко":
                    print(f'\n{hero["name"]} употребил {hero["inventory"][idx]}\n')
                    hero["inventory"].pop(idx)
                    hero["hp_curret"] += 3
                    if hero["hp_curret"] > hero["hp_max"]:
                        hero["hp_curret"] = hero["hp_max"]
                    hero["stamina_curret"] += 5
                    if hero["stamina_curret"] > hero["stamina_max"]:
                        hero["stamina_curret"] = hero["stamina_max"]
                else:
                    print("Предмет нельзя употребить\n")
            else:
                print("Нет такого предмета")

def play_dice(hero: dict, bet: int) -> None:
    if bet > 0:
        if hero["money"] >= bet:
            hero_score = randint (2, 12)
            casino_score = randint(2, 12)
            print(f'\n{hero["name"]} выбросил {hero_score}')
            print(f"Ваш противник выбросил {casino_score}\n")
            if hero_score > casino_score:
                hero["money"] += bet
                print(f'{hero["name"]} победил и забирает {bet} монет!\n')
            elif hero_score < casino_score:
                hero["money"] -= bet
                print(f'{hero["name"]} проиграл {bet} монет\n')
            else:
                print("Ничья\n")

        else:
            print(f'У {hero["name"]} нет столько монет!\n')
    else:
        print("Такая ставка не возможна! Ставки начинааются от 1 монеты!")
    input("Нажмите ENTER чтобы продолжить.")

def start_fight(hero: dict, enemy: dict) -> None:
    text = "Выберите действие:\n"
    while hero["hp_curret"] > 0 and enemy["hp_curret"] > 0:
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
        elif option == 1 and hero["inventory"]:
            os.system("cls")
            print("Инвентарь:\n")
            consume_item(hero)
        elif option == 1 and not hero["inventory"]:
            os.system("cls")
            print("\nИнвентарь пустой\n")
            input("Нажмите ENTER чтобы продолжить бой")
            return start_fight(hero, enemy)
        combat_turn(enemy, hero)
        input("\nНажмите ENTER чтобы продолжить бой: ")
    combat_result(hero, enemy)

def combat_turn(attacker: dict, defender: dict) -> None:
    if attacker["hp_curret"] > 0:
        damage = (attacker["ATK_curret"] + randint(0, (attacker["lvl"] + 1)) - defender["defense_curret"])
        defender["hp_curret"] -= damage
        print(f'{attacker["name"]} атаковал {defender["name"]} на {damage}!')

def combat_result(hero: dict, enemy: dict) -> None:
    os.system("cls")
    if hero["hp_curret"] > 0 and enemy["hp_curret"] <= 0:
        xp = 100 + 100 * enemy["lvl"]
        print(f'{hero["name"]} победил {enemy["name"]} и в награду получает:')
        hero["xp_curret"] += xp
        print(f"{xp} опыта")
        hero["money"] += enemy["money"]
        print(f'{enemy["money"]} монет')
        print(f"И забирает предметы: ", end="")
        for item in enemy["inventory"]:
            print(item, end=", ")
        hero["inventory"] += enemy["inventory"]
        input("Нажмите ENTER чтобы продолжить: ")
        levelup(hero)
    else:
        print("Вы умерли")

def choose_option(hero: dict, options: list) -> int:
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

def visit_hub(hero: dict) -> None:
    hero["hp_curret"] = hero["hp_max"]
    text = f'{hero["name"]} приехал в город. Чем займёте себя дальше?\n'
    options= [
        "Открыть инвентарь",
        "Зайти к алхимику",
        "Зайти в таверну",
        "Выйти за городские стены",
        "Использовать расходуваемый предмет",
        "Выйти в главное меню",
        "Экипировать предмет"    
    ]
    option = visit(hero, text, options)
    if option == 0:
        show_items(hero["inventory"])
        input("Наэмите ENTER чтобы продолжить: ")
    elif option == 1:
        return visit_alhimist(hero)
    elif option == 2:
        return visit_taverna(hero)
    elif option == 3:
        return magic_forest(hero)
    elif option == 4:
        consume_item(hero)
    elif option == 5:
        print("By")
    elif option == 6:
        equip_item(hero)

def visit_alhimist(hero: dict) -> None:
    text = f'{hero["name"]} зашёл в лавку ахимика. Здесь продаются зелья и ингридиенты.\n\nАлхимик: Прибыл прикупить зелья? Всё на витрине, выбирай:\n'
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
        print(f'\n{hero["name"]} вышел из лавки алхимика.')
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_hub(hero)

def visit_taverna(hero: dict) -> None:
    text = f'{hero["name"]} зашёл в таверну. Здесь можно поговорить с посетителями, сыграть в кости и арендовать комнату.\n'
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
        print(f'\n{hero["name"]} поговорил с Эльфом.')
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 3:
        print(f'\n{hero["name"]} поговорил с незнакомцем.')
        input('\nНажмите ENTER чтобы продолжить: ')
        return visit_taverna(hero)
    if option == 4:
        print(f'\n{hero["name"]} поговорил с рыцарями')
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 5:
        print(f'\n{hero["name"]} поговорил с гномом.')
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 6:
        print(f'\n{hero["name"]} поговорил с человеком.')
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_taverna(hero)
    if option == 7:
        consume_item(hero)
    if option == 8:
        print(f'\n{hero["name"]} вышел из таверны.')
        input("\nНажмите ENTER чтобы продолжить: ")
        return visit_hub(hero)

def buy_pivo(hero: dict) -> None:
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

def arenda(hero: dict) -> None:
    print(f'\n{hero["name"]} арендовал комнату.')
    input("\nНажмите ENTER чтобы продолжить: ")
    return visit_taverna(hero)

def magic_forest(hero:list) -> None:
    text = f'\n{hero["name"]} прибыл ко входу в лес.\n'
    options = [
        "Вернуться в город",
        "Пойти в холмистые поля(lvl 0-3)",
        "Пойти в окрестности зелёного леса(lvl 2-5)"
    ]
    if hero["lvl"] > 3:
        options.append(
            "Пойти в глубь зелёного леса(lvl 4-6)"
        )
    if hero["lvl"] > 5:
        options.append(
            "Пойти в горы(lvl 5-8)"
        )
    if hero["lvl"] > 7:
        options.append(
            "Пойти в горные пещеры(lvl 7-10)"
        )
    if hero["lvl"] > 9:
        options.append(
            "Пойти в окрестности опасного магического леса(lvl 9-12)"
        )
    if hero["lvl"] > 11:
        options.append(
            "Пойти в глубь магического леса(lvl 11-14)"
        )
    if hero["lvl"] > 13:
        options.append(
            "Пойти в подземелье в глубине леса(lvl 13-???)"
        )
    option = visit(hero, text, options)
    if option == 0:
        return visit_hub(hero)
    elif option == 1:
        os.system("cls")
        print(f'{hero["name"]} пришёл в холмистые поля\n')
        print("На вас напала слизь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        slime = make_hero(name="Слизь", hp_max=20, lvl=randint(0, 3), stamina_max=20, mage=False, ATK_base=0)
        start_fight(hero, slime)
        return magic_forest(hero)

    elif option == 2:
        os.system("cls")
        print(f'{hero["name"]} зашёл в окрестности зелёного леса\n')
        print("На вас напал гоблин!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        goblin = make_hero(name="Гоблин", hp_max=35, lvl=randint(2, 5), stamina_max=35, defense_base=1, mage=False)
        start_fight(hero, goblin)
        return magic_forest(hero)
    elif option == 3 and hero["lvl"] > 3:
        os.system("cls")
        print(f'{hero["name"]} зашёл в глубь зелёного леса\n')
        print("На вас напал хоб гоблин!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        hob_goblin = make_hero(name="Хоб гоблин", hp_max=50, lvl=randint(4, 6), stamina_max=50, defense_base=3, ATK_weapon=2, mage=False)
        start_fight(hero, hob_goblin)
        return magic_forest(hero)
    elif option == 4 and hero["lvl"] > 5:
        os.system("cls")
        print(f'{hero["name"]} пришёл в горы\n')
        print("На вас напал циклоп!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        Cyclops = make_hero(name="Циклоп", hp_max=65, lvl=randint(5, 8), stamina_max=65, defense_base=5, ATK_weapon=5, mage=False)
        start_fight(hero, Cyclops)
        return magic_forest(hero)
    elif option == 5 and hero["lvl"] > 7:
        os.system("cls")
        print(f'{hero["name"]} вы зашли в пещеры\n')
        print("На вас напала гиганская летучая мышь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        bat = make_hero(name="Гиганская летучая мышь", hp_max=85, lvl=randint(7, 10), stamina_max=85, defense_base=3, ATK_weapon=10)
        start_fight(hero, bat)
        return magic_forest(hero)
    elif option == 6 and hero["lvl"] > 9:
        os.system("cls")
        print(f'{hero["name"]} зашёл в окрестности опасного магического леса\n')
        print("На вас напал лютый волк!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        wolf = make_hero(name="Лютый волк", hp_max=100, lvl=randint(9, 12), stamina_max=100, defense_base=7, ATK_weapon= 10)
        start_fight(hero, wolf)
        return magic_forest(hero)
    elif option == 7 and hero["lvl"] > 11:
        os.system("cls")
        print(f'{hero["name"]} зашёл в глубь магического леса\n')
        print("На вас напал шипастый медведь!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        bear = make_hero(name="Шипастый медведь", hp_max=150, lvl=randint(11, 14), stamina_max=150, defense_base=15, ATK_weapon=20)
        start_fight(hero,bear)
        return magic_forest(hero)
    elif option == 8 and hero["lvl"] > 13:
        os.system("cls")
        print(f'{hero["name"]} зашёл в подземелье в глубине леса\n')
        print("На вас напала горгулья!\n")
        input("Нажмите ENTER чтобы начать бой: ")
        gargoyle = make_hero(name="Каменная горгулья", hp_max=150, lvl=randint(13, 17), stamina_max=150, defense_base=20, ATK_weapon=10)
        start_fight(hero, gargoyle)
        """
        TODO: БОСС
        """
        return magic_forest(hero)

def visit(hero: dict, text: str, options: list) -> None:
    os.system("cls")
    show_hero(hero)
    print(text)
    show_option(hero, options)
    option = choose_option(hero, options)
    return option

def equip_item(hero: dict) -> None:
    if not hero["inventory"]:
        print("\nИнвентарь:\n\nПустой")
        input("\nНажмите ENTER чтобы продолжить: ")
    elif hero["inventory"]:
        print("\nИнвентарь:\n")
        options = hero["inventory"]
        show_option(hero, options)
        idx = choose_option(hero, options)
        if idx is not None:
            if idx <= len(hero["inventory"]) - 1 and idx > -1:
                if hero["inventory"][idx]["type"] == "weapon":
                    if hero["weapon"]:
                        hero["inventory"].append(hero["weapon"])
                        hero["weapon"] = ["inventory"][idx]
                elif not hero["inventory"][idx]["type"] == "weapon":
                    hero["weapon"] = ["inventory"][idx]
                if hero["inventory"][idx]["type"] == "shield":
                    if hero["shield"]:
                        hero["inventory"].append(hero["shield"])
                        hero["shield"] = ["inventory"][idx]
                elif hero["inventory"][idx]["type"] == "shield":
                    hero["shield"] = ["inventory"][idx]
                if hero["inventory"][idx]["type"] == "armor":
                    if hero["armor"]:
                        hero["inventory"].append(hero["armor"])
                        hero["armor"] = ["inventory"][idx]
                elif hero["inventory"][idx]["type"] == "armor":
                    hero["armor"] = ["inventory"][idx]

def show_item(item: dict) -> None:
    if item:
        if item['mod'] >= 0:
            print(f"{item['name']} +{item['mod']} {item['stat']}")
        elif item['mod'] < 0:
            print(f"{item['name']} {item['mod']} {item['stat']}")
    else:
        print("Нет")

def show_equipped(hero: dict) -> None:
    print(f"Оружие:", end=" ")
    show_item(hero["weapon"])
    print(f"Щит:", end=" ")
    show_item(hero["shield"])
    print(f"Доспехи:", end=" ")
    show_item(hero["armor"])

def show_items(items: list) -> None:
    print("Предметы: ")
    if items:
        for num, item in enumerate(items):
            print(f"{num}.", end=" ")
            show_item(item)
    else:
        print("Нет")
