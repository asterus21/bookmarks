import re
import os

from datetime import datetime

from constants import *
from bookmarks import *


def get_folders(url) -> list:
    '''Gets a list of folders from the remote folder.'''
    try:
        folders = os.listdir(url)
        return folders
    except Exception as e:
        print(f"Unexpected error ocurred: {e}. Otherwise the VPN services is off.")


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
    '''Parsers a build folder name to get a build number.'''
    build = re.findall(r'\d+\.\d+', string)[-1]
    return build.replace('.', '')


def make_paths():
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
    ID = MONOLITH_GUID, QA_GUID, DEV_GUID
    for i in zip(ID, make_paths()):
        change_bookmarks(CHROME, i[0], i[1])
