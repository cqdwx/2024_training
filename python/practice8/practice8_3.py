def make_shirt(size, message):
    print(f"制作一件尺码为{size}的T恤，上面印有'{message}'的字样。")

# 使用位置实参调用函数
make_shirt("L", "Hello, World!")
# 使用关键字实参调用函数
make_shirt(size="M", message="Python Rocks!")
