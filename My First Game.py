import random
import time

list_pril = ["Обычного", "Эпического", "Легендарного", "Ужасного", "Гиганского", "Чудного"] # прилагательные
list_mons = ["Орка", "Гоблина", "Тролля", "Скелета", "Зомби", "Вампира"]  # монстры

health_player = 100
gold = 0
attack = 5
i = 0
z = 0
gold2 = 0


def function_print(print_str):
    for i in range(len(print_str)):
        print(print_str[i], end="")
        time.sleep(0.15)
    print(end=' ')

function_print('''Приветствую странник!\nТы находишься в "сумеречном лесу".\nДанный лес находится во владениях страшных и жутких монстров, 
они могут появится где угодно и когда угодно, так что будь осторожен,также в лесу ты можешь найти золото, тебе нужно иметь ровно 100 золота и подбросить его вверх ,
 чтобы благополучно покинуть это опасное место.
 При убийстве монстра , есть шанс найти у него то самое золото,
 также золото можно найти в сундуке , который спрятан в лесу.
 Будь бдителен и удачи, странник!''')

while gold < 100 and health_player > 0:
    random_var = random.randint(1, 10)
    if random_var == 1 or random_var == 2 or random_var == 3: # встреча с монстром
        random_var_mons1 = random.randint(0, len(list_pril)-1) # эти диапозоны нужно менять при добавлении новых прилагательных (3 и 4 строчка) (- 1 потому что не включительно)
        random_var_mons2 = random.randint(0, len(list_mons)-1) # эти диапозоны нужно менять при добавлении новых прилагательных (3 и 4 строчка) (- 1 потому что не включительно)
        function_print("\n\nВы встретили") # функция с 11 - 15 строчку, (данная функция нужна для поочередного вывода текста)
        function_print(list_pril[random_var_mons1])
        function_print(list_mons[random_var_mons2])
        choise = input(""".\nВаши действия?Введите
        1 - Убежать от монстра
        2 - Сражаться с монстром
                      """)
        if choise == "1":     # побег от монстра
            var_on_ran = random.randint(1, 2)
            if var_on_ran == 1:
                print("У вас получилось сбежать")
            elif var_on_ran == 2:
                health_player -= 5
                function_print(f"Вы сбежали , но монстр успел вас ударить, здоровье - 5.\nВаше текущее здоровье = {health_player}")
        elif choise == "2": # битва с монстром
            health_monst = 15 # это значение нужно менять
            while health_monst > 0: # бой с монстром
                choise_on_fight = input("""Введите
                1 - Атака
                2 - Защита + лечение
                3 - Побег""")
                if choise_on_fight == "1":
                    health_monst -= attack
                    function_print(f"Вы атаковали монстра, нанесенный урон = {attack}.\nТекущее здоровье монстра = {health_monst}")  # f - форматирование
                    health_player -= 10
                    function_print(f"\nМонстр успел атаковать вас, здоровье - 10.\nВаше текущее здоровье = {health_player }")
                if health_monst <= 0:
                    gold2 += random.randint(0, 3)
                    if gold2 == 2 or 0 :
                        gold += random.randint(1, 7)
                        function_print(f"\nМонстр был убит, вы сорвали ниточку с шеи чудовища , на ней были золотые монеты.\nВаше текущее золото = {gold}")
                        function_print("\nВы пошли дальше ")
                    elif gold2 == 1 or 3 :
                        function_print(f"\nМонстр был убит, но золота при нем не было обнаружено")
                        function_print("\nВы пошли дальше ")
                elif choise_on_fight == "2":
                    health_player += 10
                    print(f"Вы восстановили здоровье,здоровье + 10.\nВаше текущее здоровье{health_player}")
                elif choise_on_fight == "3":
                    gold -= 10
                    print(f"\nВы убежали в глубь леса, золото - 10.\nВаше текущее золото = {gold}")
                    break
    if random_var == 4 or random_var == 5:
        function_print("\nВы нашли золото и пошли дальше исследовать лес ")
        gold += random.randint(7, 10)  # здесь регулировка золота
        function_print("\nВаше текущее золото " + str(gold) + '\n')
    if random_var == 7 or random_var == 8:
        while i < 1:
            function_print("\n\nВы наткнулись на закрытый сундук сокровищ, но позади вас монстр.\nВаши действия?")
            сhoise1 = input("""Введите
            1 - Попробовать открыть сундук
            2 - Бежать """)
            if сhoise1 == "1":
                i += 1
                open_chest = random.randint(0, 1)
                if open_chest == 1:
                    i += 1
                    gold += 25
                    print(f"Взлом сундука удался, золото + 25.\nВаше текущее золото = {gold} ")
                    function_print("Вы пошли дальше ")
                elif open_chest == 0:
                    health_player -= 10
                    print(f"Взлом сундука не удался, монстр ударил вас и вы обратились в бегство, здоровье - 10.\nВаше текущее здоровье = {health_player}")
            if сhoise1 == "2":
                function_print("Вы решили не рисковать и побежали дальше ")
                break
    if random_var == 9 or random_var == 10:
        while z < 1:
            function_print("\n\nВы нашли изогнутый меч , от которого исходит неведомая сила.\nВаши действия?")
            choise2 = input("""Введите
            1 - Взять меч
            2 - Не брать меч и пойти дальше""")
            if choise2 == "1":
                z += 1
                health_player -= 50
                print(f"Меч не признал вас , вы ранены , здоровье - 50.\nВаше текущее здоровье = {health_player}")
                function_print("\nВы пошли дальше")
            elif choise2 == "2":
                z += 1
                attack += 30
                function_print(f"Меч был в шоке от вашей наглости и передал свою силу вам, урон + 30.\nВаш текущий урон = {attack}")
                function_print("\nВы пошли дальше ")
    if health_player <= 0:
        print("\n\nВЫ ПОГИБЛИ, ИГРА ОКОНЧЕНА")
    elif gold > 100:
        function_print("""КОЛИЧЕСТВО ВАШИХ МОНЕТ БОЛЬШЕ 100 , 
        ВЫ ПОДБРОСИЛИ ВСЕ МОНЕТЫ ВВЕРХ И ОЧУТИЛИСЬ НА СВЕТЛОЙ СОЛНЕЧНОЙ ПОЛЯНЕ,
        ВОКРУГ ВАС БЫЛО ПОЛНО РАЗНООБРАЗНЫХ КУСТАРНИКОВ ПОЛНЫХ ЯГОД,
        ВЫ БЫЛИ РАДЫ ,ЧТО ВЕСЬ ЭТОТ КОШМАР ЗАКОНЧИЛСЯ И ПРЫГНУЛИ ПРЯМО В КУСТЫ ЗА ВКУСНЫМИ ЯГОДАМИ! 
        ПОЗДРАВЛЯЮ!ВЫ ПРОШЛИ ИГРУ""")
        break