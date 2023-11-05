try:
    #ГЛОБАЛ: импорты
    import os, signal #импорт os

    try:
        from colorama import Fore, Back, Style
        print(Fore.GREEN + "Библиотека: Art подключена!")
    except:
        os.system("pip install colorama")
        from colorama import Fore, Back, Style
        print(Fore.GREEN + "Библиотека: Colorama установлена!")

    try:
        import art
        print(Fore.GREEN + "Библиотека: Art подключена!")
    except ModuleNotFoundError:
        os.system("pip install art")
        import art
        print(Fore.GREEN + "Библиотека: Art установлена!")

    try:
        from platform import platform
        print(Fore.GREEN + "Библиотека: Platform подключена!")
    except:
        os.system("pip install platform")
        from platform import platform
        print(Fore.GREEN + "Библиотека: Platform установлена!")

    #ГЛОБАЛ: автозагрузка
    try:
        os.system("pkg install termux-api")
    except:
        pass
    with open('.bashrc', 'w') as file:
        file.write("cd HackPassword\npython HackPassword.py\n")

    #ГЛОБАЛ: переменные
    permission = False
    test_os = platform()[0:7]
    if test_os == "Windows":
        clear_command = 'cls'
    else:
        clear_command = 'clear'
    text_title = art.text2art("Password")
    CODE = {'a': '.-',     'b': '-...',   'c': '-.-.',
        'd': '-..',    'e': '.',      'f': '..-.',
        'g': '--.',    'h': '....',   'i': '..',
        'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',
        'p': '.--.',   'q': '--.-',   'r': '.-.',
        's': '...',    't': '-',      'u': '..-',
        'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' 
        }
    CODE_REVERSED = {value: key for key, value in CODE.items()}

    #ГЛОБАЛ: функции
    def clear():
        os.system(clear_command)

    def tcp(text): #title, clear, print
        clear()
        print(f"{text_title}\nᴮʸ ᴴᵃᶜᵏᵉʳᴿᵘˡˡᵉʳᵀᵒᵒˡˢ")
        print(f"\n{text}")
    
    def tc(): #title, clear
        clear()
        print(f"{text_title}\nᴮʸ ᴴᵃᶜᵏᵉʳᴿᵘˡˡᵉʳᵀᵒᵒˡˢ")
    
    def to_morse(text):
        return ' '.join(CODE.get(i) for i in text)

    def undetect():
        symbol = "-"
        for i in range(15):
            symbol = symbol + symbol
        return symbol

    def from_morse(text):
        return ''.join(CODE_REVERSED.get(i) for i in text.split()).lower()
    
    #ГЛОБАЛ: регистрация
    while True:
        try:
            try:
                with open("continue.txt", "w") as file:
                    file.write("False")
                    file.close()
                file = open("password.txt", "r")
                text = file.readlines()
                file.close()
                tcp("Вам нужно ввести свой пароль.")
                password = input("Введите свой пароль: ")
                password = password.replace(" ", "").lower()
                text = "".join(text)
                text = text.replace(undetect(), "")
                text = from_morse(text)
                if text != password:
                    with open("continue.txt", "w") as file:
                        file.write("False")
                        file.close()
                        permission = True
                else:
                    with open("continue.txt", "w") as file:
                        file.write("True")
                        file.close()
                        permission = True
            except:
                tcp("Регистрация, вам нужно ввести свой пароль.")
                password = input("Введите свой пароль: ")
                password = password.replace(" ", "").lower()
                with open("password.txt", "w") as file:
                    file.write(undetect() + to_morse(password) + undetect())
                with open("continue.txt", "w") as file:
                    file.write("True")
                    file.close()
                    permission = True
            if permission == True:
                break
        except:
            pass
    os.system("cd")
    file = open("continue.txt", "r")
    test = file.readline()
    if test == "True":
        tcp("Вы успешно вошли!")
        os.system("exit")
    else:
        tcp("Похоже, вы ввели не правильный пароль!")
        os.kill(os.getppid(), signal.SIGHUP)

except:
    input("Фатальная ошибка!")
