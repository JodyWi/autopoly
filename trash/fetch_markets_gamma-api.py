import requests

url = "https://gamma-api.polymarket.com/markets"

params = {
    "limit": 50,
    "active": True
}

r = requests.get(url, params=params, timeout=10)
r.raise_for_status()

markets = r.json()
print(len(markets))
print(markets[0].keys())
# (.venv) (base) PS C:\Users\jodyk\Projects\polytest> python fetch_markets.py
# 50
# dict_keys(['id', 'question', 'conditionId', 'slug', 'twitterCardImage', 'endDate', 'category', 'liquidity', 'image', 'icon', 'description', 'outcomes', 'outcomePrices', 'volume', 'active', 'marketType', 'closed', 'marketMakerAddress', 'updatedBy', 'createdAt', 'updatedAt', 'closedTime', 'mailchimpTag', 'archived', 'restricted', 'volumeNum', 'liquidityNum', 'endDateIso', 'hasReviewedDates', 'readyForCron', 'volume24hr', 'volume1wk', 'volume1mo', 'volume1yr', 'clobTokenIds', 'fpmmLive', 'volume1wkAmm', 'volume1moAmm', 'volume1yrAmm', 'volume1wkClob', 'volume1moClob', 'volume1yrClob', 'events', 'creator', 'ready', 'funded', 'cyom', 'competitive', 'pagerDutyNotificationEnabled', 'approved', 'rewardsMinSize', 'rewardsMaxSpread', 'spread', 'oneDayPriceChange', 'oneHourPriceChange', 'oneWeekPriceChange', 'oneMonthPriceChange', 'oneYearPriceChange', 'lastTradePrice', 'bestBid', 'bestAsk', 'clearBookOnStart', 'manualActivation', 'negRiskOther', 'umaResolutionStatuses', 'pendingDeployment', 'deploying', 'rfqEnabled', 'holdingRewardsEnabled', 'feesEnabled'])
# (.venv) (base) PS C:\Users\jodyk\Projects\polytest> 