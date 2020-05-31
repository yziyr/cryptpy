import shutil
import time
import os
print('''

   ____________  ______  ______
  / ____/ __ \ \/ / __ \/_  __/
 / /   / /_/ /\  / /_/ / / /   
/ /___/ _, _/ / / ____/ / /    
\____/_/ |_| /_/_/     /_/     




''')
time.sleep(3)

import sys
message = ( "Данный скрипт создан в целях шифрования вашего кода python. Не работает на винде.\n tg @yziyr ")

def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

typewriter(message)

jj = os.getcwd()
time.sleep(2)
def crypt():
    g = input("\nНазвание файла(code.py).\n Файл обязательно должен быть в папке, где вы запустили скрипт: ") 
    try:
        file = open(g)
    except IOError as e:
        print(u'Не удалось найти файл. Перезапуск')
        time.sleep(1.5)
        os.system("clear")
        crypt()
    else:
        with file:
            os.system("python .1.py -i " + g + " -o 1243code.py")
            print("1 уровень шифрования готов!!!")
            os.system("python -OO -m py_compile 1243code.py")
            time.sleep(2)
            shutil.move(jj + "/__pycache__/1243code.cpython-38.opt-2.pyc", jj)
            os.rmdir("__pycache__")
            os.remove("1243code.py")
            name = input("Введите нужное название файла(file.py) : ")
            time.sleep(1)
            print("2 уровень шифрования готов!!!")
            os.rename("1243code.cpython-38.opt-2.pyc", name)
crypt()
