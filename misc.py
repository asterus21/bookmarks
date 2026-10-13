import sys

import datetime


# TODO: use the __str__ overload
def print_time() -> str:
    '''Prints the current time.'''
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def script_start_button():
    '''Accepts the user's input.'''
    user_input = input('Press Enter to continue (type exit to quit): ')
    print()
    if user_input in ('exit', 'Exit', 'EXIT', 'учше', 'УЧШЕ'):
        print(print_time(), 'The program is about to close...')
        print()
        sys.exit(0)
    else:
        pass


def print_script():
    print(f'{print_time()}', 'Note that the VPN serice must be turned on...')
    print(f'{print_time()}', 'Make sure that the browser is closed...\n')
    script_start_button()
