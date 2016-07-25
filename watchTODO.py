#!/usr/bin/env python
import sys
sys.path.append('/home/nick/src')
from remindme import reminder

reminderFile = '/home/nick/Dropbox/wiki/todo.org'
toAddr = 'nickponvert@gmail.com'
reminder = reminder.RemindMe(toAddr, reminderFile)

reminder.send_TODO()
reminder.tear_down()
