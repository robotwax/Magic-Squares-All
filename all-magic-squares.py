c = int(input())

def square(c):
    if c < 1 or c == 2:
        return False
    if c % 2 == 1:
        return(odd_square(c))
    else:
        if c % 4 == 0:
            return(dub_evensquare(c))
        elif c % 4 == 2:
            return(sing_evensquare(c))
        else:
            return(False)  

def odd_square(c):
    c0 = c + 1
    c1 = c0 * c0
    c2 = c - 1
    c3 = int(c/2)
    c4 = c * c
    c5 = c3 + 1
    start = np.arange(0, c1).reshape(c0, c0)
    mod1 = start % c
    clean = np.delete(mod1, c, 1)
    clean = np.delete(clean, c, 0)
    shift = np.roll(clean, c3, axis=1)
    matrix = np.arange(1, c4, c)
    matrix2 = np.repeat(matrix, c).reshape(c, c)
    firstsq = shift + matrix2
    rotatsq = np.rot90(firstsq, 3)
    mod2 = rotatsq % c
    shift2 = np.roll(mod2, c5, axis=1)
    matrix3 = np.arange(0, c)
    matrix4 = np.repeat(matrix3, c).reshape(c, c)
    matrix5 = matrix4 + shift2
    matrix5 = matrix5 % c
    matrix5[matrix5 == 0] = c
    shift5 = shift * c
    shift5 = np.rot90(shift5, 3)
    magic_square = shift5 + matrix5
    magic_square = np.rot90(magic_square, 1)
    return(magic_square)

def sing_evensquare(c):
    s = int(c/2)
    r = (odd_square(s))
    f = (s**2)
    e = r + f
    g = r + (f*2)
    h = r + (f*3)
    m = np.concatenate((r, g), axis=1)
    p = np.concatenate((h, e), axis=1)
    mas = np.concatenate((m, p), axis=0)
    bc = c - 6
    mas2 = mas.copy()
    dc = int(bc/4)
    gg = c - dc
    ee = ([-1]*dc)
    for i in ee:
        mas = np.delete(mas, i, 1)
    ff = ([0]*gg)
    for i in ff:
        mas2 = np.delete(mas2, i, 1)
    xf = np.roll(mas2, s, axis=0)
    px = np.concatenate((mas, xf), axis=1)
    eff = dc + 1
    px2 = px.copy()
    e2 = ([0]*eff)
    eg = c - eff
    for i in e2:
        px = np.delete(px, i, 1)
    ff = ([-1]*eg)
    for i in ff:
        px2 = np.delete(px2, i, 1)
    pxf = np.roll(px2, s, axis=0)
    px1 = np.concatenate((pxf, px), axis=1)
    af = int(s/2)
    ag = af + s
    temp = px1[af,0]
    px1[af,0] = px1[ag,0]
    px1[ag,0] = temp
    temp1 = px1[af, af]
    px1[af, af] = px1[ag, af]
    px1[ag, af] = temp1
    magicsum = px1[1].sum().tolist()
    return(px1)

def dub_evensquare(c):
    b = c*c
    z = range(1, b+1)
    s = (list(z))
    d = s[0] + s[-1]
    e = int(c/2)
    e = d * e
    f = int(c/4)
    g = [1, 0, 0, 1]*f
    h = [0, 1, 1, 0]*f
    i = [0, 1, 1, 0]*f
    k = [1, 0, 0, 1]*f
    m = g + h + i + k
    o = m * f
    p = np.array(o).reshape(c, c)
    p[p == 1] = d
    q = np.array(s).reshape(c, c)
    r = p - q
    magic_square = abs(r)
    magicsum = magic_square[1].sum().tolist()
    return(magic_square)
    
print(square(c))
