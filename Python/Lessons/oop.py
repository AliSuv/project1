class Human():
    # definice atributu mimo konstruktor (většinou pro konstatní hodonty)
    con = "KONSTANTA"

    # self - reference sama na sebe
    # __init__ - konstruktor = funkce která se spouští při deklaraci třídy do proměnné (objektu)
    def __init__(self, age):
        # definuje nový atribut age (je přístupný skrz celou classu pomocí self.)
        self.age = age

    def sayHello(self):
        print(f"Hello je mi {self.age}")

    def sayHi(self):
        pass  # do nothing

    def sayInfoAboutMe(self):
        print(self.age)


class Worker(Human):  # dědení z Human (převezmu charakteristiku z předešlé třídy)
    def __init__(self, age, work_hours):
        super().__init__(age)  # zavolá konstruktor z předka
        self.work_hours = work_hours  # kód specifický pro následníka

    def work(self):
        print(f"Working for {self.work_hours} hours")

    def sayHi(self):
        print("Hi")

    def sayInfoAboutMe(self):
        super().sayInfoAboutMe()  # zavolá metodu z předka
        print(self.work_hours)


human = Human(15)
human.sayHello()
human.sayHi()
human.sayInfoAboutMe()

human2 = Worker(25, 8)
human2.sayHello()  # metoda převzatá z předka
human2.work()  # metoda specifická pro následníka
human2.sayHi()
human2.sayInfoAboutMe()
