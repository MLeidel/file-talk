'''
code file: filetalkgui.py

Requires:
    espeak-ng
      see: https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md
    ffmpeg
      see: https://ffmpeg.org/download.html
    pdftotext (poppler-utils)
      see: https://poppler.freedesktop.org/

Inputs a text, word, or pdf file outputs speech, wav file, or text file.
'''
import os, sys
import subprocess
import docx
import signal
from tkinter.font import Font
from ttkbootstrap import *
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from tkinter import filedialog
from tkinter import messagebox

class Application(Frame):
    ''' main class docstring '''
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=True, padx=4, pady=4)
        self.create_widgets()

    def create_widgets(self):
        ''' creates GUI for app '''

        vpad = 10
        hpad = 6
        lblpad = 16
        btnStyle = "outline"
        self.clean_text = ""  # holds text to be sent to espeak


        frm1 = Frame(self)
        frm1.grid(row=1, column=1, sticky='n', pady=vpad, padx=hpad)

        frm2 = Frame(self)
        frm2.grid(row=1, column=2, sticky='n', pady=vpad, padx=hpad)
        
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

        self.vcbx_mp3 = IntVar()
        cbx_mp3 = Checkbutton(self, variable=self.vcbx_mp3,
                              text='mp3', width=8,
                              bootstyle='round-toggle')
        cbx_mp3.grid(row=6, column=1, sticky='es', pady=lblpad)
        ToolTip(cbx_mp3, "Create an additional mp3 version file")

        self.vcbx_txt = IntVar()
        cbx_txt = Checkbutton(self, variable=self.vcbx_txt,
                              text='text', width=8,
                              bootstyle='round-toggle')
        cbx_txt.grid(row=7, column=1, sticky='es', pady=(0, 10))
        ToolTip(cbx_txt, "Create an additional text version file")

        # frm2
        self.vent_file_in = StringVar()
        ent_file_in = Entry(frm2, textvariable=self.vent_file_in, width=40)
        ent_file_in.grid(row=1, column=1, sticky='w', pady=vpad)
        ToolTip(ent_file_in, text="Select .pdf or .docx or .txt file")

        self.vent_file_out = StringVar()
        ent_file_out = Entry(frm2, textvariable=self.vent_file_out, width=40)
        ent_file_out.grid(row=2, column=1, sticky='w', pady=vpad)
        ToolTip(ent_file_out, text="Select path, and file without extention")

        self.vent_voice = StringVar()
        ent_voice = Entry(frm2, textvariable=self.vent_voice)
        ent_voice.grid(row=3, column=1, sticky='w', pady=vpad)
        self.vent_voice.set("en-us")

        self.vspn_speed = StringVar(value=150)
        spn_speed = Spinbox(frm2, textvariable=self.vspn_speed,
                            from_=30, to=300,
                            width=6)
        spn_speed.grid(row=4, column=1, sticky='w', pady=vpad)
        ToolTip(spn_speed, "30 - 300 Default 150")

        self.vspn_pitch = StringVar(value=45)
        spn_pitch = Spinbox(frm2, textvariable=self.vspn_pitch,
                            from_=0, to=99,
                            width=6)
        spn_pitch.grid(row=5, column=1, sticky='w', pady=vpad)
        ToolTip(spn_pitch, "0 - 99 Default 45")

        btn_create = Button(frm2, text='Create', command=self.btn_create_click,
                            width=20,
                            bootstyle=btnStyle)
        btn_create.grid(row=6, column=1, sticky='', pady=vpad)
        ToolTip(btn_create, text="Create wav file from selected input file")

        self.btn_speak = Button(frm2, text='Speak', command=self.btn_speak_click,
                            width=20,
                            bootstyle=btnStyle)
        self.btn_speak.grid(row=7, column=1, sticky='', pady=vpad)
        ToolTip(self.btn_speak, text="Speak the text from selected input file")

        btn_close = Button(frm2, text='Close', command=self.btn_close_click,
                            width=20,
                            bootstyle=btnStyle)
        btn_close.grid(row=9, column=1, sticky='', pady=vpad)

    #-----------------------------------------------

    def readFileIntoText(self, infile):
        ''' converts input into one text string: clean_text '''
        self.clean_text = ""
        if infile.lower().endswith(".pdf"):
            try:
                text = subprocess.check_output(['pdftotext',
                                               infile,
                                               '-'])
                self.clean_text = text.decode()
            except Exception as e:
                raise e
        elif infile.lower().endswith(".docx"):
            doc = docx.Document(infile)
            for paragraph in doc.paragraphs:
                self.clean_text += paragraph.text
        else: # assuming here it is a plain text file
            if infile.lower().endswith(".txt"):
                self.clean_text = open(infile).read()
            else:
                if messagebox.askokcancel('Warning', 'Assume Input Is Plain Text'):
                    self.clean_text = open(infile).read()

        # an optional output text file
        if self.vcbx_txt.get() == 1:  # user checked "text" toggle
            outFile = self.vent_file_out.get()
            if outFile == "":
                messagebox.showerror('Error',
                                     "Output file name is missing")
                return
            with open(outFile+".txt", "w") as fout:
                fout.write(self.clean_text)
            #messagebox.showinfo('Created File', outFile+".txt")

    def btn_file_in_click(self):
        ''' prompt user for document to speak '''
        filename = filedialog.askopenfilename(initialdir='/home',
                    title = 'Open file',
                    filetypes = (('all files', '*.*'),
                                 ('pdf files', '*.pdf'),
                                 ('docx files', '*.docx'),
                                 ('text files', '*.txt'))
                    )
        if len(filename) > 1:  # user did enter something
            if filename.lower().endswith(".pdf") or \
                filename.lower().endswith(".docx") or \
                filename.lower().endswith(".txt"):
                    self.vent_file_in.set(filename)
            else:
                if messagebox.askokcancel('Warning', 'Assume Input Is Plain Text'):
                    self.vent_file_in.set(filename)


    def btn_file_out_click(self):
        ''' prompt user for output file to create '''
        filename = filedialog.asksaveasfilename(initialdir='/home',
                    title = 'Output file',
                    filetypes = (('files', '*'),)
                    )
        if len(filename) > 1:
            self.vent_file_out.set(filename)


    def btn_create_click(self):
        ''' create output wav/mp3 file '''
        inFile = self.vent_file_in.get()
        outFile = self.vent_file_out.get()
        voice = self.vent_voice.get()
        speed = self.vspn_speed.get()
        pitch = self.vspn_pitch.get()
        self.readFileIntoText(inFile)  # set clean_text

        # text file output only then return
        # other options ignored
        if outFile.lower().endswith(".txt"):
            with open(outFile, "w") as fout:
                fout.write(self.clean_text)
            messagebox.showinfo('Created Text File', outFile)
            return

        # create speech audio file from clean_text
        try:
            subprocess.call(["espeak-ng", "-v"+voice, "-p"+pitch,
                            "-s"+speed, "-w"+outFile+".wav", self.clean_text])
            messagebox.showinfo('Created WAV File', outFile+".wav")
        except Exception as e:
            messagebox.showerror('Error',
                "subprocess for espeak returned an error")
            raise e

        # process an optional mp3 output file
        if self.vcbx_mp3.get() == 1:  # user checked mp3 toggle
            try:
                subprocess.call(["ffmpeg", "-i",
                                outFile+".wav",
                                outFile+".mp3"])
                messagebox.showinfo('Created Output File', outFile+".mp3")
            except Exception as e:
                messagebox.showerror('Error',
                    "subprocess for ffmpeg returned an error")
                raise e


    def btn_speak_click(self):
        ''' speak clean_text '''
        btntxt = self.btn_speak.cget('text')
        if btntxt != "Speak":
            self.btn_speak.config(text="Speak", bootstyle="default-outline")
            self.proc.send_signal(signal.SIGINT)  # quit the subprocess
            return
        else:
            self.btn_speak.config(text="STOP", bootstyle="warning")
        inFile = self.vent_file_in.get()
        voice = self.vent_voice.get()
        speed = self.vspn_speed.get()
        pitch = self.vspn_pitch.get()
        self.readFileIntoText(inFile)  # set clean_text
        try:
            self.proc = subprocess.Popen(["espeak-ng", "-v"+voice, "-p"+pitch,
                                         "-s"+speed, self.clean_text])
        except Exception as e:
            messagebox.showerror('Error',
                "subprocess returned an error")
            raise e


    def btn_close_click(self):
        ''' Close the app and cancel voice if engaged '''
        try:
            self.proc.send_signal(signal.SIGINT)
        except Exception as e:
            pass

        root.destroy()


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
