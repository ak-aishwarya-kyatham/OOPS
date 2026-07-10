# Student Media Rental OOP Project

This is a Python project built to demonstrate Object-Oriented Programming (OOP) concepts.

## Project Overview

The project models a simple media rental store where students can browse and borrow items such as movies and series.

## OOP Concepts Used

- **Classes and Objects**: `LibraryItem`, `Book`, `Magazine`, and `Library` are classes used to create objects.
- **Encapsulation**: Data fields are stored as private or protected members (`_title`, `_author`, `_available`) and accessed via public methods/properties.
- **Abstraction**: `LibraryItem` is an abstract base class defining common behavior for all library items.
- **Inheritance**: `Book` and `Magazine` inherit from `LibraryItem`.
- **Polymorphism**: The `get_description` method is implemented differently by `Book` and `Magazine`, allowing each item to describe itself appropriately.

## Files

- `media_item.py` - Abstract base class and common media item behavior.
- `movie.py` - `Movie` class that inherits from `MediaItem`.
- `series.py` - `Series` class that inherits from `MediaItem`.
- `media_store.py` - `MediaStore` class and demo store builder.
- `media_store_app.py` - Main program containing the command-line interface.
- `README.md` - Project explanation and usage instructions.

## How to Run

1. Make sure you have Python installed (version 3.8 or newer).
2. Open a terminal in the project folder.
3. Run the project:

```bash
py media_store_app.py
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
