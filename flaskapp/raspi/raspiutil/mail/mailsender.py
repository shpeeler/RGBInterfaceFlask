import argparse
import smtplib
import io
import json

class MailSender(object):
    """ class for sending mail """

    def __init__(self, user, pw, toaddr, tocc):
        self.user = user
        self.pw = pw
        self.toaddr = toaddr
        self.tocc = tocc

    def send_mail(self, subject, message):
        success = True

        header = 'From: {0}\n'.format(self.user)
        header += 'To: {0}\n'.format(self.toaddr)
        header += 'Cc: {0}\n'.format(self.tocc)
        header += 'Subject: {0}\n\n'.format(subject)

        msg = header + message

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.connect('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.user, self.pw)
            server.sendmail(self.user, self.toaddr, msg)
        except:
            success = False
        finally:
            server.quit()

        return success

    