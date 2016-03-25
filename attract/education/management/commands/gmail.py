# -*- coding utf-8 -*-
import email
from imaplib import IMAP4_SSL
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = """Helps to get last received email from gmail mailbox,
        argument should be in Latin (ASCII) encoding """

    def add_arguments(self, parser):
        parser.add_argument('login', type=str, help="takes email address as login")
        parser.add_argument('password', type=str,
                            help=""" if password contains special characters
                            like '!()_@# etc., its better to take password in quotes """)

    def handle(self, login, password, **options):
        if "@" not in login:  # check if login is valid email address
            raise CommandError("Login should contain '@' symbol")
        else:
            mail = IMAP4_SSL('imap.gmail.com')
            mail.login(login, password)
            mail.select('inbox')

            result, data = mail.uid('search', None, "ALL")
            latest_email_uid = data[0].split()[-1]  # assign last letter UID
            result, data = mail.uid('fetch', latest_email_uid, "(RFC822)")  # catch data by id
            email_message = email.message_from_string(data[0][1])  # convert gibberish data to readable

            print ("""
                Received:   %s
                To:         %s
                From:       %s
                Subject:    %s
                """ % (
                    (email_message['received']),
                    (email_message['To']),
                    (email_message['From']),
                    (email_message['Subject'])
                    ))
