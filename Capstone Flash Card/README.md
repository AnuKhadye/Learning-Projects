# Flash Card Application

This is a simple flashcard application built using Python's Tkinter library. The app helps users learn French vocabulary by displaying words in French and allowing them to guess the English equivalent. The application uses a CSV file containing French words and their English translations.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Directory and File Descriptions](#directory-and-file-descriptions)
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
   
bash
   pip install pandas

## Directory and File Description
- **data/**: Contains the CSV files for the flashcards.
  - `french_words.csv`: Original list of French words.
  - `french_words_known_removed.csv`: List of known words after the app is run.
  
- **images/**: Contains the images used in the flashcards.
  - `card_front.png`: Image for the front of the flashcard.
  - `card_back.png`: Image for the back of the flashcard.
  - `wrong.png`: Image displayed for incorrect answers.
  - `right.png`: Image displayed for correct answers.

- **flashcard_app.py**: The main script for the flashcard application.
## License

This project is open-source and free to use under the [MIT License](../LICENSE).

how can i link the directory and file description
