import yaml


# TODO: make it a Class to initialize the constants object
# TODO: and call methods to get a needed field
def get_constants():
    with open('constants.yaml', 'r') as constants:
        return yaml.safe_load(constants)


def get_browsers(constants) -> str:
    return constants.get('browsers')


def get_bookmarks_path(constants, browser):
    return constants.get('bookmarks').get(browser)


def get_guid(constants, browser, build):
    return constants.get('guids').get(browser).get(build)
