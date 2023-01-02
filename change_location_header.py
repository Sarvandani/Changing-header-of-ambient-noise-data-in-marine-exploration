#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:35:07 2019

@author: Sarvandani
"""
import subprocess
import glob

p = subprocess.Popen(['sac'],
                     stdout = subprocess.PIPE,
                     stdin  = subprocess.PIPE,
                     stderr = subprocess.STDOUT )

s = "echo on\n"
#for filename in glob.glob("/Volumes/DRIVE_2/SAC_DATA/T2/T2-1-Cross1_Mic01.SAC"):
#for  filename in glob.glob("/Volumes/DRIVE_2/PROJECT_TAIWANESE_3HOURS/T3*.sac"):
for  filename in glob.glob("/Volumes/DRIVE_2/Github_header_correction/SULZ*.SAC"):
    s += '''
read %(file)s
       CHNHDR stla 58.60 stlo -33.06
write %(file)s.relocated
    ''' % ( {'file': filename } )
s += "quit\n"
out = p.communicate( s )
print out[0]
