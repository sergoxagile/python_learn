#!/usr/bin/env python3
import os
import time
import sys

source = os.getcwdb().decode(encoding='UTF-8')
if len(source) == 0:
    sys.exit()
targetDir = '/home/petrushinsy/Dropbox'
today = targetDir + os.sep + source.split(os.sep)[-1] + '_' +time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

print(os.getcwdb())

comment = input('Enter comment:')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
print('Folder {} create', today)
zipCommand = 'zip -qr {0} {1}'.format(target, ' '.join(source))
if os.system(zipCommand) == 0:
    print('all good')
else:
    print('Something wrong')