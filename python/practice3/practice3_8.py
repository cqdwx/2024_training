# 练习 3.8：放眼世界
places = ["东京", "巴黎", "纽约", "巴厘岛", "开普敦"]

print("原始排列顺序:")
print(places)

print("\n按字母顺序排列:")
print(sorted(places))

print("\n再次打印原始排列顺序:")
print(places)

print("\n按字母相反顺序排列:")
print(sorted(places, reverse=True))

print("\n再次打印原始排列顺序:")
print(places)

places.reverse()
print("\n使用reverse()修改排列顺序:")
print(places)

places.reverse()
print("\n再次使用reverse()修改排列顺序:")
print(places)

places.sort()
print("\n使用sort()按字母顺序排列:")
print(places)

places.sort(reverse=True)
print("\n使用sort()按字母相反顺序排列:")
print(places)
