import os
import re


def get_folders(url: str) -> list:
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
    return builds


def get_build(builds: list, monolith=False) -> str:
    '''Gets a latest build from the list of build folders.'''
    folders = [build for build in builds if build]
    folder = folders[-1][-1]
    if monolith:
        return folder
    else:
        return re.findall(r'\d+\.\d+', folder)[-1].replace('.', '')
