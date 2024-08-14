import tkinter as tk
from tkinter import messagebox
import random
import json
import os
import pyperclip
from datetime import date

class InspirationalQuotesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inspirational Quotes")
        self.root.geometry("400x500")

        self.quotes = self.load_quotes()
        self.favorites = self.load_favorites()

        self.current_quote = tk.StringVar()
        self.update_quote()

        self.quote_label = tk.Label(root, textvariable=self.current_quote, wraplength=350, font=("Helvetica", 14), pady=20)
        self.quote_label.pack(pady=20)

        self.refresh_button = tk.Button(root, text="New Quote", command=self.update_quote)
        self.refresh_button.pack(pady=10)

        self.favorite_button = tk.Button(root, text="Add to Favorites", command=self.add_to_favorites)
        self.favorite_button.pack(pady=10)

        self.view_favorites_button = tk.Button(root, text="View Favorites", command=self.view_favorites)
        self.view_favorites_button.pack(pady=10)

        self.share_button = tk.Button(root, text="Share Quote", command=self.share_quote)
        self.share_button.pack(pady=10)

    def load_quotes(self):
        # List of inspiring quotes
        return [
            "The best way to predict the future is to create it.",
            "Do not wait for the perfect moment, take the moment and make it perfect.",
            "Success is not final, failure is not fatal: It is the courage to continue that counts.",
            "Believe you can and you're halfway there.",
            "Act as if what you do makes a difference. It does.",
            "Keep your face always toward the sunshine—and shadows will fall behind you.",
            "What lies behind us and what lies before us are tiny matters compared to what lies within us."
        ]

    def load_favorites(self):
        if os.path.exists("favorites.json"):
            with open("favorites.json", "r") as file:
                return json.load(file)
        else:
            return []

    def save_favorites(self):
        with open("favorites.json", "w") as file:
            json.dump(self.favorites, file)

    def update_quote(self):
        # Show a random quote from the list
        self.current_quote.set(random.choice(self.quotes))

    def add_to_favorites(self):
        quote = self.current_quote.get()
        if quote not in self.favorites:
            self.favorites.append(quote)
            self.save_favorites()
            messagebox.showinfo("Favorite Added", "Quote added to favorites.")
        else:
            messagebox.showwarning("Already Exists", "This quote is already in your favorites.")

    def view_favorites(self):
        if not self.favorites:
            messagebox.showinfo("No Favorites", "You have no favorite quotes yet.")
            return

        favorites_window = tk.Toplevel(self.root)
        favorites_window.title("Favorite Quotes")

        for i, quote in enumerate(self.favorites):
            quote_label = tk.Label(favorites_window, text=quote, wraplength=350, font=("Helvetica", 12), pady=10)
            quote_label.pack(anchor="w", padx=10)

    def share_quote(self):
        quote = self.current_quote.get()
        pyperclip.copy(quote)
        messagebox.showinfo("Quote Copied", "Quote copied to clipboard. You can now share it.")

if __name__ == "__main__":
    root = tk.Tk()
    app = InspirationalQuotesApp(root)
    root.mainloop()
