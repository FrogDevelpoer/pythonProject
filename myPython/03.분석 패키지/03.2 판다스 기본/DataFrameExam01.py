from pandas import DataFrame

sdata = {
            '도시': ['서울', '서울', '서울', '부산', '부산'],
            '년도': [2000, 2001, 2002, 2001, 2002],
            '실적': [150, 170, 360, 240, 290]
        }
myindex = ['one', 'two', 'three', 'four', 'five']
myframe = DataFrame(sdata, index=myindex)
print(myframe)
print(type(myframe))

myframe.columns.name = 'ㅎㅎ'
myframe.index.name = 'ㅋㅋ'
print(myframe)

print(myframe.index)
print(myframe.columns)
print(myframe.values)
print(type(myframe.values))

print(myframe.dtypes)
print(myframe.T)

mycolumns = ['실적', '도시', '년도']
newframe = DataFrame(sdata, columns=mycolumns)
print(newframe)