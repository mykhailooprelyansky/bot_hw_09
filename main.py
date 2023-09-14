phone_book = {}


# Function decorator
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except TypeError:
            return "Error: insufficient data entered"
        except ValueError:
            return "Enter correct number"
        except KeyError:
            return "Name is not found"
        except NameError:
            return "Name already exists, enter other name"
    return inner


# # Functions - handlers
@input_error
def add_number(name, number):
    if name in phone_book:
        raise NameError
    else:
        phone_book[name] = int(number)
        return f"New contact {name}: {number}"


@input_error
def change_number(name, number):
    if name not in phone_book:
        raise KeyError
    else:
        phone_book[name] = number
        return f"Number of contact {name} changed on {number}"


@input_error
def show_contact_number(name):
    if name in phone_book:
        return f"{name.title()}: {phone_book[name]}"
    else:
        raise KeyError


def show_all_phone_book():
    if phone_book:
        for name, number in phone_book.items():
            return f"{name}: {number}"
    else:
        return "Phone book is empty"


# Dictionary of command
HANDLERS_WITH_PAR = {
    "add": add_number,
    "change": change_number,
    "phone": show_contact_number,
    "hello": lambda: "How can I help you?",
    "good bye": lambda: "Good bye!",
    "close": lambda: "Good bye!",
    "exit": lambda: "Good bye!"
}


def get_handler(func):
    def inner(*args):
        if args:
            result = func(*args)
            return result
        else:
            result = func()
            return result
    return inner


def main():
    while True:
        enter_text = input('Enter command:').lower().split(" ", maxsplit=2)
        first_itm = enter_text[0]
        if first_itm == "show":
            print(show_all_phone_book())
        if first_itm in HANDLERS_WITH_PAR:
            handler = get_handler(HANDLERS_WITH_PAR[first_itm])
            result = handler(*enter_text[1:])
            print(result)
            if result == "Good bye!":
                break


if __name__ == '__main__':
    main()
