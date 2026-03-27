class car():
    name="Benz"
    model=2016
    def __init__(self,company):
        self.company=company

    def display(self):
        return self.company


class new_car(car):
    name="BMW"


obj1=new_car("poo")
print(obj1.name)
print(obj1.model)
print(obj1.display())