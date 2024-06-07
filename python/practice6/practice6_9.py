# 创建一个名为 favorite_places 的字典
favorite_places = {
    'Alice': ['beach', 'mountains', 'Paris'],
    'Bob': ['New York', 'Tokyo', 'London'],
    'Charlie': ['Rome', 'Sydney', 'countryside']
}

# 遍历字典，并将其中每个人的名字及其喜欢的地方打印出来
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}")
