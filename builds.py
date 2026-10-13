from folders import *


def get_monolith(url: str, path: str, regex: str) -> str:
    '''Returns a new URL for the monolith version.'''
    folder = url  + get_build(
        get_build_number(get_folders(path), regex), 
            monolith=True)    
    from constants import MONOLITH_ENDPOINT
    folder = folder + MONOLITH_ENDPOINT
    return folder


def get_platform(url: str, path: str, regex: str) -> str:
    '''Returns a new URL for the platform version.'''
    folder = url  + get_build(
        get_build_number(get_folders(path), regex), 
            monolith=False)
    return folder


def get_developer(url: str) -> str:
    '''Returns a new URL for the developer version.'''
    from datetime import datetime
    folder = url + str(datetime.now().isoweekday())
    return folder
