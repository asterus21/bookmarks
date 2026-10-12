from bookmarks import *
from builds import *
from browser import *
from constants import *


def main():
    '''Performs the main logic of the script.'''
    constants        = get_constants()
    chrome           = get_browser(constants)[0]
    # yandex         = get_browser(constants)[1]
    # opera          = get_browser(constants)[2]
    # mozilla        = get_browser(constants)[3]
    bookmarks_chrome = get_bookmarks_path(constants, chrome)
    monolith         = get_monolith(QA_WEBSOFT, MONOLITH, MONOLITH_REGEX)
    platform         = get_platform(QA_WEBSOFT, PLATFORM, PLATFORM_REGEX)
    developer        = get_developer(DEV_WEBSOFT)
    for i in zip(
                (
                    get_guid(constants, chrome, build='monolith'),
                    get_guid(constants, chrome, build='platform'),
                    get_guid(constants, chrome, build='devops')
                ),
                (
                    monolith,
                    platform,
                    developer
                 )
                ):
        change_bookmarks(bookmarks_chrome, i[0], i[1])
