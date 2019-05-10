import turtle
t = turtle.Pen()

def estrellanlados(lados):
	for x in range(1, (l+1)):
		t.forward(100)
		t.left(lados)


l = int(input("El numero de lados impar es: "))
ang = (-(360/l+180)*2)
estrellanlados(ang)