   __ _ _            _        _ _    
  / _(_) | ___      | |_ __ _| | | __
 | |_| | |/ _ \_____| __/ _` | | |/ /
 |  _| | |  __/_____| || (_| | |   < 
 |_| |_|_|\___|      \__\__,_|_|_|\_\
                                     
Python 3.x
FileTalk
filetalk.py - terminal version
filetalkgui.py - GUI version

espeak-ng
  see: https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md
ffmpeg
  see: https://ffmpeg.org/download.html
pdftotext (poppler-utils)
  see: https://poppler.freedesktop.org/
       https://blog.alivate.com.au/poppler-windows/
       Ubuntu: sudo apt install poppler-utils

Inputs a text, word, or pdf file and outputs:
speech, audio file, or just text file.

special modules needed:

>pip install --pre python-docx  # for MS Word docs
>pip install argparse  # for command line help


filetalk.py - terminal version
------------------------------
usage: filetalk.py [-h] [-v VOICE] [-s SPEED] [-p PITCH] [-mp3] [-txt] infile outfile

Converts textual content from a PDF, Word, or Text file into speech, audo file, or
textfile. REQUIRES: "espeak-ng", "ffmpeg", and "pdftotext".

positional arguments:
  infile      input file: .txt, .pdf, or .docx only
  outfile     output file (no .ext) | "talk" | file.txt

options:
  -h, --help  show this help message and exit
  -v VOICE    espeak-ng voice code. Dft en-us
  -s SPEED    espeak-ng speed 30-300 Dft 150
  -p PITCH    espeak-ng pitch 0-99 Dft 45
  -mp3        make additional mp3 output file
  -txt        make additional text output file


filetalkgui.py - GUI version
----------------------------
Python modules may need to pip install:

    import docx
    ttkbootstrap
    tkinter
    argparse

