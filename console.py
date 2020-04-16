from v2 import Project_manager
from problema4 import problemaLab4
class UI:
    def __init__(self):
        pass

    def meniu(self):
        print("Alegeti o comanda: ")
        print("1.Rezolvati problema 2")
        print("2.Problema 4")
        print("3.Quit")
    def run(self):

        project=Project_manager()
        while(True):
            self.meniu()
            option = input("Comanda: ")
            if option=="1":
                project.solution("input.txt" , "output.txt")
            if option=="2":
                gen=int(input("Cate generatii: "))
                problemaLab4(gen)
            if option=="3":
                exit()

