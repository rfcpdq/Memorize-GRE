import pandas as pd


def timestamp2datetime(timestamp):
    datetime = ((pd.to_datetime(timestamp, unit='us')).dt.tz_localize(
        'UTC').dt.tz_convert('Asia/Shanghai')).astype('str')
    datetime = datetime.str.split('+', expand=True)[0]
    return datetime
