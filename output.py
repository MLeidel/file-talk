'''
code file:
date:
comments:
    tkauto generated
'''
import os, sys
from tkinter.font import Font
from ttkbootstrap import *
from ttkbootstrap.constants import *
# from tkinter import Listbox
# from tkinter import filedialog
# from tkinter import messagebox
# from tkinter import simpledialog
# import webbrowser
# from ttkbootstrap.tooltip import ToolTip
# from ttkbootstrap.dialogs import Querybox  # get_date, get_font ...
# from functools import partial # action_w_arg = partial(self.proc_btns, n)
# from time import gmtime, strftime

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''
        # expand widget to fill the grid
        # self.columnconfigure(1, weight=1, pad=100)
        # self.rowconfigure(1, weight=1, pad=20)

        # myfont = Font(family='Lucida Console', weight = 'bold', size = 20)

        ''' ONLY OPTIONS FOR 'grid' FUNCTIONS:
                column  row
                columnspan  rowspan
                ipadx and ipady
                padx and pady
                sticky="nsew"
        -------------------------------------------------------- '''
        vpad = 10
        hpad = 6
        lblpad = 16
        btnStyle = "outline"

        frm1 = Frame(self)
        frm1.grid(row=1, column=1, sticky='n', pady=vpad, padx=hpad)
        
        # lframe = LabelFrame(self, text="text",
        #                     width=100, height=100)
        # lframe.grid(row=1, column=1, sticky='nsew')
        #
        

        frm2 = Frame(self)
        frm2.grid(row=1, column=2, sticky='n', pady=vpad, padx=hpad)
        
        # lframe = LabelFrame(self, text="text",
        #                     width=100, height=100)
        # lframe.grid(row=1, column=1, sticky='nsew')
        #

        # frm1
        btn_file_in = Button(frm1, text='File In', bootstyle=btnStyle,
                             command=self.btn_file_in_click,
                             width=8)
        btn_file_in.grid(row=1, column=1, sticky='e', pady=vpad)

        btn_file_out = Button(frm1, text='File Out', bootstyle=btnStyle,
                              command=self.btn_file_out_click,
                              width=8)
        btn_file_out.grid(row=2, column=1, sticky='e', pady=vpad)

        lbl_voice = Label(frm1, text='voice code')
        lbl_voice.grid(row=3, column=1, sticky='es', pady=lblpad)

        lbl_speed = Label(frm1, text='Speed')
        lbl_speed.grid(row=4, column=1, sticky='es', pady=lblpad)

        lbl_pitch = Label(frm1, text='Pitch')
        lbl_pitch.grid(row=5, column=1, sticky='es', pady=lblpad)

        # frm2
        self.vent_file_in = StringVar()
        ent_file_in = Entry(frm2, textvariable=self.vent_file_in, width=40)
        ent_file_in.grid(row=1, column=1, sticky='w', pady=vpad)

        self.vent_file_out = StringVar()
        ent_file_out = Entry(frm2, textvariable=self.vent_file_out, width=40)
        ent_file_out.grid(row=2, column=1, sticky='w', pady=vpad)

        self.vent_voice = StringVar()
        ent_voice = Entry(frm2, textvariable=self.vent_voice)
        ent_voice.grid(row=3, column=1, sticky='w', pady=vpad)

        self.vspn_speed = IntVar(value=150)
        spn_speed = Spinbox(frm2, textvariable=self.vspn_speed,
                            from_=30, to=300,
                            width=6)
        spn_speed.grid(row=4, column=1, sticky='w', pady=vpad)

        self.vspn_pitch = IntVar(value=45)
        spn_pitch = Spinbox(frm2, textvariable=self.vspn_pitch,
                            from_=0, to=99,
                            width=6)
        spn_pitch.grid(row=5, column=1, sticky='w', pady=vpad)

        btn_create = Button(frm2, text='Create', command=self.btn_create_click,
                            width=20,
                            bootstyle=btnStyle)
        btn_create.grid(row=6, column=1, sticky='', pady=vpad)

        btn_speak = Button(frm2, text='Speak', command=self.btn_speak_click,
                            width=20,
                            bootstyle=btnStyle)
        btn_speak.grid(row=7, column=1, sticky='', pady=vpad)

        btn_close = Button(frm2, text='Close', command=self.btn_close_click,
                            width=20,
                            bootstyle=btnStyle)
        btn_close.grid(row=9, column=1, sticky='', pady=vpad)

    def btn_file_in_click(self):
        ''' prompt user for document to speak '''

    def btn_file_out_click(self):
        ''' docstring '''

    def btn_create_click(self):
        ''' docstring '''

    def btn_speak_click(self):
        ''' docstring '''

    def btn_close_click(self):
        ''' docstring '''
        root.destroy()


    # def eventHandler(self):
    #     pass

    # def eventHandler(self):
    #     pass
#


# change working directory to path for this file
p = os.path.realpath(__file__)
os.chdir(os.path.dirname(p))

# THEMES
# 'cosmo', 'flatly', 'litera', 'minty', 'lumen',
# 'sandstone', 'yeti', 'pulse', 'united', 'morph',
# 'journal', 'darkly', 'superhero', 'solar', 'cyborg',
# 'vapor', 'simplex', 'cerculean'
root = Window("FileTalkGUI", "solar")  # , size=(400, 400)

# root.protocol("WM_DELETE_WINDOW", save_location)  # UNCOMMENT TO SAVE GEOMETRY INFO
Sizegrip(root).place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')
root.resizable(0, 0) # no resize & removes maximize button
# root.overrideredirect(True) # removed window decorations
# root.iconphoto(False, PhotoImage(file='icon.png'))
# root.attributes("-topmost", True)  # Keep on top of other windows

Application(root)

root.mainloop()
