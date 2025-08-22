import tkinter as tk
import os
from asyncio import tasks
from datetime import datetime
from pathlib import Path
documents_folder = os.path.join(Path.home(), "Documents")

def add_task():
    text = input_field.get()
    if text.strip():
        var = tk.BooleanVar()
        cb = tk.Checkbutton(root, text=text, variable=var, font=("Arial", 12))
        cb.pack(anchor="w")
        tasks.append((text, var))
        input_field.delete(0, tk.END)

def save_tasks():
    documents_folder = os.path.join(Path.home(), "Documents")
    file_path = os.path.join(documents_folder, "tasks_log.txt")
    os.makedirs(documents_folder, exist_ok=True)

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"\n{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - Daily tasks:\n")
        for txt, v in tasks:
            mark = "✔" if v.get() else "✘"
            file.write(f"{txt} {mark}\n")

    status_label.config(text=f"✅ A fájl elementve ide: {file_path}")

root = tk.Tk()
root.title("📅 Napi feladatok")
date_label = tk.Label(root, text=datetime.now().strftime("%Y. %B %d. (%A)"), font=("Arial", 14, "bold"))
date_label.pack(pady=10)
input_field = tk.Entry(root, font=("Arial", 12), width=40)
input_field.pack(pady=5)
add_button = tk.Button(root, text="➕ Feladat hozzáadása", command=add_task, font=("Arial", 12))
add_button.pack(pady=5)
tasks = []
save_button = tk.Button(root, text="💾 Mentés", command=save_tasks, font=("Arial", 12))
save_button.pack(pady=5)
status_label = tk.Label(root, text="", fg="green", font=("Arial", 11))
status_label.pack()
root.mainloop()