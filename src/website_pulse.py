import ses_mailer
import requests

mail = ses_mailer.Mail(
    sender="slad0716@gmail.com"
)

def lambda_handler(event, context):
    WEBSITE_URL: str = "https://example.com/void"

    # Make a get request to a random website
    response = requests.get(WEBSITE_URL)

    # If we get anything other than a 200 OK response, trigger
    # a warning email
    if response.status_code is not 200:
        mail.send(
            to="slad0716+test@gmail.com",
            subject=f"HEY! {WEBSITE_URL} down",
            body=f"WARNING: {WEBSITE_URL} just went down! Retrying in 5 minutes."
        )
