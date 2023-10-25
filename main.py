import csv
import tkinter as tk

#print(help(csv.DictReader))

print('start')

class Str:
    def strip_quotes(string:str)->str:
        if len(string) > 2 and string[0] == string[-1] and string[0] in '\'"':
            string = string[1:-1]
        return string

class Sheet:
    def __init__(self, file:str, fieldnames:list=None, dialect='excel', *args, **kwds):
        self.file = file
        self.fh = open(file, 'r')
        self._sheet_dict = {}
        self.fieldnames = None
        self.rows = []

        
        self.fieldnames = self.fh.readline().strip().split(',')
        for i in range(len(self.fieldnames)):
            name = self.fieldnames[i]
            name = Str.strip_quotes(name)
            self.fieldnames[i] = name

        for line in self.fh.readlines():
            lis = line.strip().split(',')
            lis = [Str.strip_quotes(x) for x in lis]

            self.rows.append(dict(zip(self.fieldnames, lis)))
            
        

    def column(self, name:str)->list:
        'returns: column under heading [name]'
        
    
    def row(self, n:int)->dict:
        'returns: row n'


    def rm_column(self, name:str)->list:
        'removes row and returns it'
        re = []
        self.fieldnames.remove(name)
        for i in range(len(self.rows)):
            re.append(self.rows[i].pop(name))
        return re
        

    def __len__(self):
        return len(self.rows)

    def __str__(self)->str:
        re = ''
        re = str(self.fieldnames)
        return re

class Wdg:
    'custom widgets'
    class Label(tk.Label):
        def __init__(self, parent, *args, **kwargs):
            super().__init__(parent, *args, **kwargs)
            self.parent = parent
            self.config(borderwidth=1, relief="solid")



class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        sheet = Sheet('csv91001.csv')
        sheet.rm_column('USD$')
        
        self.grid = GridDisplay(self, sheet)
        self.grid.pack(fill='both')

class GridDisplay(tk.Frame):
    class Header(tk.Frame):
        def __init__(self, parent, names:list, *args, **kwargs):
            super().__init__(parent, *args, **kwargs)
            self.parent = parent   
            self.names = names
            self.labels = []

            

            for i, name in enumerate(self.names):
                self.labels.append(Wdg.Label(self, text=name))
                self.labels[i].grid(column=i, row=0, sticky='nsew')
                self.grid_columnconfigure(i, minsize=100)
    
    class Content(tk.Frame):
        def __init__(self, parent, sheet:Sheet, *args, **kwargs):
            super().__init__(parent, *args, **kwargs)
            self.parent = parent 
            self.sheet = sheet
            

    def __init__(self, parent, sheet:Sheet, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)
        self.parent = parent
        self.sheet = sheet

        self.header = GridDisplay.Header(self, self.sheet.fieldnames)
        self.header.grid(column=0, row=0, sticky='nsew')
        
        label = Wdg.Label(self, text="Label")
        label.config(padx=5, pady=5)

        label.grid(column=0, row=1)

if __name__ == '__main__':
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    


    
