#ГЛОБАЛ: импорты

import os, signal

try:
    from platform import platform
except:
    os.system("pip install platform")
    from platform import platform

try:
    import art
except ModuleNotFoundError:
    os.system("pip install art")
    import art

#ГЛОБАЛ: переменные
text_title = art.text2art("Password")
test_os = platform()[0:7]
if test_os == "Windows":
    clear_command = 'cls'
else:
    clear_command = 'clear'

#ГЛОБАЛ: функции
def tc(): #title, clear
    os.system(clear_command)
    print(f"{text_title}\nᴮʸ ᴴᵃᶜᵏᵉʳᴿᵘˡˡᵉʳᵀᵒᵒˡˢ")

#ГЛОБАЛ: тест на выход

tc()
file = open("continue.txt", "r")
test = file.readline()
if test == "True":
    tc()
    os.system("exit")
else:
    tc()
    os.kill(os.getppid(), signal.SIGHUP)