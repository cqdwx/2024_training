things = ["珠穆朗玛峰", "尼罗河", "巴西", "东京", "Python编程语言"]

print("原始列表:")
print(things)

print("\n按字母顺序排列:")
print(sorted(things))

print("\n再次打印原始排列顺序:")
print(things)

print("\n按字母相反顺序排列:")
print(sorted(things, reverse=True))

print("\n再次打印原始排列顺序:")
print(things)

things.reverse()
print("\n使用reverse()修改排列顺序:")
print(things)

things.reverse()
print("\n再次使用reverse()修改排列顺序:")
print(things)

things.sort()
print("\n使用sort()按字母顺序排列:")
print(things)

things.sort(reverse=True)
print("\n使用sort()按字母相反顺序排列:")
print(things)