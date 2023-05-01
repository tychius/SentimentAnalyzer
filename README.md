# Sentiment Analysis Tool

A simple Sentiment Analysis Tool built using Python and TextBlob. This application analyzes the sentiment (positive, negative, or neutral) of a given text input.

## Features

- Graphical user interface for easy interaction
- Analyzes sentiment and provides polarity and subjectivity scores

## Installation

1. Download the standalone executable file for your platform from the [releases](https://github.com/tychius/SentimentAnalyzer/releases) page.
2. Run the executable file to launch the Sentiment Analysis Tool.

## Usage

1. Enter the text you want to analyze in the input text box.
2. Click the "Analyze" button.
3. The sentiment, polarity, and subjectivity scores will be displayed in the "Results" text box.

## Building from source

If you want to build the Sentiment Analysis Tool from source, follow these steps:

1. Clone the repository:

git clone https://github.com/tychius/SentimentAnalyzer.git


2. Change into the project directory:

cd SentimentAnalyzer


3. Create and activate a virtual environment:

- For Windows (using Git Bash):

python -m venv venv
source venv/Scripts/activate


- For macOS and Linux:

python3 -m venv venv
source venv/bin/activate


4. Install the required dependencies:

pip install -r requirements.txt


5. Run the application:

python main.py


6. (Optional) To create a standalone executable, install `pyinstaller` and build the executable as described in steps 4 and 5 of the main instructions.

