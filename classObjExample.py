class employee:
    def __init__(self):
        print("the execution is started data/attribute are initializing")
        self.id = 123
        self.salary = 50000
        self.Designation = "Data Scientist"
        print("the execution is completed data/attribute are initialized")


    def travel(self,destination):
        print("the method called manually started")
        print(f'Traveling to {destination}')
        

ram = employee()
print(ram.id)
ram.travel("India")