import time
import random
import requests
import datetime

WEBHOOK_URL = "https://discord.com/api/webhooks/1470177389588906317/uh5sXiYbEfHC8_-GAFvO4_pc6dmXOcFoFp9hdgSS0IkFaN1hAelS0yNVX2iCTxv_JUE2"

NORMAL_AMOUNTS = [2000, 5000, 1500, 8000, 500, 250, 9000, 3000, 1100, 1300]
RARE_AMOUNTS = [14000, 11000, 9500, 16000]
WAITTIME = [20,150,500,600,1100,1500,4000]

END_TIME = time.time() + (2 * 60 * 60)  # 2 hours

def get_random_currency():
    rand = random.random()
    if rand < 0.80:
        return "LTC"
    elif rand < 0.90:
        return "BTC"
    else:
        return "USDT"

while time.time() < END_TIME:
    # 4% chance for rare amount
    if random.random() < 0.04:
        amount = random.choice(RARE_AMOUNTS)
    else:
        amount = random.choice(NORMAL_AMOUNTS)

    currency = get_random_currency()

    payload = {
        "embeds": [
            {
                "title": "Transaction Completed!",
                "color": 458687,
                "description": (
                    f"Brick Amount (abbreviated for anonymity): `{amount}`\n\n"
                    "Sender: `Anonymous`\n"
                    "Receiver: `Anonymous`\n\n"
                    f"Currency Paid: `{currency}`"
                )
            }
        ],
        "components": []
    }

    r = requests.post(WEBHOOK_URL, json=payload, timeout=10)

    print(
        f"[{datetime.datetime.utcnow().isoformat()}] "
        f"Sent amount={amount} currency={currency} status={r.status_code}",
        flush=True
    )

    sleep_time = random.choice(WAITTIME)
    time.sleep(sleep_time)
