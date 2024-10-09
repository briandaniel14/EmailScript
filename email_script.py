import smtplib
import secrets
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email(subject, body, to_emails, smtp_server, smtp_port, username, password, attachments=None):
    # Set up the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)

    for to_email in to_emails:
        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Attach any files
        if attachments:
            for file in attachments:
                attachment = open(file, "rb")

                # Instance of MIMEBase and named as p
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')

                # Attach the instance 'part' to instance 'msg'
                msg.attach(part)

                # Close the file
                attachment.close()

        # Send the message via the server
        server.send_message(msg)

    # Terminate the SMTP session and close the connection
    server.quit()

subject = "Talent Accquisition opportunity with Edinburgh AI"

body = """Dear reader,

Edinburgh AI is the University of Edinburgh's leading AI Society. We're currently looking for sponsors in exchange for a wide range of channels for talent acquisition.

This includes but is not limited to:
- A booth at our AI Expo (A science fair type event where students present AI projects competing for a £1000 cash prize)
- Speaker slots at our AI Expo
- Branding on our social media and at weekly workshops
- Tailored access to CVs of top students
- Much more

Notably, The University of Edinburgh produces the most AI publications in the UK - ensuring the students you're exposed to are some of the best AI talent in the world.

I've attached our pitch deck so you can have a more detailed look at our offerings.

Our website is https://www.edinburghai.org/

If you're interested please let me know so we can set up a call (or continue discussing through email if you wish).

Thank you!

Kind Regards,
Brian Daniel"""

#to_emails = ['briandaniel789@gmail.com']

to_emails = [
    "briandaniel789@gmail.com"
]

smtp_server='mail.privateemail.com'
smtp_port=587
username='brian@edinburghai.org'
password=secrets.password
attachments = [r"C:\Users\brian\Downloads\EdinburghAISponsorDeckv4min.pdf"]

if __name__ == '__main__':
    send_email(subject, body, to_emails, smtp_server, smtp_port, username, password, attachments)
    with open(r"C:\Users\brian\OneDrive\Work\CodingProjects\EdinburghAIEmailSender\sent_emails.txt", "a") as log:
        log.write("\n".join(to_emails) + "\n")

    