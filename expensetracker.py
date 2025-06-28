# set a budget
# add expenses in categories
# transport, food, accomodation, shopping, sightseeing



class Expenses:
    def __init__(self, budget):
        self.budget = budget
        self.total = 0
        self.categories = {
            "transportation": [],
            "food": [],
            "accomodation": [],
            "shopping": [],
            "sightseeing": []
        }
        print("specify a category when adding the expense: \n\nBudget:")
        print(self.budget, "\n")
        print([c for c in self.categories.keys()], "\n")
    
    def add_expense(self, cat, amount, comment = None):
        self.categories[cat].append([amount, comment])
        self.total += amount

    def list_expenses(self):
        print("\nListing Expenses: ")
        for k, i in self.categories.items():
            print(f"{k}: {i}")
        print(f"\nRemaining budget: {self.budget - self.total}")

    def list_total(self):
        print(f"Expenses:")
        for k, v in self.categories.items():
            total = 0
            for i in range(len(v)):
                total += v[i][0]
            print(f"{k}: {total}")
        print("Total:", self.total)
        


expenses = Expenses(500)
expenses.add_expense("transportation", 20, "Prague to Bratislava")
expenses.add_expense("transportation", 15, "Bratislava to Budapest")
expenses.add_expense("transportation", 15, "Budapest to Vienna")
expenses.add_expense("transportation", 27, "Vienna to Munich")
expenses.add_expense("food", 10 * 8, "eating")
expenses.add_expense("accomodation", 20 * 7, "hostels")
expenses.list_total()
expenses.list_expenses()