# check_db.py
# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")
# db = client['polytest']

# # for m in db.markets.find().limit(5):
# #     print(m)


# # count entriesn in documents
# print(db.markets.count_documents({}))

import pandas as pd
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['polytest']
markets_col = db['markets']

df = pd.DataFrame(list(markets_col.find()))
# df.head()
# print(df.head())

# count all rows id's
df['_id'].count()
print("Rows:", df['_id'].count())

# inside markets collection show liquidity and volume
# df[['liquidity', 'volume']].head()
# print(df[['liquidity', 'volume']].head())

# count all rows that endDate inside "events"
# Count rows where events contain an 'endDate' key
count = df['events'].apply(lambda ev: any('endDate' in e for e in ev) if isinstance(ev, list) else False).sum()
print("Count end dates:", count)

from datetime import datetime

# Target date
target_date = "2025-12-17"

# Flatten and filter events
end_dates = []
for events in df['events']:
    if isinstance(events, list):
        for e in events:
            if 'endDate' in e and e['endDate'] is not None:
                # Compare date portion only
                if e['endDate'].startswith(target_date):
                    end_dates.append(e['endDate'])
# print(end_dates)
# count end_dates
count = len(end_dates)
print("Total Dates:", target_date, count)


# display "title" of the target_date on limit 5 rows
# Filter rows where any event has endDate starting with target_date
mask = df['events'].apply(
    lambda ev: any(e.get('endDate', '').startswith(target_date) for e in ev) 
    if isinstance(ev, list) else False
)

# Extract titles from matching events
titles = [
    e.get('title')
    for events in df['events'] if isinstance(events, list)
    for e in events if e.get('endDate', '').startswith(target_date)
]
# for events in df[mask]['events']:
#     if isinstance(events, list):
#         for e in events:
#             if e.get('endDate', '').startswith(target_date):
#                 titles.append(e.get('title'))

# Show first 5 titles
print(titles[:5], target_date)
