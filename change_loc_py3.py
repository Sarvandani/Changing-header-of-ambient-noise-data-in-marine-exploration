#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Sarvandani
"""

import subprocess
import glob

p = subprocess.Popen(['sac'],
                     stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE,
                     stderr=subprocess.STDOUT,
                     universal_newlines=True)

s = "echo on\n"
for filename in glob.glob("/Volumes/DRIVE_2/test_data/*.SAC"):
    s += f'''
read {filename}
       CHNHDR stla 30.7302 stlo -9.3566 
write {filename}.relocated
    '''
s += "quit\n"
out, _ = p.communicate(s)
print(out)