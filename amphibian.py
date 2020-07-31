import json
import tkinter as tk

store_name = 'store.json' # we define a global variable with the file name so that we can easily change it if we need to

window = tk.Tk()
window.title('Amphibian')

def singleQuestion(path): # this is what will display when we want to ask a question
    with open(store_name, 'r') as f: # code below will only run when we open the file, as f
        default_datastore = json.loads(f.read()) # load data from the json array
        item = [d for d in default_datastore if d['pathId'] == path][0] # select an item from the array that has the 'pathId' attribute being set to the 'path' argument
        label = tk.Label(text=item['preSelection'])
        label.pack()

        window.mainloop()

        print(item['preSelection'])
    print('hello!')

singleQuestion(1)