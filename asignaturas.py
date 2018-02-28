# encoding: utf-8
print("Asignaturas optativas Agno 2017")

print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida ")

asignatura=opcion.lower();

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):

    print("Asignatura elegida es: " +asignatura)

else:
    print("La asignatura escogida no esta completada")