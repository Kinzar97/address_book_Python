import pickle  # Импортируем модуль Pickle для сохранения адресной книги в файле на локальном диске


class Address_book:
    '''Класс содержит функции которые применяются к адресной книге'''

    @staticmethod
    def OpenAdd():  # Открытие адресной книги
        if Add_book == {}:
            print('\nThe address book is empty!')
        for i in Add_book:
            print(Add_book[i])

    @staticmethod
    def Add_cont():  # Добавление контакта в словарь
        na = input('\nEnter the name: ')
        s = input('Enter the surname: ')
        ph = input('Enter the phone number: ')
        add = input('Enter the additional information: ')
        Add_book[na] = Contacts(na, s, ph, add)

    @staticmethod
    def Del_cont():  # Удалеие элемента из словаря по ключу
        n = input("Who do you want to delete? (Enter the name): ")
        del Add_book[n]

    @staticmethod
    def Find_cont():  # Поиск элемента из словаря по ключу
        n = input("Who do you want to find? (Enter the name): ")
        print(Add_book.get(n, 'The name is not in the address book!'))

    @staticmethod
    def Save_Add():  # Сохранение словаря в файл
        f = open(Namefile, 'wb')
        pickle.dump(Add_book, f)
        f.close()


class Contacts:
    '''Класс Контакты
    Конструктор принимает имя, фамилию, номер телефона и дополнительную информацию о человеке'''

    def __init__(self, name, surname, ph_num, add='Empty'):
        self.name = name
        self.surname = surname
        self.ph_num = ph_num
        self.add_info = add

    def __str__(self):  # Возвращает информацию об объекте
        return str(
            'Name: {0}, Surname: {1}, The phone number: {2}, Addition information: {3}'.format(self.name, self.surname,
                                                                                               self.ph_num,
                                                                                               self.add_info))


Namefile = 'Address_book.data'
Add_book = {}
n = None

try:
    open(Namefile, 'rb')

except:
    f = open(Namefile, 'wb')
    pickle.dump(Add_book, f)  # помещаем объект в файл
    f.close()

f = open(Namefile, 'rb')
St = pickle.load(f)
f.close()
if St != None:
    Add_book = St
print("Hello!")
print("\nWelcome to the address book.")
while n != 0:
    print(
        '\nWhat do you want?'
        '\n1 - Open address book'
        '\n2 - Add contact'
        '\n3 - Change contact'
        '\n4 - Remove contact'
        '\n5 - Find contact'
        '\n0 - Exit the program\n', )
    try:
        n = int(input('Select the action: '))
    except ValueError:
        print('\nYou entered something wrong! Try again.')
        n = None
    if n == 1:
        Address_book.OpenAdd()
    elif n == 2:
        Address_book.Add_cont()
    elif n == 3:
        Address_book.Add_cont()
    elif n == 4:
        Address_book.Del_cont()
    elif n == 5:
        Address_book.Find_cont()
    elif n == 0:
        break
    else:
        if type(n) == int:
            print('\nYou entered something wrong! Try again.')

print('\nBye, Nikita!')
Address_book.Save_Add()
input('\n\nPress any key to exit...')
