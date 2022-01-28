def main():
    input_n = list(map(int, input("データを入力してください(スペース区切り) > ").split()))

    def sum():
        sum_n = 0
        for n in input_n:
            sum_n += n
        return sum_n

    def max():
        max_n = input_n[0]
        for n in input_n:
            if n > max_n:
                max_n = n
        return max_n

    def min():
        min_n = input_n[0]
        for n in input_n:
          if n < min_n:
                min_n = n
        return min_n

    def ave():
        ave = sum() // len(input_n)
        return ave

    print(f"合計値: {sum()}")
    print(f"最大値: {max()}")
    print(f"最小値: {min()}")
    print(f"平均値: {ave()}")

if __name__ == "__main__":
    main()
