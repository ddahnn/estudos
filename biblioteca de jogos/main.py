from modules.Genero import Genero
from modules.JogoFisico import JogoFisico
from modules.JogoDigital import JogoDigital
line = "*"

gen = Genero("Ação")


gen2=Genero("c")
j1 = JogoFisico("a", 'b', gen2, "d", 1 )
j2 = JogoFisico("ae", 'f', gen, "g", 8 )

j1.cadastrar()
j2.cadastrar()



g3 = Genero("Comedia")
g4 = Genero("Terror")
jd = JogoDigital("h", "i", g3, 19.5, 255.9)
jd2 = JogoDigital("cv", "m", g4, 55.5, 299.59)

jd.cadastrar()
jd2.cadastrar()




print(f"\n\n" + line*20 + "lista fisica" + line*20 + f"\n\n")
j1.ver_Lista()


print(f"\n\n" + line*20 + "lista Digital" + line*20 + f"\n\n")

jd.ver_Lista()