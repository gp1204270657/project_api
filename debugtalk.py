import hashlib
import random
import time

#获取协议金额
def getAmount():
    amount=random.randint(20000,60000)
    return amount

def timesleep():
    time.sleep(1)


def jiamimd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()

def generate_sig(request):
    offset='0ce37dd6b927730161a1e559c2336d0a'
    s = ''

    res = sorted(request["params"].items(), key=lambda item: item[0])

    for i in range(0,len(res)):

        s = s + str(res[i][0])+'='+str(res[i][1])

    # for k,v in request["params"].items():
    #     print(k,v)
    #     s = s + k+'='+v
    s = s+offset

    _sig = jiamimd5(s)

    request["params"]['_sig'] = _sig

    return request