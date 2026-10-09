import json


def change_bookmarks(browser, guid, url):
    with open(browser, 'r', encoding='utf-8') as file:
        data = json.load(file)
        values = data['roots']['bookmark_bar']['children']
    with open(browser, 'w', encoding='utf-8') as file:
        for value in values:
            if value.get('guid') == guid:
                value['url'] = url
                break
        json.dump(data, file, ensure_ascii=False, indent=4)
    return
