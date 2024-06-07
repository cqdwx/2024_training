foods = {
    'fruits': ['apple', 'banana', 'orange'],
    'vegetables': ['carrot', 'lettuce', 'broccoli'],
    'meats': ['chicken', 'beef', 'pork']
}

for category, items in foods.items():
    print(f"\n{category.title()}:")
    for item in items:
        print(item)