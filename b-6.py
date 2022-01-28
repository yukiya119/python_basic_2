def main():

    import random

    dice_men = int(input("サイコロの面の数は?: "))
    dice_count = int(input("何回振りますか?: "))

    def dice():
        if dice_men >= 1 and dice_count >= 1:
            dice_trial = [random.randint(1, dice_men) for d in range(1, dice_count + 1)]
            return dice_trial
        else:
            raise ValueError("正の整数(1以上)を入力してください")

    print(dice())

if __name__ == "__main__":
    main()
