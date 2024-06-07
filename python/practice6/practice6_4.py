programming_glossary = {
    'variable': 'A named storage location in memory.',
    'function': 'A block of organized, reusable code.',
    'loop': 'A sequence of instructions that is repeated until a certain condition is reached.',
    'list': 'A data structure that holds an ordered collection of items.',
    'dictionary': 'A data structure that holds key-value pairs.'
}

for term, definition in programming_glossary.items():
    print(f"{term}: {definition}\n")

# 添加新术语
programming_glossary['module'] = 'A file containing Python code.'
programming_glossary['class'] = 'A blueprint for creating objects.'
programming_glossary['method'] = 'A function associated with an object.'
programming_glossary['exception'] = 'An error that occurs during program execution.'
programming_glossary['inheritance'] = 'The process where one class acquires the properties and behaviors of another.'

# 再次打印更新后的词汇表
for term, definition in programming_glossary.items():
    print(f"{term}: {definition}\n")
