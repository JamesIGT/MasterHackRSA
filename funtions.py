def es_primo(n):
    if n >= 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    else:
        return False

def generar_primos(n):
    lista_primos = []
    numero = 2
    while len(lista_primos) < n:
        if es_primo(numero):
            lista_primos.append(numero)
        numero += 1
    return lista_primos

def mcd(e, ø):
    m = ø % e
    while m != 0:
        ø, e = e, m
        m = ø % e
    return e

def calcular_e(ø):
    e = 2
    lista_e = []
    while e < ø:
        if mcd(e, ø) == 1:
            lista_e.append(e)
        e += 1
    return lista_e

def calcular_d(e, ø):
    k = 1
    m = (1 + (k * ø)) % e
    while m != 0:
        k += 1
        m = (1 + (k * ø)) % e
    d = (1 + (k * ø)) // e
    return d

def buscarpos(letra):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alf.index(letra)

def buscarlet(posicion):
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alf[posicion % len(alf)]

def cifrar_mensaje(mensaje, keyPublic):
	mensaje = mensaje.upper()
	list_msg = mensaje.split(" ")
	list_msg_cif=[]
	for palabra in list_msg:
		pal_cif=cifrar_palabra(palabra, keyPublic)
		list_msg_cif.append(pal_cif)
	return " ".join(list_msg_cif)

def cifrar_palabra(m, keyPublic):
	n, e = keyPublic
	lp=[]
	lpc=[]
	for letra in m:
		li=buscarpos(letra)
		lp.append(li)
	for mi in lp:
		lpi=((mi**e) % n )
		lpc.append(lpi)
	return " ".join(map(str, lpc))

def descifrar_mensaje(msj, key):
    msj = msj.upper()
    lm = msj.split(" ")
    lmc = [descifrar_numero(pal, key) for pal in lm]
    return " ".join(lmc)

def descifrar_numero(m, k):
    n, d = k
    ln = [int(x) for x in m.split(" ")]
    lnc = [(j**d) % n for j in ln]
    return "".join(buscarlet(k) for k in lnc)