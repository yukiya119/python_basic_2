number1 = int(input("行数を入力してください："))
number2 = int(input("列数を入力してください："))

for cnt1 in range(1, number1 + 1):
    for cnt2 in range(1, number2 + 1):
        print(cnt1 * cnt2, end=' ')

    print('\n', end='') #取り敢えず完成
