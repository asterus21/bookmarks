import yaml


# for the input
def get_constants():
    with open('constants.yaml', 'r') as constants:
        return yaml.safe_load(constants)


def get_browser(constants):
    return constants.get('browsers')


def get_bookmarks_path(constants, browser):
    return constants.get('bookmarks').get(browser)


def get_guid(constants, browser, build):
    return constants.get('guids').get(browser).get(build)
