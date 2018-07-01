


while True:
    dan = int(input("구구단 몇 단을 계산할까요?(1~9) "))
    if(dan>9 or dan<0):
        print("잘못 입력하셨습니다. 1부터 9 사이 숫자를 입력해 주세요")
        continue
    if(dan==0):
        print("구구단 게임을 종료합니다.")
        break
    else:
        print("구구단 ", dan, "단을 게산합니다.")
        i=1
        while i < 10:
            print(dan, " X ", i, " = ", dan*i);
            i+=1
