
# coding: utf-8

# In[4]:

tail ../zipline/examples/buyapple.py

from zipline.api import order, record, symbol


def initialize(context):
    pass


def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data[symbol('AAPL')].price)


# In[ ]:



