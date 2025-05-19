import os
import json

LIBRARY_FILE = "library.txt"
library = []

# Load library from file (with error handling)
def load_library():
    try:
        if os.path.exists(LIBRARY_FILE):
            with open(LIBRARY_FILE, "r") as file:
                return json.load(file)
    except Exception as e:
        print(f"Error loading library: {e}")
    return []

# Save library to file (with error handling)
def save_library():
    try:
        with open(LIBRARY_FILE, "w") as file:
            json.dump(library, file)
    except Exception as e:
        print(f"Error saving library: {e}")

# Add a book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    try:
        year = int(input("Enter the publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("Book added successfully!")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ").strip()
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

# Search books
def search_books():
    print("Search by: \n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    if choice not in ['1', '2']:
        print("Invalid choice.")
        return
    keyword = input("Enter the search term: ").strip().lower()
    matches = []

    for book in library:
        if (choice == '1' and keyword in book['title'].lower()) or \
           (choice == '2' and keyword in book['author'].lower()):
            matches.append(book)

    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found.")

# Display all books
def display_books():
    if not library:
        print("Library is empty.")
    else:
        print("Your Library:")
        for i, book in enumerate(library, 1):
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

# Display statistics
def display_stats():
    total = len(library)
    if total == 0:
        print("Library is empty.")
        return
    read_books = sum(1 for book in library if book['read'])
    percent_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percent_read:.1f}%")

# Main menu loop
def menu():
    while True:
        print("\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
# Start
library = load_library()
menu()
