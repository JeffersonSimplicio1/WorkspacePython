def metros_para_cent (a, num):
    if num == 1:
        resp = a / 1000
        return resp
    elif num == 2:
        resp = a/100
        return resp
    elif num == 3:
        resp = a/10
        return resp
    elif num == 4:
        resp = a
        return resp
    elif num == 5:
        resp = a*10
        return resp
    elif num == 6:
        resp = a*100
        return resp
    elif num == 7:
        resp = a*1000
        return resp
    else:
        return print(f'O valor que você digitou é invalido!!')


def medida (m):
    if m == 1:
        resp = 'km'
        return resp
    elif m == 2:
        resp = 'hm'
        return resp
    elif m == 3:
        resp = 'dam'
        return resp
    elif m == 4:
        resp = 'm'
        return resp
    elif m == 5:
        resp = 'dm'
        return resp
    elif m == 6:
        resp = 'cm'
        return resp
    elif m == 7:
        resp = 'mm'
        return resp