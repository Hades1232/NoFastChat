import keyboard
import json
import threading

with open("time.json", 'rt', encoding='UTF8') as f:
    
    data = json.load(f)

if int(data["time"]) == 0:
    print("단타 방지 프로그램에서 0초를 하는건 너무한 거 아닌가요?")
    input()
    exit()

elif int(data["time"]) < 3:
    print("적어도 3초는.. ㅎ..")
    input()
    exit()

def main(test):
    keyboardOff() 
    

def keyboardOn():
    keyboard.unhook_all()
    keyboard.on_press_key('enter', main)
    

def keyboardOff():
    keyboard.block_key('enter')


keyboardOff()


def my_func():
    print('단타 방지가 실행중입니다!')
    keyboardOn()
    threading.Timer(data["time"], my_func).start()  


my_func()
input()
      


