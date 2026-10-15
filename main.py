import argparse

import script


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chrome',  action='store_true', dest='chrome',  help='flag to change Chrome bookmarks')
    parser.add_argument('-y', '--yandex',  action='store_true', dest='yandex',  help='flag to change Yandex bookmarks')
    parser.add_argument('-o', '--opera',   action='store_true', dest='opera',   help='flag to change Opera bookmarks')
    parser.add_argument('-m', '--mozilla', action='store_true', dest='mozilla', help='flag to change Mozilla bookmarks')

    args = parser.parse_args()
    match (args.chrome, args.yandex, args.opera, args.mozilla):
        case (True, False, False, False): script.main(browser='chrome')
        case (False, True, False, False): script.main(browser='yandex')
        case (False, False, True, False): script.main(browser='opera')
        case (False, False, False, True): script.main(browser='mozilla')        
        case _:                           script.main(browser='chrome')
