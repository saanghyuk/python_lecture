
dan = int(input("몇 단을 계산할까요? "))
print("구구단 ", dan, "단을 계산합니다.")
for i in range(1, 10):
    print("{0} X {1} = {2}".format(dan, i, dan*i))
