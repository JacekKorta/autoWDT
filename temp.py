'''
import os, time
os.startfile('vies.pdf', "print")
#os.startfile('eksportowi.txt', "print")
 
time.sleep(5)
for p in psutil.process_iter(): #Close Acrobat after printing the PDF
    if 'AcroRd' in str(p):
        p.kill()

import os
import subprocess
subprocess.call(['acrord32', "/t", r"D:\Skrypty\autoWDT\vies.pdf", "Adobe PDF"])

import os
import subprocess
subprocess.Popen([r"D:\Skrypty\autoWDT\vies.pdf"])
'''

import os
os.startfile("vies.pdf", "print")
