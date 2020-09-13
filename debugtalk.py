import hashlib


def jiamimd5(src):
    m = hashlib.md5()
    m.update(src.encode('UTF-8'))
    return m.hexdigest()

def generate_sig(request):
    offset='0ce37dd6b927730161a1e559c2336d0a'
    s = ''
    print(request)
    res = sorted(request["params"].items(), key=lambda item: item[0])
    print(res)
    for i in range(0,len(res)):
        print(res[i][0])
        print(res[i][1])
        s = s + res[i][0]+'='+res[i][1]

    # for k,v in request["params"].items():
    #     print(k,v)
    #     s = s + k+'='+v
    s = s+offset
    print(s)
    _sig = jiamimd5(s)
    print('_sig---------'+_sig)
    request["params"]['_sig'] = _sig
    print(request)
    return request