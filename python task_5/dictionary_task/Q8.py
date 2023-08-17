#Create a dictionary of book titles and their respective authors, write a Python program that allows users to search for books by entering either the title or author's name.
books = {
    "Data Structure & Algorithm" : "Thomas H. Cormen",
    "Object Oriented Programming Language" : "Matt Weisfeld",
    "Operating System" : "Rohit Khurana",
    "Database Management System" : "Raghu Ramakrishnan",
    "Machine Learning" : "Oliver Theobald"
}

def search_books(query) :
    results = []
    for title, author in books.items():
        if query.lower() in title.lower() or query.lower() in author.lower() :
            results.append(title)
            return results

results = search_books("Weisfeld") 
print(results)