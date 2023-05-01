import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

def analyze_sentiment():
    # Obtain the input text
    text = input_text.get("1.0", tk.END)

    # Create a TextBlob object
    blob = TextBlob(text)

    # Obtain sentiment polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Classify sentiment based on polarity
    if -0.1 < polarity < 0.1:
        sentiment = "Neutral"
    elif polarity >= 0.1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    # Display the results
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Sentiment: {sentiment}\n")
    result_text.insert(tk.END, f"Polarity: {polarity:.2f}\n")
    result_text.insert(tk.END, f"Subjectivity: {subjectivity:.2f}")

# Create the main window
root = tk.Tk()
root.title("Sentiment Analysis Tool")

# Create input text box
input_label = ttk.Label(root, text="Enter text for sentiment analysis:")
input_label.pack()
input_text = tk.Text(root, wrap=tk.WORD, width=40, height=10)
input_text.pack()

# Create analyze button
analyze_button = ttk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Create result text box
result_label = ttk.Label(root, text="Results:")
result_label.pack()
result_text = tk.Text(root, wrap=tk.WORD, width=40, height=10, state="disabled")
result_text.pack()

# Run the main loop
root.mainloop()
