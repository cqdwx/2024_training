import random

# 创建一个包含10个数字和5个字母的列表
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# 从列表中随机选择4个数或字母
winning_numbers = random.sample(lottery_pool, 4)
print("If your lottery ticket contains these 4 numbers/letters, you've won the jackpot:", winning_numbers)
