import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    
    window.title(f"Open File: {filepath}")

def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return
    
    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content) 
    
    window.title(f"Save File: {filepath}")

def undo_text(text_edit):
    # Undo the last text editing operation
    text_edit.edit_undo()

def redo_text(text_edit):
    # Redo the last undone text editing operation
    text_edit.edit_redo()

def main(): 
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font="Arial 18", undo=True, wrap=tk.WORD)
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(frame, text="Open", command=lambda: open_file(window, text_edit))

    undo_button = tk.Button(frame, text="Undo", command=lambda: undo_text(text_edit))
    redo_button = tk.Button(frame, text="Redo", command=lambda: redo_text(text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")

    undo_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    redo_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

    frame.grid(row=0, column=0, sticky="ns")

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))

    window.mainloop()

main()
