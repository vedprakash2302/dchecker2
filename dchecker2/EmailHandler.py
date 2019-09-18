import click
import smtplib
import configparser
from datetime import datetime
from email.mime.text import MIMEText
from .utils import echo


class EmailHandler:

    def send(self, from_address, to_address, subject, body):
        """Sends an email with specified body.
        Keyword arguments:
        subject -- subject of the report.
        body -- the body as a string.
        from_address -- email address the report will come from.
        to_address -- email address the report is going to.
        """

        msg = MIMEText(body)
        msg['Subject'] = subject + "\n"
        msg['From'] = from_address
        msg['To'] = to_address
        mail_connection = smtplib.SMTP("smtp.ufl.edu")
        mail_connection.sendmail(from_address, to_address, msg.as_string())
        mail_connection.quit()
