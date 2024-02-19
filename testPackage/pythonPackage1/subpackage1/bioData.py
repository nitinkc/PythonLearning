class MybioData:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def getNameAge(self):
        return f"my nme is {self.name} and age is {self.age}"

    def getNameCity(self):
        return f"my nme is {self.name} and city is {self.city}"

    def getAll(self):
        return f"my nme is {self.name}, and age is {self.age} and I live in {self.city}"


GNA = MybioData("Prasad", 35, "Durg")
