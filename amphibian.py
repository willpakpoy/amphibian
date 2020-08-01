import json
import tkinter as tk

store_name = 'store.json' # we define a global variable with the file name so that we can easily change it if we need to
default_padding = 10
window = tk.Tk()
window.title('Amphibian')

def singleQuestion(path): # this is what will display when we want to ask a question
    with open(store_name, 'r') as f: # code below will only run when we open the file, as f
        default_datastore = json.loads(f.read()) # load data from the json array
        item = [d for d in default_datastore if d['pathId'] == path][0] # select an item from the array that has the 'pathId' attribute being set to the 'path' argument
        label = tk.Label(text=item['preSelection']) # create a label to be displayed in the window
        label.pack(padx=default_padding, pady=default_padding)
        print(item['postSelection'])
        options_wrap = tk.Frame(master=window)
        for option in item['options']:
            option_list_item = [d for d in default_datastore if d['pathId'] == option][0]
            option_label = tk.Button(master=options_wrap, text=option_list_item['preSelection'])
            option_label.pack(side=tk.LEFT, fill=tk.BOTH)
        options_wrap.pack(padx=default_padding, pady=default_padding)
        window.mainloop()

    print('hello!')

singleQuestion(1)