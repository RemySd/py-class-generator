def generate_constructor(properties: list) -> str:
    result = '    def __init__(self' + (', ' if len(properties) > 0 else '') + ', '.join(properties) + '):'
    result += '\n'

    for property in properties:
        result += '        self.' + property + ' = ' + property
        result += '\n'

    result += '\n'

    return result


def generate_get_set(properties: list) -> str:
    result = ''

    for property in properties:
        result += '    def get_' + property + '(self):'
        result += '\n'
        result += '        return self.' + property
        result += '\n'
        result += '\n'
        result += '    def set_' + property + '(self, ' + property + '):'
        result += '\n'
        result += '        self.' + property + ' = ' + property
        result += '\n'
        result += '\n'

    return result


def generate_class(name: str, properties: list) -> str:
    result = 'class ' + name.lower().capitalize() + ':'
    result += '\n'

    result += generate_constructor(properties)
    result += generate_get_set(properties)

    return result


def write_class(name: str, text: str) -> None:
    my_file = open(name.lower().capitalize() + '.py', "w")
    my_file.write(text)
    my_file.close()


className = None
while not className:
    className = str(input('class name : '))

properties = []
while True:
    propertyName = str(input('property name : '))

    if not propertyName:
        break

    properties.append(propertyName)

classText = generate_class(className, properties)
write_class(className, classText)
