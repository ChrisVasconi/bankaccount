class User:
    def __inti__(self, first_name, last_name, age):
        self.first_name = "Adrien"
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hello my name is {self.firstname}!")


adrien = User("Adrien", "Dion", 39)
adrien.greeting()
