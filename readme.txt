
Python 3.x
FileTalk
filetalk.py - terminal version
filetalkgui.py - GUI version

espeak-ng is required on your system.
  see: https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md
ffmpeg is required on your system.
  see: https://ffmpeg.org/download.html


filetalk.py - terminal version
------------------------------
usage: filetalk.py [-h] [-v VOICE] [-s SPEED] [-p PITCH] [-mp3] infile outfile

Converts textual content from a PDF, Word, or Text file into speech or audo file.
REQUIRES: "espeak-ng" and "ffmpeg"

positional arguments:
  infile      input file: .txt, .pdf, or .docx only
  outfile     output file (no .ext) or "talk"

options:
  -h, --help  show this help message and exit
  -v VOICE    espeak-ng voice code. Dft en-us
  -s SPEED    espeak-ng speed 30-300 Dft 150
  -p PITCH    espeak-ng pitch 0-99 Dft 45
  -mp3        make additional mp3 output file
  -txt		  make additional text output file

filetalkgui.py - GUI version
----------------------------
Python modules may need to pip install:

    import PyPDF2
    import docx
    ttkbootstrap
    tkinter

