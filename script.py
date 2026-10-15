from constants import *
from bookmarks import *
from yaml_ import *
from builds import *
from misc import *


def main(browser):
    '''Performs the main logic of the script.'''
    print_script()
    CONSTANTS = get_constants()
    match browser:
        case 'chrome':  browser = get_browsers(CONSTANTS)[0]
        case 'yandex':  browser = get_browsers(CONSTANTS)[1]
        case 'opera':   browser = get_browsers(CONSTANTS)[2]
        case 'mozilla': browser = get_browsers(CONSTANTS)[3]
        case _:         browser = get_browsers(CONSTANTS)[0]
    bookmarks = get_bookmarks_path(CONSTANTS, browser)
    monolith  = get_monolith(QA_WEBSOFT, MONOLITH, MONOLITH_REGEX)
    platform  = get_platform(QA_WEBSOFT, PLATFORM, PLATFORM_REGEX)
    developer = get_developer(DEV_WEBSOFT)    
    for i in zip(
                (
                    get_guid(CONSTANTS, browser, build='monolith'),
                    get_guid(CONSTANTS, browser, build='platform'),
                    get_guid(CONSTANTS, browser, build='devops')
                ),
                (
                    monolith,
                    platform,
                    developer
                 )
                ):
        change_bookmarks(bookmarks, i[0], i[1])
    print(print_time(), 'Bookmarks have been changed...')
