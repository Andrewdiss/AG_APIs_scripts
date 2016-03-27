# -*- coding utf-8 -*-
import email
from imaplib import IMAP4_SSL
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from validate_email import validate_email


class Command(BaseCommand):
    help = 'Helps to get last received email from gmail mailbox'

    def add_arguments(self, parser):
        parser.add_argument('login', help='takes email address as login')
        parser.add_argument('password', help='password should be in quotes')

    def handle(self, *args, **options):
        login, password = options['login'], options['password']
        if not validate_email(login):  # check if login is valid email address
            raise CommandError('Email is not correct')
        else:
            mail = IMAP4_SSL(settings.GMAIL_IMAP)
            mail.login(login, password)
            mail.select('inbox')

            result, data = mail.uid('search', None, 'ALL')
            latest_email_uid = data[0].split()[-1]
            # catch data by id
            result, data = mail.uid('fetch', latest_email_uid, settings.RFC)
            # convert gibberish data to readable
            email_message = email.message_from_string(data[0][1])
            fields = {'received': email_message['Date'],
                      'to': email_message['To'],
                      'from': email_message['From'],
                      'subj': email_message['Subject']
                      }
            self.stdout.write('''
                Received: %(received)s
                To: %(to)s
                From: %(from)s
                Subject: %(subj)s
                ''' % fields)
