import json
import tkinter as tk
from functools import partial
import getpass
from datetime import datetime
from tksheet import Sheet

animal_database = 'paths.json' # we define a global variable with the file name so that we can easily change it if we need to
recent_selections_database = 'store.json'
default_padding = 12.5
window = tk.Tk()
window.title('Amphibian')

def clearWindow():
    for widget in window.winfo_children():
        widget.destroy()

def singleQuestion(path): # this is what will display when we want to ask a question
    clearWindow()
    with open(animal_database, 'r') as f: # code below will only run when we open the file, as f
        question_wrap = tk.Frame(master=window)
        default_datastore = json.loads(f.read()) # load data from the json array
        item = [d for d in default_datastore if d['pathId'] == path][0] # select an item from the array that has the 'pathId' attribute being set to the 'path' argument
        label = tk.Label(text=item['postSelection'], master=question_wrap) # create a label to be displayed in the window
        label.pack(padx=default_padding, pady=default_padding) # pack the label
        if item['type'] == 'continuation':
            options_wrap = tk.Frame(master=question_wrap) # wrap the options in a frame
            for option in item['options']: # this is the loop where we make the buttons
                option_list_item = [d for d in default_datastore if d['pathId'] == option][0] # we get the path from the json file 
                option_button = tk.Button(master=options_wrap, text=option_list_item['preSelection'], command=partial(closeThisSingleQuestion, option))
                option_button.pack(side=tk.LEFT, fill=tk.BOTH)
            options_wrap.pack(padx=default_padding, pady=default_padding)
        elif item['type'] == 'completion':
            saveAnimalType(item['postSelection'])
            return_button = tk.Button(master=question_wrap, text="Return to home", command=lambda : home())
            return_button.pack()
        question_wrap.pack()
        window.mainloop()
        
def closeThisSingleQuestion(option):
        singleQuestion(option)


def saveAnimalType(postSelection):
    with open(recent_selections_database, 'r+') as f:
        now = datetime.now()
        new = {
            "text": postSelection,
            "user": getpass.getuser(),
            "time": now.strftime("%d %b %Y %H:%M:%S")
        }
        selections = json.load(f)
        selections.append(new)
        f.seek(0)
        json.dump(selections, f)

def previousSelections():
    clearWindow()
    with open(recent_selections_database, 'r') as f:
        selections = json.load(f)
        text_text = tk.Label(text="Result", font="bold")
        user_text = tk.Label(text="User", font="bold")
        time_text = tk.Label(text="Datetime", font="bold")

        text_text.grid(row=0, column=1, pady=default_padding, padx=default_padding)
        user_text.grid(row=0, column=2, pady=default_padding, padx=default_padding)
        time_text.grid(row=0, column=3, pady=default_padding, padx=default_padding)
        i = 0
        while i < len(selections):
            item = selections[i]
            print(item)
            text_text = tk.Label(text=item["text"])
            user_text = tk.Label(text=item["user"])
            time_text = tk.Label(text=item["time"])

            text_text.grid(row=i+1, column=1, pady=default_padding, padx=default_padding)
            user_text.grid(row=i+1, column=2, pady=default_padding, padx=default_padding)
            time_text.grid(row=i+1, column=3, pady=default_padding, padx=default_padding)

            i += 1

        back_button = tk.Button(text="Back", command= lambda : home())
        back_button.grid(row=0, column=4, pady=default_padding, padx=default_padding)
        sheet = Sheet(window, data=selections)
        sheet.pack()
        window.mainloop()

def home():
    clearWindow()
    title = tk.Label(text="Amphibian")
    title.pack(padx=default_padding, pady=default_padding)

    buttons_wrap = tk.Frame()
    start_button = tk.Button(master=buttons_wrap, text="Start", command=lambda : singleQuestion(1))
    start_button.pack(side=tk.LEFT, fill=tk.BOTH)
    view_button = tk.Button(master=buttons_wrap, text="View previous results", command=lambda : previousSelections())
    view_button.pack(side=tk.LEFT, fill=tk.BOTH)
    buttons_wrap.pack(padx=default_padding, pady=default_padding)
    window.mainloop()

home()