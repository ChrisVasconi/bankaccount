
class User:
    # -!- CONSTRUCTOR FUNCTION!!! CREATES THE INSTANCE OF AN OBJECT
    bank_name = "First National Dojo"

    def __init__(self, first_name, email_adress):
        self.first_name = "michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0


guido = ("Guido van Rossum", "guido@python.com")
monty = ("Monty Python", "monty@python.com")
print(guido.name)
print(monty.name)
