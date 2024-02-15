# rjin
Make a deliverable HTML file to view tabular data from pandas in python.

## Benefits
- Super lightweight: 16kb on disk
- Make your csv data beautiful instead of an eye sore for laymen
- Don't need Excel or spreadsheet software, no apps required
- Mobile friendly data viewing as well
- Deliverable in a format everyone can open
- Dark mode by design ^_^

## Use Case

I am a programmer/data scientist and sometimes I have data I need to show a client or non-techy team member. I use `rjin` to turn my CSV data into a single HTML file that acts as a record viewer so that the person viewing only needs a browser to see the data, and the data is nicely formatted, readable, and best of all, has a nice dark style so it goes easy on the eyes. I made `rjin` have the smallest possible footprint and provide only the most base features because I'm a minimalist when it comes to UX.

Forget Excel, OpenOffice, etc. If you are just trying to show someone tons of data with tons of fields and not make their heads explode, `rjin` is for you. Send them a nice HTML formatted report they can sink their eyes into.

## How it Works

`rjin` is just a function and a template. The rjin function simply reads the template, replaces the \__TITLE__ and \__REPORT__ strings from it with the title and json formatted data fed in as the arguments.  The `default.html` template includes some HTML, CSS and Javascript which allows for the viewer to function.  The reason this works in any browser is because we are simply hard-coding our formatted data into the resulting HTML file.  This means you can send it to anyone and they will instantly understand what they are looking at, having no problem opening the file.

## Required Data

In order for the report to properly work, you need to provide one key column who's default value is `name` in your data. If your data doesn't already have a field named `name`, you can specify a different identifying field for your data like in the Pandas Example below. This key field is more for the end-viewer of this report to understand some logical identifier for each record

## Basic Example
```py
from rjin import rjin

data = [
    {'name': 'John', 'age': 35, 'profile_image': 'https://thispersondoesnotexist.com/'},
    {'name': 'Alice', 'age': 39, 'profile_image': 'https://thispersondoesnotexist.com/'},
    {'name': 'Deborah', 'age': 52, 'profile_image': 'https://thispersondoesnotexist.com/'},
    {'name': 'Yantze', 'age': 27, 'profile_image': 'https://thispersondoesnotexist.com/'},
]

rjin(data, output_path="my/output/path/report.html")
```
### Output
![Screenshot from 2024-02-15 11-44-21](https://github.com/newsbubbles/rjin/assets/1012779/48dc6233-8673-4fb1-87f0-873ead20999e)

## Example using pandas
It is important to note that rjin does not use pandas format, so each row must be converted to a `dict` in order to feed into the `rjin` function
```py
import pandas as pd
from rjin import rjin

df = pd.read_csv("vc3.csv")
data = []
for index, row in new_df.iterrows():
    rd = row.to_dict()
    # Do any pruning or other data magic here if you need to
    data.append(rd)

rjin(data, record_key="company_name") # will output to `report/report.html` if no output_path specified
```
