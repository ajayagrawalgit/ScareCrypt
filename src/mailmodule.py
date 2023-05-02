import smtplib
from src.SECRETS.mailcreds import *
import datetime

def send_key_to_mail(encryption_key, cleaned_key):
    try:
        # Set up SMTP connection with SSL/TLS encryption
        with smtplib.SMTP_SSL(smtp_server, smtp_port_no) as smtp:
            smtp.login(sender_email_id, sender_email_password)

            # Compose message including current date and time (12 hr format) - "mm/dd/yyyy hh:mm:ss AM/PM"
            current = datetime.datetime.now()
            date_and_time = current.strftime("%m/%d/%Y %I:%M:%S %p")
            
            subject = f"Encryption Key generated at {date_and_time}"
            body = f"Below is your Encryption key details:\nKey(Binary Format): {encryption_key}\nKey(Encoded): {cleaned_key}\nGenerated at: {date_and_time}\n\nKeep it very safe and secure.\n\nThanks."
            message = f"Subject: {subject}\n\n{body}"

            smtp.sendmail(sender_email_id, receiver_email_id, message)
            
            message_to_be_displayed = f'''
            The Encrypted key has been sent successfully to the mail. Details below:
            Sent From:      {sender_email_id}
            Recipient:      {receiver_email_id}
            Date and Time:  {date_and_time}
            
            Make sure you also check your Spam Folder for the mail if you don't find it on Inbox.
            
            Cheers !
            '''
            print(message_to_be_displayed)
        
        return 0
    
    except Exception as e:
        error_message_to_be_displayed = f'''
        Uh Oh...
        !!! THE MAIL WAS NOT SENT !!!
        Error: {e}
        
        Here are a few things you can try to resolve this error:
        1. Double-check your SMTP server and port number to make sure they are correct.
        2. Make sure that your credentials (sender email id and password) are correct.
        3. Check your internet connection to ensure that it is stable.
        4. Try running your code on a different network to rule out any network-related issues.
        5. Try using a different SMTP server or port number.
        6. Ensure that the SMTP server allows authentication and allows email to be sent using SMTP.
        
        If none of these steps resolve the issue, you may want to consult the documentation for the email provider you are using or seek help from their support team.
        
        After putting in the correct details in mailcreds.py under SECRETS Folder. Please try re-run the script and it should work. If not, feel free to open an issue on the GitHub and help us make this tool a robust one.
        
        GitHub link: 
        
        Cheers.
        '''
        print(error_message_to_be_displayed)
        
        return 1
