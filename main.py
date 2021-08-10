from load_data import table_data_filter
from sentiment_trend import get_sentiment_trend

data=table_data_filter("./data.csv",name_ch="疯狂动物城")
get_sentiment_trend(data)