
import datetime as dt

t = dt.datetime.today()

# print(t + dt.timedelta(days=-5))

# print(t + dt.timedelta(hours=8))

# print(dt.datetime.strftime(t, "%Y %m %d, %H:%M:%S"))
# print(t.strftime("%Y %m %d, %H:%M:%S"))

def avg(*args):
    return(sum(args)/len(args))

print(avg(1, 2, 3))

def comb(**kvargs):
    s = ''
    for k, v in kvargs.items():
        s += f'<{k}>: <{v}>\n'
    return s

print(comb(a = 12, b = 'z'))
