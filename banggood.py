import time

import checker

URL = "https://www.banggood.com/PRODUCT_URL"
TOKENS = ["Under restocking", "Expected restock on"]
SMTPDetails = checker.SMTPDetails(
    # Hotmail, Live, Outlook => smtp.live.com:25
    # Yahoo => smtp.mail.yahoo.it:25
    # Gmail => smtp.gmail.com:587
    address="smtp.gmail.com",
    port="587",
    tls=True,
    username="",
    password="",
    sender="",
    recipients=[""]
)

while True:
    if not checker.check(URL, TOKENS):
        time.sleep(60)
    else:
        checker.notify(
            SMTPDetails, "New Banggood stock!",
            'The product on Banggood is available!\nCheck the website now: {}'.format(URL)
        )
        break
