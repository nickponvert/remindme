'''
Reminder
2016-07-22 Nick Ponvert

 - I want something that will email me, starting at a specific time and afterwards repeatedly until I disable it, with a reminder.
 - I want to be able to set the reminders in an easy format - python is fine
 - It should use cron to run itself at specific times
 -- Check the reminders
 -- If the time is up on any, send an email
 - The cron job can be the mechanism that sends the reminder repeatedly, all I need is a delay function
 - It should use an org file in my wiki to scrape for the reminders
'''

#Promising, but not well documented from PyOrgMode import PyOrgMode
from remindme import emailme
from remindme import orgnode #Finally something that works
import datetime

class RemindMe(object):
    def __init__(self, toAddr, reminderFile):
        self.mailer = emailme.Emailer(toAddr)
        self.today = datetime.datetime.now().date()
        self.reminderFile = reminderFile
        self.nodelist = orgnode.makelist(self.reminderFile)

    def send_TODO(self):
        '''
        Meant to be run once a day. Sends an email for each TODO item if
        scheduled date is here
        '''
        for node in self.nodelist:
            if node.Todo()=='TODO':
                schedDay = node.Scheduled()
                if schedDay:
                    if self.today>=schedDay:
                        messageBody = node.Body()
                        subject = node.Heading()
                        message = self.mailer.construct_message(subject, messageBody)
                        self.mailer.send_email(message)

    def tear_down(self):
        self.mailer.tear_down()

if __name__=='__main__':
    reminderFile = '/home/nick/src/remindme/reminders_EXAMPLE.org'
    toAddr = 'nickponvert@gmail.com'
    reminder = RemindMe(toAddr, reminderFile)

    reminder.send_TODO()
    reminder.tear_down()

