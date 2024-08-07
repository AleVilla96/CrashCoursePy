glossary = {
    'class': 'A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that '
             'the created objects will have.',
    'object': 'An object is an instance of a class. It is a self-contained entity that consists of both data ('
              'attributes) and behavior (methods).',
    'dictionary': 'A dictionary in Python is a collection of key-value pairs. It is an unordered, mutable data type '
                  'that allows you to store and retrieve values using unique keys.',
    'loop': 'Loops in Python are used to repeatedly execute a block of code. The main types of loops are for loops '
            'and while loops.',
    'variable': 'Variables in Python are used to store data values. They are named references to a memory location '
                'where the data is stored, and their values can be changed during program execution.',
}

for k, v in glossary.items():
    print(f"{k.title()}: {v.capitalize()}")
