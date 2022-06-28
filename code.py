import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

bg = '#183642'
fg = '#ECE6DB'

root = Tk()
root.geometry('1000x400')
root.configure(bg=bg)
root.resizable(False, False)
img = PhotoImage(file="Assets/favicon.png")
root.iconphoto(False, img)


heading = Label(root, text='Dictionary', bg=bg, fg=fg, font=(
    'Helvetica', 18, 'bold')).place(x=447, y=15)

word = ttk.Entry(root, width=156)
word.place(x=30, y=56)

output = Text(root, width=117, height=15)
output.place(x=30, y=80)
output.config(state='disabled')


def findDefinition():
    try:
        full_definition = ''
        response = requests.get(
            str('https://api.dictionaryapi.dev/api/v2/entries/en/' + word.get()))
        response = response.json()

        full_definition += word.get()
        full_definition += '''

Definitions:'''

        for i in range(len(response[0].get('meanings')[0].get('definitions'))):
            full_definition += '''
----------------------------------
Definition {}: {}
Synonym of this definition: {}
Antonym of this definition: {}
Example: {}'''.format(str(i+1), response[0].get('meanings')[0].get('definitions')[i].get('definition'), ', '.join(map(str, response[0].get('meanings')[0].get('definitions')[i].get('synonyms'))),  ', '.join(map(str, response[0].get('meanings')[0].get('definitions')[i].get('antonyms'))), response[0].get('meanings')[0].get('definitions')[i].get('example'))

        synonyms = '''


General Synonyms: '''
        synonyms += ', '.join(map(str,
                              response[0].get('meanings')[0].get('synonyms')))

        antonyms = '''
General antonyms: '''
        antonyms += ', '.join(map(str,
                              response[0].get('meanings')[0].get('antonyms')))

    except KeyError:
        messagebox.showerror(
            title='Error!', message='Uh oh! This word does not exist!')

    full_definition += synonyms
    full_definition += antonyms
    output.config(state='normal')
    output.delete(1.0, 'end')
    output.insert('end', full_definition)
    output.config(state='disabled')


find = Button(root, text='Find meaning', font=(
    'Helvetica', 10, 'bold'), height=3, width=14, command=findDefinition, bg='#334e58', fg=fg)
find.place(x=447, y=330)

root.title('Dictionary')
root.mainloop()
