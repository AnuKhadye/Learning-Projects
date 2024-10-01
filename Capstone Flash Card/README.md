# Flash Card Application

This is a simple flashcard application built using Python's Tkinter library. The app helps users learn French vocabulary by displaying words in French and allowing them to guess the English equivalent. The application uses a CSV file containing French words and their English translations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)


## Features

- Display flashcards with French words and their English translations.
- Automatically flip cards to show the English translation after a few seconds.
- Track known words and remove them from the deck for future sessions.

## Requirements

To run this application, you'll need the following:

- Python 3.x
- Tkinter library (usually included with Python installations)
- Pandas library
- A CSV file containing French words and their English translations.

## Installation

1. Clone this repository or download the source code.
2. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
3. Install the Pandas library if you haven't already:
   ```bash
   pip install pandas

## File Structure
Capstone Flash Card)
│
├── data/
│   ├── french_words.csv
│   └── french_words_known_removed.csv (generated after running the app)
│
├── images/
│   ├── card_front.png
│   ├── card_back.png
│   ├── wrong.png
│   └── right.png
│
└── flashcard_app.py  (your main application script)

## License

This project is open-source and free to use under the [MIT License](../LICENSE).


