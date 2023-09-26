from sklearn.linear_model import LogisticRegression
sids=[
    [1,1,0,0,0,1],
    [1,0,0,1,1,0],
    [1,0,1,1,0,1],
    [0,1,0,1,1,1],
    [1,1,1,0,0,0],
    [0,1,0,0,1,1]
]
sid_table=[
    [0,6],
    [3,7],
    [5,9],
    [1,7],
    [2,9],
    [5,6]
]
sid_price=[
    404,
    573,
    107,
    210,
    330,
    178
]
def surg1(sid,alpha=2.0):
    alpha=max(1.0, alpha)
    base_price=1.0
    price=base_price+(alpha - 1.0)*(1.0-(sid[0]/sid[1]))
    price=min(price,2.0)
    return price
p=int(input('Enter slot Id: '))
h=surg1(sid_table[p],1.6)
print('Price for that slot is: ', h*sid_price[p])
