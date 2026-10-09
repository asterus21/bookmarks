import json

# TODO: check for the URL to be available
# TODO: via requests.get() to return 200
def change_bookmarks(bookmarks, guid, url):
    with open(bookmarks, 'r', encoding='utf-8') as file:
        data = json.load(file)
        values = data['roots']['bookmark_bar']['children']
    with open(bookmarks, 'w', encoding='utf-8') as file:
        for value in values:
            if value.get('guid') == guid:
                value['url'] = url
                break
        json.dump(data, file, ensure_ascii=False, indent=4)
    return
