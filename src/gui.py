import tkinter as tk
import tkinter.font as tkFont
from analyser import Analyser


class App:
    def __init__(self, root):
        root.title("Stash finder coordinates analyser")
        width = 383
        height = 319
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        submit_button = tk.Button(root)
        submit_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=12)
        submit_button["font"] = ft
        submit_button["fg"] = "#000000"
        submit_button["justify"] = "center"
        submit_button["text"] = "Open scatter plot of cords"
        submit_button.place(x=80, y=260, width=150, height=25)
        submit_button["command"] = self.button_pressed

        chests_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        chests_label["font"] = ft
        chests_label["fg"] = "#333333"
        chests_label["justify"] = "left"
        chests_label["text"] = "Minimum number of chests"
        chests_label.place(x=10, y=40, width=160, height=25)

        self.chest_entry = tk.Entry(root)
        self.chest_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.chest_entry["font"] = ft
        self.chest_entry["fg"] = "#333333"
        self.chest_entry["justify"] = "center"
        self.chest_entry.place(x=230, y=40, width=70, height=25)

        self.shulk_entry = tk.Entry(root)
        self.shulk_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.shulk_entry["font"] = ft
        self.shulk_entry["fg"] = "#333333"
        self.shulk_entry["justify"] = "center"
        self.shulk_entry.place(x=230, y=100, width=70, height=25)

        self.minecart_entry = tk.Entry(root)
        self.minecart_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.minecart_entry["font"] = ft
        self.minecart_entry["fg"] = "#333333"
        self.minecart_entry["justify"] = "center"
        self.minecart_entry.place(x=230, y=160, width=70, height=25)

        shulk_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        shulk_label["font"] = ft
        shulk_label["fg"] = "#333333"
        shulk_label["justify"] = "left"
        shulk_label["text"] = "Minimum number of shulkers"
        shulk_label.place(x=10, y=100, width=160, height=25)

        minecarts_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        minecarts_label["font"] = ft
        minecarts_label["fg"] = "#333333"
        minecarts_label["justify"] = "left"
        minecarts_label["text"] = "Minimum number of minecarts"
        minecarts_label.place(x=10, y=160, width=160, height=25)

        self.file_path_entry = tk.Entry(root)
        self.file_path_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=12)
        self.file_path_entry["font"] = ft
        self.file_path_entry["fg"] = "#333333"
        self.file_path_entry["justify"] = "center"
        self.file_path_entry.place(x=200, y=200, width=170, height=25)


        file_path_label = tk.Label(root)
        ft = tkFont.Font(family='Times', size=12)
        file_path_label["font"] = ft
        file_path_label["fg"] = "#333333"
        file_path_label["justify"] = "left"
        file_path_label["text"] = "File Path"
        file_path_label.place(x=10, y=200, width=160, height=25)

        self.minecart_entry.insert(-1, 0)
        self.chest_entry.insert(-1, 0)
        self.shulk_entry.insert(-1, 0)
        self.file_path_entry.insert(-1, "stashFinder.csv")

    def button_pressed(self):
        print("Analysing...")
        analyser = Analyser(csv_path=self.file_path_entry.get(),
                            min_minecratrs=int(self.minecart_entry.get()),
                            min_chests=int(self.chest_entry.get()),
                            min_shulkers=int(self.shulk_entry.get()))
        analyser.show_plot()
