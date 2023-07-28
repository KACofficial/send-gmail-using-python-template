import smtplib
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Set up the SMTP server and login
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Using TLS for secure communication
    server.starttls()  # For secure communication
    server.login(sender_email, sender_password)

    # Compose the email
    email_body = MIMEText(message)
    email_body['From'] = sender_email
    email_body['To'] = recipient_email
    email_body['Subject'] = subject

    # Send the email
    server.sendmail(sender_email, recipient_email, email_body.as_string())

    # Close the connection
    server.quit()
  
# Replace the following variables with your Gmail credentials and recipient's email address
sender_email = 'SENDERSEMAIL@gmail.com' #the gmail that will send the email to the recipient
sender_password = 'SENDERPASSWORD' #the password to the sender(using app passwords, tutorial: https://shorturl.at/BO046)
recipient_email = 'RECIPIENTEMAIL' #the email to the person that will recieve the email
subject = 'SUBJECT' #the subject of the email
message = 'CONTENT' #the message to the emal
# Call the function to send the email
send_email(sender_email, sender_password, recipient_email, subject, message)
