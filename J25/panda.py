import pandas as pd
import numpy as np


df=pd.read_csv('hacker_news.csv')

first_five_rows=df.head()
last_five_rows=df.tail()

title_column=df['title']

number_row_column=df.shape

title_contains_python=df[title_column.str.contains('python')]
title_contains_javascript=df[title_column.str.contains('JavaScript')]
print(title_contains_javascript)