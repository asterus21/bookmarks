import requests


def check_url(link: str) -> bool:
    '''Checks whether the URL is available.'''
    global url
    try:
        url = requests.get(link)
    except:
        requests.exceptions.ConnectionError
        import sys
        sys.exit(1)
    # TODO: use of 'finally' is a logical mistake here
    finally:
        # TODO: still doesn't work for the (Cancelled) status
        # TODO: of the devops version
        if url.status_code == 200 or url.status_code == 401:
            return True
        else:
            return False
