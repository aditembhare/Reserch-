import tkinter as tk
from tkinter import ttk
from collections import defaultdict

# --- Data: 50 companies with multiple ratings ---
feedback = [
    ("Google", 5), ("Google", 5), ("Google", 4), ("Google", 5),
    ("Apple", 5), ("Apple", 5), ("Apple", 4), ("Apple", 5),
    ("Microsoft", 5), ("Microsoft", 4), ("Microsoft", 5), ("Microsoft", 5),
    ("Amazon", 5), ("Amazon", 4), ("Amazon", 5), ("Amazon", 5),
    ("Facebook", 4), ("Facebook", 4), ("Facebook", 4), ("Facebook", 5),
    ("Tesla", 5), ("Tesla", 4), ("Tesla", 5),
    ("Netflix", 5), ("Netflix", 5), ("Netflix", 4),
    ("NVIDIA", 5), ("NVIDIA", 5), ("NVIDIA", 4),
    ("Salesforce", 5), ("Salesforce", 4), ("Salesforce", 5),
    ("Adobe", 5), ("Adobe", 4), ("Adobe", 4),
    ("Intel", 4), ("Intel", 4), ("Intel", 3),
    ("Cisco", 4), ("Cisco", 3), ("Cisco", 4),
    ("Oracle", 4), ("Oracle", 3), ("Oracle", 4),
    ("IBM", 3), ("IBM", 3), ("IBM", 2),
    ("Accenture", 3), ("Accenture", 3), ("Accenture", 2),
    ("Infosys", 3), ("Infosys", 2), ("Infosys", 3),
    ("TCS", 2), ("TCS", 2), ("TCS", 3),
    ("Wipro", 2), ("Wipro", 2), ("Wipro", 1),
    ("Dell", 2), ("Dell", 1), ("Dell", 2),
    ("HP", 2), ("HP", 2), ("HP", 1),
    ("Snapchat", 3), ("Snapchat", 2), ("Snapchat", 3),
    ("Spotify", 3), ("Spotify", 4), ("Spotify", 3),
    ("Uber", 2), ("Uber", 2), ("Uber", 3),
    ("Lyft", 2), ("Lyft", 2), ("Lyft", 1),
    ("Dropbox", 3), ("Dropbox", 3), ("Dropbox", 2),
    ("Zoom", 4), ("Zoom", 3), ("Zoom", 4)
]

# --- Process Feedback ---
feedback_map = defaultdict(list)
for company, rating in feedback:
    feedback_map[company].append(rating)

companies = [
    (company, sum(ratings) / len(ratings))
    for company, ratings in feedback_map.items()
]

# Sort companies by average rating (descending)
companies.sort(key=lambda x: x[1], reverse=True)

# --- Tkinter UI ---
def show_companies():
    """Display all companies and their average ratings."""
    for row in companies:
        tree.insert("", "end", values=(row[0], f"{row[1]:.2f}"))

# Main Window
root = tk.Tk()
root.title("Company Ratings")
root.geometry("500x550")
root.configure(bg="#f5f5f5")

# Heading Label
label = tk.Label(
    root,
    text="Companies Sorted by Average Rating (Best to Worst)",
    font=("Arial", 12, "bold"),
    bg="#f5f5f5"
)
label.pack(pady=10)

# Table (Treeview)
columns = ("Company", "Average Rating")
tree = ttk.Treeview(root, columns=columns, show="headings", height=20)

# Define column headings
tree.heading("Company", text="Company")
tree.heading("Average Rating", text="Average Rating")

# Adjust column widths and alignment
tree.column("Company", width=250, anchor="center")
tree.column("Average Rating", width=150, anchor="center")

# Add scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

tree.pack(pady=10, padx=20, fill="both", expand=True)

# Populate the table
show_companies()

# Run the main loop
root.mainloop()
