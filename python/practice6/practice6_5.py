rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# 打印每条河流及其流经的国家
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 打印每条河流的名字
print("\nRiver Names:")
for river in rivers.keys():
    print(river.title())

# 打印每个国家的名字
print("\nCountry Names:")
for country in rivers.values():
    print(country.title())
