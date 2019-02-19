def square(a):
	if a < 1 or a == 2:
		return False
	if a % 2 == 1:
		return oddsquare(a)
	else:
		if a % 4 == 0:
			return 2evensquare(a)
		elif a % 4 == 2:
			return 1evensquare(a)
		else:
			return False

c = int(25)
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
print(magic_square)

def 1evensquare(a):
	def odd_square(a):
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
		print(magic_square)
    r = (odd_square(a))
    f = (c**2)
    e = r + f
    g = r + (f*2)
    h = r + (f*3)
    m = np.concatenate((r, g), axis=1)
    p = np.concatenate((h, e), axis=1)
    mas = np.concatenate((m, p), axis=0)
    bc = a - 6
    mas2 = mas.copy()
    dc = int(bc/4)
    gg = a - dc
    ee = ([-1]*dc)
    for i in ee:
        mas = np.delete(mas, i, 1)
    ff = ([0]*gg)
    for i in ff:
        mas2 = np.delete(mas2, i, 1)
    xf = np.roll(mas2, c, axis=0)
    px = np.concatenate((mas, xf), axis=1)
    eff = dc + 1
    px2 = px.copy()
    e2 = ([0]*eff)
    eg = a - eff
    for i in e2:
        px = np.delete(px, i, 1)
    ff = ([-1]*eg)
    for i in ff:
        px2 = np.delete(px2, i, 1)
    pxf = np.roll(px2, c, axis=0)
    px1 = np.concatenate((pxf, px), axis=1)
    af = int(c/2)
    ag = af + c
    temp = px1[af,0]
    px1[af,0] = px1[ag,0]
    px1[ag,0] = temp
    temp1 = px1[af, af]
    px1[af, af] = px1[ag, af]
    px1[ag, af] = temp1
    magicsum = px1[1].sum().tolist()
    with open('magicsum.txt', 'w') as f:
        return json.dump(magicsum, f)


def 2evensquare(a):
    z = range(1, b+1)
    c = (list(z))
    d = c[0] + c[-1]
    e = int(a/2)
    e = d * e
    f = int(a/4)
    g = [1, 0, 0, 1]*f
    h = [0, 1, 1, 0]*f
    i = [0, 1, 1, 0]*f
    k = [1, 0, 0, 1]*f
    m = g + h + i + k
    o = m * f
    p = np.array(o).reshape(a, a)
    p[p == 1] = d
    q = np.array(c).reshape(a, a)
    r = p - q
    magic_square = abs(r)
    magicsum = magic_square[1].sum().tolist()
    with open('magicsum.txt', 'w') as f:
        return json.dump(magicsum, f)


