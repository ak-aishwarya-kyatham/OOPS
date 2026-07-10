# Student Library OOP Project

This is a Python project built to demonstrate Object-Oriented Programming (OOP) concepts.

## Project Overview

The project models a simple library system where students can browse and borrow items such as books and magazines.

## OOP Concepts Used

- **Classes and Objects**: `LibraryItem`, `Book`, `Magazine`, and `Library` are classes used to create objects.
- **Encapsulation**: Data fields are stored as private or protected members (`_title`, `_author`, `_available`) and accessed via public methods/properties.
- **Abstraction**: `LibraryItem` is an abstract base class defining common behavior for all library items.
- **Inheritance**: `Book` and `Magazine` inherit from `LibraryItem`.
- **Polymorphism**: The `get_description` method is implemented differently by `Book` and `Magazine`, allowing each item to describe itself appropriately.

## Files

- `library_item.py` - Abstract base class and common library item behavior.
- `book.py` - `Book` class that inherits from `LibraryItem`.
- `magazine.py` - `Magazine` class that inherits from `LibraryItem`.
- `library.py` - `Library` class and demo library builder.
- `library_project.py` - Main program containing the command-line interface.
- `README.md` - Project explanation and usage instructions.

## How to Run

1. Make sure you have Python installed (version 3.8 or newer).
2. Open a terminal in the project folder.
3. Run the project:

```bash
python library_project.py
```

## Project Features

- Add and manage library items.
- Search items by title.
- Borrow and return items.
- Clear console interface for student interaction.

## Example Use

- View currently available books and magazines.
- Search by title keyword like `Ocean` or `Coding`.
- Borrow an item by ID.
- Return an item by ID.

## Notes

This project was created to satisfy an OOP school assignment and clearly demonstrates functions, classes and objects, encapsulation, abstraction, inheritance, and polymorphism.
