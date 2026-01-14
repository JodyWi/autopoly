import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client['polytest']
markets_col = db['markets']

# Load into DataFrame
df = pd.DataFrame(list(markets_col.find()))
print(df.head())
print(df.info())

# (.venv) (base) PS C:\Users\jodyk\Projects\polytest> python load_markets.py
#                         _id      id  acceptingOrders acceptingOrdersTimestamp  active  approved  archived  automaticallyActive  ...  volume1moAmm  volume1wkAmm  volume1yrAmm volume24hrAmm  volumeAmm  automaticallyResolved closedTime umaEndDate
# 0  69402b82bf880c3c22e9f5b9  679162             True     2025-11-13T00:25:54Z    True      True     False                 True  ...           NaN           NaN           NaN           NaN        NaN                    NaN        NaN        NaN
# 1  69402b82bf880c3c22e9f5ba  678779             True     2025-11-13T16:18:24Z    True      True     False                 True  ...           NaN           NaN           NaN           NaN        NaN                    NaN        NaN        NaN
# 2  69402b82bf880c3c22e9f5bb  936264             True     2025-12-14T20:47:29Z    True      True     False                 True  ...           NaN           NaN           NaN           NaN        NaN                    NaN        NaN        NaN
# 3  69402b82bf880c3c22e9f5bc  540208             True     2025-05-01T17:45:22Z    True      True     False                 True  ...           NaN           NaN           NaN           NaN        NaN                    NaN        NaN        NaN
# 4  69402b82bf880c3c22e9f5bd  679257             True     2025-11-13T19:11:24Z    True      True     False                 True  ...           NaN           NaN           NaN           NaN        NaN                    NaN        NaN        NaN

# [5 rows x 105 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 7288 entries, 0 to 7287
# Columns: 105 entries, _id to umaEndDate
# dtypes: bool(23), float64(33), int64(2), object(47)
# memory usage: 4.7+ MB
# None
# (.venv) (base) PS C:\Users\jodyk\Projects\polytest> 