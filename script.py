import re
import os

from datetime import datetime
import yaml

from constants import *
from bookmarks import *


# for the input
def get_constants():
    with open('constants.yaml', 'r') as constants:
        return yaml.safe_load(constants)


# browsers:
#   - chrome    0
#   - yandex    1
#   - opera     2
#   - mozilla   3


def get_browser(constants):
    return constants.get('browsers')


def get_bookmarks_path(constants, browser):
    return constants.get('bookmarks').get(browser)


def get_guid(constants, browser, build):
    return constants.get('guids').get(browser).get(build)


def get_folders(url) -> list:
    '''Gets a list of folders from the remote folder.'''
    try:
        folders = os.listdir(url)
        return folders
    except Exception as e:
        print(f"Unexpected error ocurred: {e}. Otherwise the VPN service is off.")


def get_build_number(folders: list, regex: str) -> list:
    '''Filters a list of folders to get only the build folders.'''
    builds = [
        re.findall(regex, build) for build in folders if build
    ]
    return(builds)


def get_build(builds: list) -> str:
    '''Gets a latest build from the list of build folders.'''
    folders = [build for build in builds if build]
    return folders[-1][-1]


def parse_build(string: str) -> str:
    '''Parses a build folder name to get a build number.'''
    build = re.findall(r'\d+\.\d+', string)[-1]
    return build.replace('.', '')



def get_url():
    monolith = QA_WEBSOFT  + get_build(
        get_build_number(
            get_folders(MONOLITH), MONOLITH_REGEX))
    platform = QA_WEBSOFT  + parse_build(get_build(
        get_build_number(
            get_folders(PLATFORM), PLATFORM_REGEX)))
    devops   = DEV_WEBSOFT + str(datetime.now().isoweekday())
    return monolith, platform, devops


def main():
    '''Performs the main logic of the script.'''
    constants = get_constants()
    browser = get_browser(constants)[0]
    bookmarks = get_bookmarks_path(constants, browser)
    for i in zip(
                (
                    get_guid(constants, browser, build='monolith'),
                    get_guid(constants, browser, build='platform'),
                    get_guid(constants, browser, build='devops')
                 ),
                (
                    get_url()[0],
                    get_url()[1],
                    get_url()[2]
                 )
                ):
        change_bookmarks(bookmarks, i[0], i[1])
