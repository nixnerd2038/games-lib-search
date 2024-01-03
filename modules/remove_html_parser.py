from html2text import html2text

def remove_html(data):
    for k, v in data.items():
        if isinstance(v, bool) or isinstance(v, int):
            data[k] = v
        elif isinstance(v, str):
            try:
                data[k] = html2text(v.replace('\n', ''))
            except KeyError as err:
                print(f"Error processing data: Key error on {k}")
        elif isinstance(v, list):
            data[k] = [remove_html(x) for x in v if isinstance(x, dict)]
        elif isinstance(v, dict):
            remove_html(v)
        else:
            data[k] = v
    return data