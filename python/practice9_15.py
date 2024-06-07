import random

# 创建一个包含10个数字和5个字母的列表
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 创建一个名为my_ticket的列表，代表彩票持有人的号码
my_ticket = ['A', 5, 9, 3]

# 循环直到中了大奖才结束
attempts = 0
while True:
    attempts += 1
    chosen_numbers = random.sample(lottery_pool, 4)
    if chosen_numbers == my_ticket:
        print("It took", attempts, "attempts to win the jackpot!")
        break
