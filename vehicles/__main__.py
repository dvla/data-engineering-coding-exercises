import argparse
import base64 
from vehicles.model import *
from vehicles.data import *


def test(_):
    if len(list(get_countries())) > 0:
        print("OK: There is some test data. Let's go.")
    else:
        print("ERROR: There is no test data.")


def are_you_ready(_):
    with open("vehicles/.code", "r") as file:
        code = file.read()
        print(base64.b64decode(code).decode("utf-8"))


def show_imports(_):
    for country in get_countries():
        print(country)


def show_top(arguments):
    def top_three(items):
        return sorted(items, key=lambda i: i.get_registrations_count(), reverse=True)[:3]

    countries = get_brands_by_country_of_manufacturing()

    for country in countries: 
        print(country)
        for index, brand in enumerate(top_three(country._brands.values())):
            print(f"\t{index+1}: {brand}")


def show(command):
    if command == []:
        print("Incorrect syntax. \nUsage: vehicles show <what>\n")
        return
    
    {
       "imports": show_imports,
       "top": show_top
    }[command[0]](command[1:])


def _parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="*", default=["start"])
    return parser.parse_args()


def main():
    print()

    arguments = _parse_arguments()

    {
        "show": show,
        "start": are_you_ready,
        "test": test
    }[arguments.command[0]](arguments.command[1:])

    print()


main()