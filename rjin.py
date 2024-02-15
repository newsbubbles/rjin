# Free to use, do whatever you want with it
# coded with love by @newsbubbles

import json
from typing import Any

def rjin(data:list[dict[str, Any]], title:str="Record Viewer", template:str="default", order_descending:bool=False, output_path:str="report/report.html", record_key:str="name"):
    """rjin summary

    Args:
        data (list[dict[str, Any]]): The data to build the report with, a list of flat dicts
        title (str, optional): Report Title. Defaults to "Record Viewer".
        template (str, optional): The template to use. Defaults to "default".
        order_descending (bool, optional): If you want to order latest records first. Defaults to False.
        output_path (str, optional): Where to put the resulting html file. Defaults to "report/report.html".
        record_key (str, optional): The key data field that will identify each record on the left. Defaults to "name".
    """

    json_formatted = json.dumps(data if not order_descending else data[::-1])
        
    with open(f'template/{template}.html', 'r') as f:
        html = f.read()
    html = html.replace('__REPLACE__', json_formatted) \
        .replace('__TITLE__', title) \
        .replace('__KEY__', record_key)

    with open(output_path, 'w+') as f:
        f.write(html)


if __name__ == "__main__":
    # Example Report
    data = [
        {'name': 'John', 'age': 35, 'profile_image': 'https://thispersondoesnotexist.com/'},
        {'name': 'Alice', 'age': 39, 'profile_image': 'https://thispersondoesnotexist.com/'},
        {'name': 'Deborah', 'age': 52, 'profile_image': 'https://thispersondoesnotexist.com/'},
        {'name': 'Yantze', 'age': 27, 'profile_image': 'https://thispersondoesnotexist.com/'},
    ]
    rjin(data, title="Example Report", output_path="report/example.html")
    import webbrowser
    webbrowser.open("report/example.html")