# filetalk (Python3)
# espeak-ng is required on your system.
#   see: https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md
# ffmpeg is required on your system.
#   see: https://ffmpeg.org/download.html
# Inputs a text, word, or pdf file and talks, or outputs a wav file
# special modules needed:
# >pip install --pre python-docx  # for MS Word docs
# >pip install PyPDF3  # for .pdf documents
# >pip install argparse  # for command line help
# args:
#   input path/file (required)
#   output path/file | 'talk' (required)
#   -v voice -s speed (defaults: -v "en-us" -s 150 )
#   -mp3 (default wav file output)

import sys
import subprocess
import PyPDF3
import docx
import argparse

desc = '''
Converts textual content from a PDF, Word, or Text file
into speech or audo file.
REQUIRES: "espeak-ng" and "ffmpeg"
'''
# create command-line variables from arguments
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('infile', help='input file: .txt, .pdf, or .docx only')
parser.add_argument('outfile', help='output file (no .ext) or "talk"')
parser.add_argument('-v', dest='voice', action='store',
                    default='en-us', help='espeak-ng voice code. Dft en-us')
parser.add_argument('-s', dest='speed', action='store',
                    default='150', help='espeak-ng speed 30-300 Dft 150')
parser.add_argument('-p', dest='pitch', action='store',
                    default='45', help='espeak-ng pitch 0-99 Dft 45')
parser.add_argument('-mp3', dest='MP3', action='store_true',
                    help='make additional mp3 output file')
parser.add_argument('-txt', dest='TXT', action='store_true',
                    help='make additional text output file')

args = parser.parse_args()

#---------------------------------------------------------------

clean_text = ""  # holds text to be sent to espeak

# read input file .txt .pdf or .docx

if args.infile.lower().endswith(".pdf"):
    pdfreader = PyPDF3.PdfFileReader(open(args.infile, 'rb'))
    for page_num in range(pdfreader.numPages):
        text = pdfreader.getPage(page_num).extractText()
        clean_text += text
elif args.infile.lower().endswith(".docx"):
    doc = docx.Document(args.infile)
    for paragraph in doc.paragraphs:
        clean_text += paragraph.text
elif args.infile.lower().endswith(".txt"):
    clean_text = open(args.infile).read()
else:
    print("Input file must be txt, pdf, or docx file!")
    sys.exit()

# Just "speak" the file contents
if args.outfile.lower() == "talk":
    subprocess.call(["espeak-ng", "-v"+args.voice, "-p"+args.pitch,
                "-s"+args.speed, clean_text])
    sys.exit()

# create speech audio file
subprocess.call(["espeak-ng", "-v"+args.voice, "-p"+args.pitch,
                "-s"+args.speed, "-w"+args.outfile+".wav", clean_text])

# create mp3 version also?
if args.MP3 is True:
    subprocess.call(["ffmpeg", "-i", args.outfile+".wav", args.outfile+".mp3"])
    print("Created MP3 file:", args.outfile+".mp3")

if args.TXT is True:
    with open(args.outfile+".txt", "w") as fout:
        fout.write(clean_text)
    print("Created TXT file:", args.outfile+".txt")
