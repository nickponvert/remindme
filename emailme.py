import smtplib
from local import secrets

class Emailer(object):
    def __init__(self, toAddr):
        self.server = smtplib.SMTP()
        self.server.connect('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(secrets.EMAIL, secrets.PASS)
        self.toAddr = toAddr
    @staticmethod
    def construct_message(subject, message):
        fullMessage = 'Subject: {}\n\n{}'.format(subject, message)
        return fullMessage
    def send_email(self, message):
        self.server.sendmail(secrets.EMAIL, self.toAddr, message)
    def tear_down(self):
        self.server.quit()

if __name__=='__main__':
    em = Emailer(secrets.EMAIL)
    messageBody = 'hello world'
    subject = 'emailme.py test'
    message = em.construct_message(subject, messageBody)
    em.send_email(message)
    em.tear_down()
