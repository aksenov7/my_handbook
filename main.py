import os
DEFAULT_HAND_BOOK = None
def create_handbook():
    while True:
        name = input("Введите название справочника\n")
        if name in [f.split('.')[0] for f in os.listdir() if f.endswith(".hb")]:
            print(f"Справочник с именем {name} уже существует!")
            print(f"Прервать создание справочника?")
            answer = input("y/n?\n")
            if answer == "y":
                break
            else:
                continue
        else:
            with open(f"{name}.hb", "w") as file:
                file.write("Фамилия\tИмя\tГород\tТелефон\tПочта")
            break

def view_handbook():
    global DEFAULT_HAND_BOOK
    if DEFAULT_HAND_BOOK is not None:
        with open(DEFAULT_HAND_BOOK, "r") as file:
            for line in file.readlines():
                print(line)
        return
    else:
        search = search_exist_hb()
    if search == -1:
        print("У вас нет справочников для просмотра!")
        return
    if DEFAULT_HAND_BOOK is None:
        print("Справочник не выбран!")
        return

def create_record():
    global DEFAULT_HAND_BOOK
    contact = {"Фамилия": None, "Имя": None, "Город": None, "Телефон": None,"Почта": None}
    if DEFAULT_HAND_BOOK is not None:
        with open(DEFAULT_HAND_BOOK, "a") as file:
            for key in contact.keys():
                while True:
                    contact[key] = input(f"Введеите '{key}'") + "\t"
                    if len(contact[key]) < 3:
                        print("Вы не ввели {key}! Введите пожалуйста")
                        continue
                    break
            contact = "".join([val for val in contact.values()])
            file.write(contact.strip('\t'))
        return
    else:
        search = search_exist_hb()
    if search == -1:
        print("У вас нет справочников для просмотра!")
        return
    if DEFAULT_HAND_BOOK is None:
        print("Справочник не выбран!")
        return

def search_record():
    pass

def delete_record():
    pass

def change_record():
    pass

def delete_handbook():
    global DEFAULT_HAND_BOOK
    if DEFAULT_HAND_BOOK is not None:
        print("Удалить справочник используемый по умолчанию?")
        answer =input("y/n\n")
        if answer == "y":
            os.remove(DEFAULT_HAND_BOOK)
            print(f"Справочник '{DEFAULT_HAND_BOOK}' успешно удален!")
            DEFAULT_HAND_BOOK = None
            return

    while True:
        name = input("Введите название справочника\n")
        if name not in [f.split(".")[0] for f in os.listdir() if f.endswith(".hb")]:
            print(f"Справочника с именем {name} не обнаружено!")
            print(f"Прервать удаление справочника?")
            answer = input("y/n?\n")
            if answer == "y":
                break
            else:
                continue
        for f in [f for f in os.listdir() if f.endswith(".hb")]:
            if name == f.split(".")[0]:
                os.remove(f)
                break
        break
def your_choice():
    while True:
        choice = input("""Выберите одну из операций:
    1: создать новый справочник
    2: просмотр всего справочника
    3: создать новую запись
    4: найтити запись
    5: удалить запись
    6: изменить запись
    7: удалить справочник
    8: выйти из программы\n""")
        choice = int(choice)
        if choice not in range(1, 9):
            print("Операции, которую вы ввели не существует!\nПопробуйте еще раз.")
        else:
            return choice

def search_exist_hb():
    global DEFAULT_HAND_BOOK
    exist_hb = []
    for f in os.listdir():
        if f.endswith(".hb"):
            exist_hb.append(f)
    if not exist_hb:
        return -1
    else:
        print("У вас уже существуют справочники:")
        for i, hb in enumerate(exist_hb, 1):
            print(i, hb)
        print("Хотите установить какой-то из них для работы по умолчанию?")
        answer = input("Если да, то введите порядковый номер книжки в списке выше. Иначе, введите 0:\n")
        try:
            answer = int(answer)
        except:
            return
        if answer in range(1, len(exist_hb)+1):
            DEFAULT_HAND_BOOK = exist_hb[answer - 1]
            return
        else:
            return

def menu():
    print("Прииветствую вас!")
    search_exist_hb()
    while True:
        choice = your_choice()
        if choice == 8:
            return
        func_menu = {1: create_handbook, 2: view_handbook,
                     3: create_record, 4: search_record,
                     5: delete_record, 6: change_record,
                     7: delete_handbook,}
        choice_func = func_menu[choice]
        choice_func()

if __name__ == '__main__':
    menu()
