# encoding: utf-8
def function():

	print("Asignaturas optativas Agno 2017")

	print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
	
	asignatura=input("Escribe la asignatura escogida")

	if asignatura in ("Informatica gráfica", "Pruebas de software", "Usabilidad y accesibilidad"):

		print("Asignatura elegida" +asignatura)

	else:
		print("La asignatura escogida no esta completada")

function ()