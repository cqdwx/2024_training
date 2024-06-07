def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending message:", current_message)
        sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "Good morning!"]
sent_messages = []
send_messages(messages[:], sent_messages)  # 传递消息列表的副本

print("\nSent Messages:")
for message in sent_messages:
    print(message)

print("\nOriginal Messages:")
for message in messages:
    print(message)
