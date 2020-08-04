import json
import tkinter as tk
from functools import partial

store_name = 'store.json' # we define a global variable with the file name so that we can easily change it if we need to
default_padding = 12.5
window = tk.Tk()
window.title('Amphibian')

def clearWindow():
    for widget in window.winfo_children():
        widget.destroy()

def singleQuestion(path): # this is what will display when we want to ask a question
    with open(store_name, 'r') as f: # code below will only run when we open the file, as f
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
        question_wrap.pack()
        window.mainloop()
        
def closeThisSingleQuestion(option):
        clearWindow()
        singleQuestion(option)
singleQuestion(1)
