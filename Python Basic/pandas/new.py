import pandas as pd


# info={
#     "name":["sumit","ram","shyam"],
#     "age":[20,21,22]
# }
# df=pd.DataFrame(info)
# print(df)


# s=pd.Series([1,2,3,4,5])
# print(s)



s=pd.Series([12,14,18,19],index=['rahul','shivem','anil','monu'])
print(s)

# output 

# PS D:\Ai &Ml  by Shardha Khapra\Python Basic\pandas> python new.py
# rahul     12
# shivem    14
# anil      18
# monu      19
# dtype: int64

# we can access with labeled  values  like this
print(s['monu'])

# dtype: int64
# 19

print(s.index)

# Index(['rahul', 'shivem', 'anil', 'monu'], dtype='str')