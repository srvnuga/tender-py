import smtplib

SMTP_SERVER = 'localhost:1025'
NOTIFICATOR_ADDRESS = ['tndr64@gmail.com']
NOTIFICATION_RECIPIENTS_LIST = ['tndr64@gmail.com']


class Notificator:
    _server = None

    def __init__(self):
        self._server = smtplib.SMTP(SMTP_SERVER)
        self._server.starttls()
        print('Started smtp conn')

    def notify_about_tenders(self, tender_list):
        for tender in tender_list:
            self.send_notification(tender)

    def send_notification(self, tender):
        self._server.sendmail(NOTIFICATOR_ADDRESS, NOTIFICATION_RECIPIENTS_LIST,
                              "Please check tender: " + tender.get_number())

    def __send_email(self, from_addr, to_addr_list, message):

        # header = 'From: %s' % from_addr
        # header += 'To: %s' % ', '.join(to_addr_list)
        # header += 'Cc: %s' % ', '.join(cc_addr_list)
        # header += 'Subject: %s' % subject

        # message = header + message

        # server = smtplib.SMTP(smtpserver)
        # server.starttls()
        # server.login(login, password)
        self._server.sendmail(from_addr, to_addr_list, message)


asd = Notificator()
asd.notify_about_tenders([])
# sendemail(from_addr='python@RC.net',
#           to_addr_list=['12@asd.com'],
#           cc_addr_list=['gebond77@gmail.com'],
#           subject='Howdy',
#           message='Howdy from a python function',
#           login='user',
#           password='pass')
