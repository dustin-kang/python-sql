import time
from random import randint

def birthday(name, age):
    for i in range(1,10):
        print('')
    space = ''
    try: 
        for i in range(1,1000):
            count = randint(1, 100)
            while(count > 0): # Just Blank
                space += ' '
                count -= 1
            if(i%10==0):
                print(space + f'{name}님의 {age}번째 생일을 축하합니다!')
            elif(i%9 == 0):
                print(space + "🎂")
            elif(i%8==0):
                print(space +"💛")
            elif(i%6==0):
                print(space + f"{name}님은 올한해 좋은일만 생길 거에요.")
            elif(i%7==0):
                print(space + "🍫")
            elif(i%6==0):
                print(space + "🎉")
            else:
                print(space + "🔸")
            space = ''
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("               ")
        time.sleep(0.2)
        print("                   dMP dMP  .aMMMb   dMMMMb   dMMMMb   dMP dMP")
        time.sleep(0.2)
        print("                  dMP dMP  dMP\"dMP  dMP.dMP  dMP.dMP  dMP.dMP")
        time.sleep(0.2)
        print("                 dMMMMMP  dMMMMMP  dMMMMP\"  dMMMMP\"   VMMMMP")
        time.sleep(0.2)
        print("                dMP dMP  dMP dMP  dMP      dMP      dA .dMP")
        time.sleep(0.2)
        print("               dMP dMP  dMP dMP  dMP      dMP       VMMMP\"")
        time.sleep(0.2)
        print("               ")
        time.sleep(0.2)
        print("      dMMMMb   dMP  dMMMMb  dMMMMMMP  dMP dMP  dMMMMb  .aMMMb   dMP dMP")
        time.sleep(0.2)
        print("     dMP\"dMP  amr  dMP.dMP    dMP    dMP dMP  dMP VMP  dMP\"dMP  dMP.dMP")
        time.sleep(0.2)
        print("    dMMMMK\"  dMP  dMMMMK\"    dMP    dMMMMMP  dMP dMP  dMMMMMP   VMMMMP")
        time.sleep(0.2)
        print("   dMP.aMF  dMP  dMP\"AMF    dMP    dMP dMP  dMP.aMP  dMP dMP  dA .dMP")
        time.sleep(0.2)
        print("  dMMMMP\"  dMP  dMP dMP    dMP    dMP dMP  dMMMMP\"  dMP dMP   VMMMP\"")
        time.sleep(0.5)
        print(f"""
                               🔥🔥
                              🔥🔥
                               /\\
                              [[]]
                           @@@[[]]@@@
                     @@@@@@@@@[[]]@@@@@@@@@
                 @@@@@@@      [[]]      @@@@@@@
             @@@@@@@@@        [[]]        @@@@@@@@@
            @@@@@@@           [[]]           @@@@@@@
            !@@@@@@@@@                    @@@@@@@@@!
            !    @@@@@@@                @@@@@@@    !
            !        @@@@@@@@@@@@@@@@@@@@@@        !
            !              @@@@@@@@@@@             !
            !             ______________           !
            !           HAPPY {age}'s BIRTHDAY        !
            !             --------------           !
            !!!!!!!                          !!!!!!!
                 !!!!!!!                !!!!!!!
                     !!!!!!!!!!!!!!!!!!!!!!!
        """)
    


name = input("이름을 입력해주세요 -> ")
age = input("올해 나이를 입력해주세요 -> ")
print("☺️  선물을 확인하셨으면 Ctrl + C 버튼을 눌러주세요.  ☺️")
time.sleep(0.5)
print("그럼 시작합니다.")
print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)
birthday(name, age)