import turtle
t=turtle.Pen()

def micuadrado (tamano):
	for x in range (1, 5):
		t.forward(tamano)
		t.left(90)

n = float(input("tamaño del cuadrado: "))

micuadrado(n)