"""
This call sends a message to one recipient.
"""
from mailjet_rest import Client
from mailjet.forgot_password_code import forgot_password_template
from config import get_settings

api_key = get_settings().MJ_APIKEY_PUBLIC
api_secret = get_settings().MJ_APIKEY_PRIVATE

def send_email(subject: str, send_to: str):
    mailjet = Client(auth=(api_key, api_secret))
    data = {
        'FromEmail': 'admin@sduf.net',
        'FromName': 'Dmytro Kozin',
        'Subject': f'{subject}',
        'Text-part': 'this is test email',
        'Html-part': 'this is test email',
        'Recipients': [{'Email': f'{send_to}'}]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
    return result

def send_forgot_password_email(full_name: str, code: str, send_to: str):
    mailjet = Client(auth=(api_key, api_secret))

    params = {
        "full_name": full_name,
        "one_time_code": code,
        "expiration_time": "10 minutes",
        "company_name": "SDUF Inc.",
        "support_email": "support@bite.com",
        "company_website": "https://sduf.net"
    }

    email_content = forgot_password_template.format(**params)

    data = {
        'FromEmail': 'admin@sduf.net',
        'FromName': 'no-reply',
        'Subject': 'One-Time Login Code',
        'Text-part': '',
        'Html-part': email_content,
        'Recipients': [{'Email': f'{send_to}'}]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
    return result
