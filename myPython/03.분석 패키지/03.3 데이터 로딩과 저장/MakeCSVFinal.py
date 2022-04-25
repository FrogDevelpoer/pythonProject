import pandas as pd
from pandas import DataFrame
import numpy as np

myencoding = 'UTF-8'
mycolumns = ('이름', '나이')
mydata = [('김철수', 10), ('박영희', 20)]
myframe = DataFrame(data=mydata, columns=mycolumns, index=None)
print(myframe)

myframe = pd.DataFrame(myframe)
filename = 'csv_02_01.csv'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)

filename = 'csv_02_02.csv'
myframe.to_csv(filename, encoding=myencoding, columns=mycolumns, mode='w', index=False, sep='#')