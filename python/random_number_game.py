
import random
rand_num = random.randint(1, 100)
print(rand_num)
choose = int(input("숫자를 찍으시오 : "))
while(choose != rand_num):
    if(choose > rand_num):
        print("숫자가 너무 큽니다.")
    elif(choose < rand_num):
        print("숫자가 너무 작습니다.")
    choose =int(input("숫자를 다시 입력해 주세요 : "))
print("정답입니다! 정답은 {} 였습니다.".format(rand_num))
