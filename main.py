phone_book = {}


# # Functions - handlers
def hello():
    print("How can I help you?")


def add_contact(name, number):
    phone_book[name] = number


def change_contact(name, number):
    phone_book[name] = number


def print_number(name):
    print(phone_book[name])


def show_all():
    if phone_book:
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    else:
        print("Phone book is empty")


def good_bye():
    print("Good bye!")


COMMANDS = {
    "add": add_contact,
    "change": change_contact,
    "phone": print_number
}

break_command = ("good bye", "close", "exit")


# Function decorator
def input_error(func):
    def inner(string):
        try:
            func(string)
        except ValueError:
            print("Enter correct number")
        except KeyError:
            print("Enter correct command")
    return inner


# Parser - function
@input_error
def parser(string):
    list_str = string.split(" ")
    handler = get_handler(list_str[0])
    handler(list_str[1].title(), int(list_str[2]))


def get_handler(command):
    return COMMANDS[command]


def main():
    while True:
        enter_text = input('Enter command:').lower()
        if enter_text == 'hello':
            hello()
        elif enter_text == 'show all':
            show_all()
        elif enter_text in break_command:
            good_bye()
            break
        else:
            parser(enter_text)


if __name__ == '__main__':
    main()
