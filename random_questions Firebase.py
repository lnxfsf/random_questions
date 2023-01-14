
import tkinter as tk
import mysql.connector

#uses SQL 

# Connect to the database
db = mysql.connector.connect(
    host="hostname",
    user="username",
    password="password",
    database="database"
)

# Create a cursor object to execute SQL commands
cursor = db.cursor()

# Define the GUI
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Random Question Generator")
        self.question_label = tk.Label(self, text="Loading question...")
        self.question_label.pack()
        self.get_random_question()
    
    def get_random_question(self):
        # Execute a SQL query to get a random question
        cursor.execute("SELECT question FROM questions ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        if result:
            self.question_label.config(text=result[0])

# Run the GUI
if __name__ == "__main__":
    app = App()
    app.mainloop()
