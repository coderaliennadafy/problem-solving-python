class person():
    def __init__(self,name):
        self.name = name
    def talk(self):
        print("talk")

john = person("john smith")
print(john.name)
john.talk()    
    