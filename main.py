import tkinter as tk  # for graphical interface
# for natural language processing - NLTK (Natural language tool kit)
import nltk
from textblob import TextBlob  # for sentiment analysis
from newspaper import Article  # to read new articles from url

nltk.download('punkt')

def sentiment_analysis(text):
    analysis = TextBlob(text)
    if analysis.polarity > 0:
        return 'Positive'
    elif analysis.polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

def summarize():
    #url = 'https://www.businesstoday.in/personal-finance/top-story/story/investing-in-us-market-should-you-take-a-bet-on-us-treasury-bonds-or-gold-now-403608-2023-10-28'
    url = input_url.get('1.0', 'end').strip()

    article = Article(url)
    article.download()
    article.parse()

    article.nlp()

    title.config(text=article.title)
    author.config(text=f"By: {article.authors}")
    published_date.config(text=f"Date: {article.publish_date}")
    sentiment.config(text=f"Sentiment: {sentiment_analysis(article.text)}")

    summary.config(state='normal')
    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)
    summary.config(state='disabled')

    print(f'Title: {article.title}')
    print(f'Author: {article.authors}')
    print(f'Published Date: {article.publish_date}')
    print(f'Summary: {article.summary}')
    print(f'Text Length: {len(article.text)} words')
    

# create tkinter window
window = tk.Tk()
window.title("News Sumarizer")
window.geometry('800x500')
window.config(padx=10, pady=10)

input_url = tk.Text(window, width=85, height=2)
input_url.grid(row=0, column=0, sticky='w', columnspan=2, pady=5)

button = tk.Button(window, text="Summarize", height=2, background= 'blue',command=summarize)
button.grid(row=0, column=1, sticky='e', columnspan=2, padx=10, pady=5)

# create tkinter widgets
title = tk.Label(window, font=('Arial', 16, 'bold'), wraplength=780)
title.grid(row=1, column=0, sticky='w', columnspan=2, pady=5)

author = tk.Label(window, font=('Arial', 12))
author.grid(row=2, column=0, sticky='w', columnspan=2, pady=5)

published_date = tk.Label(window,font=('Arial', 12))
published_date.grid(row=3, column=0, sticky='w', columnspan=2, pady=5)
# 
sentiment = tk.Label(window, font=('Arial', 12))
sentiment.grid(row=4, column=0, sticky='w', columnspan=2, pady=5)

summary = tk.Text(window, width=110, height=12, font=('Arial', 10))
summary.grid(row=5, column=0, sticky='w', columnspan=2, pady=5)
summary.config(state='disabled')

# grid layout
# title.grid(row=0, column=0, columnspan=2, pady=10)
# sentiment.grid(row=1, column=0, columnspan=2, pady=10)
# 
# run tkinter app
window.mainloop()