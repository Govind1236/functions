class Me:
    name = ""
    occupation = ""
    def info(self):
        print(f"{self.name} is an {self.occupation}")
obj = Me()
obj.name = "Govind"
obj.occupation = "All Rounder"
obj.info()
