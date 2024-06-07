guests = ["张三", "李四", "王五"]
print("很抱歉，新购买的餐桌无法及时送达，只能邀请两位嘉宾共进晚餐。")
while len(guests) > 2:
    sorry_guest = guests.pop()
    print(sorry_guest + "，很抱歉，无法邀请您来共进晚餐。")
for guest in guests:
    print(guest + "，您好！仍然诚挚邀请您共进晚餐。")
del guests[0:2]
print(guests)