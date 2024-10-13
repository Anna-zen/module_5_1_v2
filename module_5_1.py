# Домашняя работа по уроку "Атрибуты и методы объекта."
class House :
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print (' Такого этажа у ', self.name, ' не существует ')
        else:
            for i in range (new_floor) :
                print(i+1)
            print(' Приехали на ',new_floor ,' этаж ', self.name)




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(-2)
h2.go_to(2)