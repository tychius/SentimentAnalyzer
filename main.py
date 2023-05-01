import tkinter as tk
from tkinter import ttk
from textblob import TextBlob

def analyze_sentiment():
    try:
        # Obtain the input text
        text = input_text.get("1.0", tk.END).strip()

        # Raise ValueError if there is no input text
        if not text:
            raise ValueError("No input text")

        # Create a TextBlob object
        blob = TextBlob(text)

        # Obtain sentiment polarity and subjectivity
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Classify sentiment based on polarity
        if polarity > 0.5:
            sentiment = "Very Positive"
        elif 0.1 < polarity <= 0.5:
            sentiment = "Slightly Positive"
        elif -0.1 <= polarity <= 0.1:
            sentiment = "Neutral"
        elif -0.5 <= polarity < -0.1:
            sentiment = "Slightly Negative"
        else:
            sentiment = "Very Negative"

        # Display the results
        result_text.configure(state="normal")  # Enable the result_text widget
        result_text.delete("1.0", tk.END)

        result_text.tag_configure("header", font="TkDefaultFont 10 bold")
        result_text.tag_configure("value", font="TkDefaultFont 10")

        result_text.insert(tk.END, "Sentiment: ", "header")
        result_text.insert(tk.END, f"{sentiment}\n", "value")
        result_text.insert(tk.END, "Polarity: ", "header")
        result_text.insert(tk.END, f"{polarity:.2f}\n", "value")
        result_text.insert(tk.END, "Subjectivity: ", "header")
        result_text.insert(tk.END, f"{subjectivity:.2f}\n", "value")
        
        result_text.configure(state="disabled")  # Disable the result_text widget
    except ValueError as e:
        # Handle ValueError exceptions separately to provide better feedback
        result_text.configure(state="normal")  # Enable the result_text widget
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {e}")
        result_text.configure(state="disabled")  # Disable the result_text widget
    except:
        # Handle other exceptions
        result_text.configure(state="normal")  # Enable the result_text widget
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "An error occurred while analyzing the sentiment.")
        result_text.configure(state="disabled")  # Disable the result_text widget

def clear_input():
    input_text.delete("1.0", tk.END)  # Clear the input text box

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

#Create clear input button
clear_input_button = ttk.Button(root, text="Clear Input", command=clear_input)
clear_input_button.pack()

#Create result text box
result_label = ttk.Label(root, text="Results:")
result_label.pack()
result_text = tk.Text(root, wrap=tk.WORD, width=40, height=10, state="disabled")
result_text.pack()

# Run the main loop
root.mainloop()
