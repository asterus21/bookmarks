import requests


def check_url(link: str) -> bool:
    '''Checks whether the URL is available.'''
    global url
    try:
        url = requests.get(link)
    except:
        requests.exceptions.ConnectionError
    finally:
        if url.status_code == 200 or url.status_code == 401:
            return True
        else:
            return False
