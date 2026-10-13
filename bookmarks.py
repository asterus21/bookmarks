import json


def change_bookmarks(bookmarks: str, guid: str, url: str) -> None:
    import links
    with open(bookmarks, 'r', encoding='utf-8') as file:
        data = json.load(file)
        values = data['roots']['bookmark_bar']['children']
    with open(bookmarks, 'w', encoding='utf-8') as file:        
        for value in values:
            if value.get('guid') == guid:
                if links.check_url(url):
                    value['url'] = url
                    break
                else:
                  pass
        json.dump(data, file, ensure_ascii=False, indent=4)
    return
