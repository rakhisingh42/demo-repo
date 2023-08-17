#Implement a function that takes a list of dictionaries, each representing a person's income and expenses for a month. The keys in each dictionary are "name", "income", and "expenses". Calculate the savings (income-expenses) for each person and return the result as a new dictionary with the names as keys and savings as values
def calculate_savings(data):
    savings={}
    for item in data:
        name = item['name']
        income = item['income']
        expenses = item['expenses']
        savings[name] = income - expenses
    return savings
data = [
    {"name": "Rakhi", "income": 10000, "expenses" : 3000},
    {"name": "Shivani", "income": 15000, "expenses" : 5000},
    {"name": "Vishakha", "income": 8000, "expenses" : 2500},
    {"name": "Ojal", "income": 5000, "expenses" : 2000}
]
savings = calculate_savings(data)
print(savings)