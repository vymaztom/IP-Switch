import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from copy import *
from time import *
import threading
import time


class cmd:

    def __init__(self, master, net):
        self.frame = tk.Frame(master)
        self.net = net
        # define scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill="y", expand=False)

        # define text
        self.text = tk.Text(self.frame, wrap=tk.WORD, yscrollcommand=self.scrollbar.set, width=68, height=23, bg='black',
                            fg="white")
        self.text.pack()
        self.text.config(state=tk.DISABLED)
        self.text.yview('end')

        self.scrollbar.config(command=self.text.yview)

    def place(self, x, y):
        self.frame.place(x=x, y=y)

    def text_add(self, text):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END, str(text) + "\n")
        self.text.config(state=tk.DISABLED)
        self.text.yview('end')

class table:

    def __init__(self, master, net):
        self.master = master
        self.net = net

        self.frame = tk.Frame(master)
        self.table = tk.Frame(self.frame)
        self.table.grid(row=0, column=0)

        self.data = ["Name", "interface", "IP", "Mask", "Gate"]
        self.create_table()

    def place(self, x, y):
        self.frame.place(x=x, y=y)

    def create_table(self):
        head = ["interface", "IP", "Mask", "Gate"]

        for line in range(len(head)):
            if line == 0:
                tk.Label(self.table, text=head[line], highlightthickness=1, width=30, bg="gray")\
                    .grid(row=0, column=line, sticky=tk.W, ipady=2, ipadx=5)
            else:
                tk.Label(self.table, text=head[line], highlightthickness=1, width=15, bg="gray")\
                    .grid(row=0, column=line, sticky=tk.W, ipady=2, ipadx=5)
        self.net.get_parameters()


        cRoll = 1
        for interface in self.net.l_interface:
            color = "white"
            if cRoll%2 == 0:
                color = "light gray"
            else:
                color = "white"
            tk.Label(self.table, text=interface, highlightthickness=1, width=30, bg=color)\
                .grid(row=copy(cRoll), column=0, sticky=tk.W, ipady=2, ipadx=5)
            tk.Label(self.table, text=self.net.d_ip[interface], highlightthickness=1, width=15, bg=color)\
                .grid(row=copy(cRoll), column=1, sticky=tk.W, ipady=2, ipadx=5)
            tk.Label(self.table, text=self.net.d_mask[interface], highlightthickness=1, width=15, bg=color)\
                .grid(row=copy(cRoll), column=2, sticky=tk.W, ipady=2, ipadx=5)
            tk.Label(self.table, text=self.net.d_gate[interface], highlightthickness=1, width=15, bg=color)\
                .grid(row=copy(cRoll), column=3, sticky=tk.W, ipady=2, ipadx=5)
            cRoll += 1

    def refresh(self):
        self.net.get_parameters()

class menu(tk.Menu):

    def __init__(self, master, data, net, tree):
        tk.Menu.__init__(self, master)
        self.master = master
        self.data = data
        self.net = net
        self.tree = tree

        # define menu
        self.add_command(label="Add", command=self.action_add)
        self.add_command(label="Remove", command=self.action_remove)
        self.add_command(label="About ..", command=self.action_about)

        # active
        self.master.config(menu=self)

    def action_add(self):
        self.add_win = tk.Tk()
        self.add_win.title("Add")
        #self.add_win.iconbitmap("icon.ico")

        # define componets
        label_name = tk.Label(self.add_win, text = "Name of configuration:")
        label_interface = tk.Label(self.add_win, text = "Name of interface:")
        label_ip = tk.Label(self.add_win, text = "IP address:")
        label_mask = tk.Label(self.add_win, text = "Defautl Mask:")
        label_gate = tk.Label(self.add_win, text = "Defautl Gateway:")

        self.add_entry_name = tk.Entry(self.add_win, bd = 0, width = 35)
        self.add_entry_interface = tk.Entry(self.add_win, bd = 0, width = 35)

        self.add_entry_ip = tk.Entry(self.add_win, bd = 0, width = 20)
        self.add_entry_mask = tk.Entry(self.add_win, bd = 0, width = 20)
        self.add_entry_gate = tk.Entry(self.add_win, bd = 0, width = 20)

        button_save = tk.Button(self.add_win, text = "Save", command = self.action_add_send)

        # define entry componets
        label_name.place(x= 10 , y = 10)
        label_interface.place(x = 10, y = 30)
        label_ip.place(x = 10, y = 50)
        label_mask.place(x = 10, y = 70)
        label_gate.place(x = 10, y = 90)


        self.add_entry_name.place(x = 170, y = 10)
        self.add_entry_interface.place(x = 170, y = 30)
        self.add_entry_ip.place(x = 170, y = 50)
        self.add_entry_mask.place(x = 170, y = 70)
        self.add_entry_gate.place(x = 170, y = 90)

        button_save.place(x = 330, y = 115)

        # active win
        self.add_win.geometry("400x150+10+10")
        self.add_win.mainloop()

    def action_remove(self):
        self.delete_win = tk.Tk()
        self.delete_win.title("Remove")
        #self.delete_win.iconbitmap("icon.ico")

        # define componets
        label_name = tk.Label(self.delete_win, text = "Name of configuration:")
        self.delete_entry_name = tk.Entry(self.delete_win, bd = 0, width = 35)
        button_delete = tk.Button(self.delete_win, text = "Remove", command = self.action_remove_send)

        # entry componets
        label_name.place(x = 10, y = 10)
        self.delete_entry_name.place(x = 170, y = 10)
        button_delete.place(x = 170, y = 50)
        # active win
        self.delete_win.geometry("400x100+10+10")
        self.delete_win.mainloop()

    def action_about(self):
        self.about_win = tk.Tk()
        self.about_win.title("About ..")
        #self.about_win.iconbitmap("icon.ico")

        scrollbar = tk.Scrollbar(self.about_win)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text = tk.Text(self.about_win, wrap=tk.WORD, yscrollcommand=scrollbar.set)
        text.insert(tk.END,"    Welcome to IP Switch\n\n")
        text.insert(tk.END,"The program is designed to make\n")
        text.insert(tk.END,"switching between network settings easier.\n\n")
        text.insert(tk.END,"The program is completely free, if you want to program yourself for\n\n")
        text.insert(tk.END,"yourself, write me to email vymaztom@fel.cvut.cz and\n")
        text.insert(tk.END," I would like to give you a whole project.\n\n")
        text.insert(tk.END,"The entire program is written in Python and compiled using py2exe")
        text.config(state=tk.DISABLED)
        text.pack()

        scrollbar.config(command=text.yview)
        self.about_win.geometry("450x300+10+10")
        self.about_win.mainloop()

    def action_add_send(self):
        name = self.add_entry_name.get()
        interface = self.add_entry_interface.get()
        ip = self.add_entry_ip.get()
        mask = self.add_entry_mask.get()
        gate = self.add_entry_gate.get()
        if self.test_of_add(name, ip, mask, gate):
            self.tree.add(name, interface, ip, mask, gate)
            self.data.add_data(name, ip, interface, mask, gate)
            self.add_win.quit()
            self.add_win.destroy()

    def action_remove_send(self):
        name = str(self.delete_entry_name.get())
        if self.test_of_remove(name):
            self.tree.remove(name)
            self.delete_win.quit()
            self.delete_win.destroy()
        else:
            messagebox.showinfo("ERROR", "Invalide name")

    def test_of_add(self, name, ip, mask, gate):
        if self.data.list_of_name.__contains__(name):
            messagebox.showinfo("ERROR", "Invalide NAME")
            return 0
        data_ip = ip.split(".")
        data_mask = mask.split(".")
        data_gate = gate.split(".")
        if not len(data_ip) == 4:
            messagebox.showinfo("ERROR", "Invalide len of ip")
            return 0
        if not len(data_mask) == 4:
            messagebox.showinfo("ERROR", "Invalide len of mask")
            return 0
        if not len(data_gate) == 4:
            messagebox.showinfo("ERROR", "Invalide len of gate")
            return 0
        if int(data_ip[0]) > 255 and int(data_ip[1]) > 255 and int(data_ip[2]) > 255 and int(data_ip[3]) > 255:
            messagebox.showinfo("ERROR", "IP values > 255")
            return 0
        if int(data_mask[0]) > 255 and int(data_mask[1]) > 255 and int(data_mask[2]) > 255 and int(data_mask[3]) > 255:
            messagebox.showinfo("ERROR", "MASK values > 255")
            return 0
        if int(data_gate[0]) > 255 and int(data_gate[1]) > 255 and int(data_gate[2]) > 255 and int(data_gate[3]) > 255:
            messagebox.showinfo("ERROR", "GATE values > 255")
            return 0
        return 1

    def test_of_remove(self, name):
        if self.data.list_of_name.__contains__(name):
            return 1
        return 0


class stoptime(threading.Thread):

    def __init__(self, threadID, name, counter, master):
        self.master = master

        self.frame = tk.Frame(master)
        self.table = tk.Frame(self.frame)
        self.table.grid(row=0, column=0)
        self.act = True
        self.t = "none"
        self.text = tk.Label(self.table, text=self.text).grid(row=0, column=0)

    def run(self):
        while self.act:
            self.t = strftime('%X')
            time.sleep(1)




    def place(self,x,y):
        self.frame.place(x=x, y=y)

    def create_time(self):
        pass

class tree:

    def __init__(self, master, data, net, cmd, table):
        self.master = master
        self.data = data
        self.net = net
        self.cmd = cmd
        self.table = table
        self.frame = tk.Frame(master)

        # define scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill="y", expand=False)

        # define tree
        self.tree = ttk.Treeview(self.frame, yscrollcommand=self.scrollbar.set, selectmode="extended", height="8")
        self.tree.pack()

        self.scrollbar.config(command=self.tree.yview)
        self.create_tree()
        self.load_data()

    def create_tree(self):
        self.iterator = 0
        self.name_index = {}
        self.index_name = {}
        self.tree["columns"] = ("Interface", "IP", "Mask", "Gate")

        self.tree.column("#0", width=150, stretch=tk.YES)
        self.tree.column("#1", width=150, stretch=tk.YES)
        self.tree.column("#2", width=90)
        self.tree.column("#3", width=90)
        self.tree.column("#4", width=90)

        self.tree.heading("#0", text="Name")
        self.tree.heading("#1", text="Interface")
        self.tree.heading("#2", text="IP")
        self.tree.heading("#3", text="Mask")
        self.tree.heading("#4", text="Gate")

        self.tree.bind('<ButtonRelease-1>', self.action_select)

    def place(self, x, y):
        self.frame.place(x=x, y=y)

    def add(self, name, interface, ip, mask, gate):
        one = self.tree.insert('', str(self.iterator), text=str(name), values=(str(interface), str(ip), str(mask), str(gate)))
        if self.iterator == 0:
            self.tree.focus("I001")
        self.iterator += 1
        self.name_index[str(name)] = str(copy(one))
        self.index_name[str(copy(one))] = str(name)

    def remove(self, name):
        self.tree.delete(self.name_index[str(name)])
        self.index_name.__delitem__(self.name_index[str(name)])
        self.name_index.__delitem__(str(name))
        self.data.delete_data(name)

    def load_data(self):
        for name in self.data.list_of_name:
            self.add(name,\
                     self.data.dictioary_of_interface[name],\
                     self.data.dictioary_of_ip[name],\
                     self.data.dictioary_of_mask[name],\
                     self.data.dictioary_of_gate[name],)

    def action_select(self, arg):
        name = self.index_name[self.tree.focus()]
        print(name)
        interface = self.data.dictioary_of_interface[name]
        ip = self.data.dictioary_of_ip[name]
        mask = self.data.dictioary_of_mask[name]
        gate = self.data.dictioary_of_gate[name]
        text = self.net.set_configuratin(interface, ip, mask, gate)
        self.cmd.text_add(text)
        self.table.refresh()

class GUI:

    def __init__(self, data, net):
        self.win = tk.Tk()
        self.win.title("IP Switch")
        #  ... add icon

        self.data = data
        self.net = net


        self.cmd = cmd(self.win, self.net)
        self.table = table(self.win, self.net)
        self.tree = tree(self.win, self.data, self.net, self.cmd, self.table)
        self.menu = menu(self.win, self.data, self.net, self.tree)

        self.time = stoptime(0,"time",10,self.win)

        self.cmd.place(630,10)
        self.table.place(10,10)
        self.tree.place(10,195)
        self.time.place(10,195)

        self.win.geometry("1200x400")
        self.win.mainloop()

if __name__ == "__main__":
    root = GUI(None, None)
