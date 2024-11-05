import random
import string
import requests

from django.conf import settings

login = settings.NIKITA_LOGIN
password = settings.NIKITA_PASSWORD
sender = settings.NIKITA_SENDER
url = settings.NIKITA_URL


def generate_transaction_id(length=12):
    chars = string.ascii_letters + string.digits
    transactionId = ''.join(random.choice(chars) for _ in range(length))
    return transactionId


def send_sms(phone_number, text):
    xml_data = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    <message>
        <login>{login}</login>
        <pwd>{password}</pwd> 
        <id>{generate_transaction_id()}</id>
        <sender>{sender}</sender>
        <text>{text}</text>
        <phones>
            <phone>{phone_number}</phone>
        </phones>
    </message>"""

    headers = {
        'Content-Type': 'application/xml'
    }
    try:
        response = requests.post(
            url,
            data=xml_data,
            headers=headers,
            verify=False,
            timeout=10
        )

        if response.status_code != 200:
            raise ValueError(f'Not successfully sent to nikita')

    except requests.exceptions.Timeout as t:
        raise ValueError('Timeout error')
    except Exception as e:
        raise ValueError(f'Exception {e}')
    else:
        return response.text
