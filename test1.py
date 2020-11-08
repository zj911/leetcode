'''
回文年
'''

def mouth(m):
    if m != '00' and int(m) <= 12: 
        return m
    else:
        return 0
def day(y, m,d):
    if int(m) in [1,3,5,7,8,10,12]:
        if int(d) > 31:
            return 1
        else:
            return d
    elif int(m) in [4,6,9,11]:
        if int(d) > 30:
            return 1
        else:
            return d
    elif int(m) == 2:
        if int(d) > 28:
            return 1
        else:
            return d

for i in range(2000, 3000):
    year = str(i)
    m = str(i)[::-1][:2]
    d = str(i)[::-1][2:4]
    get_mouth = mouth(m)
    get_day = day(year, m, d)
    if get_mouth  != 0 and get_day != 1:
        print(year+get_mouth+get_day)