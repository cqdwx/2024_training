# 创建名为 cities 的字典
cities = {
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'The city that never sleeps.'
    },
    'London': {
        'country': 'UK',
        'population': '8.9 million',
        'fact': 'The capital city of England.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '9.3 million',
        'fact': 'The largest metropolitan area in the world.'
    }
}

# 打印每座城市的名字以及相关信息
for city, info in cities.items():
    print(f"City: {city}")
    for key, value in info.items():
        print(f"{key}: {value}")
    print()
