class Car(object):
    def __init__(self,make,model,color):
        self.make = make
        self.model = model
        self.color = color
        self.owner_no = 0

    def car_info(self):
        print("Make: ",self.make)
        print("Model: ",self.model)
        print("Color: ",self.color)
        print("Number of owners",self.owner_no)
    
    def sell(self):
        self.owner_no += 1

my_car = Car("Honda","Accord","Black")

my_car.car_info()
my_car.sell()
my_car.car_info()

