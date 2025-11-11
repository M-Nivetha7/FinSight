# backend/scripts/generate_synthetic_transactions.py
import random, uuid, time
import csv
from datetime import datetime, timedelta

OUT = "../data/synthetic_transactions.csv"

card_types = ["credit", "debit", "upi"]
locations = ["Chennai", "Bengaluru", "Mumbai", "Kolkata", "Delhi"]

def generate(n=1000):
    rows = []
    base = datetime.utcnow()
    for i in range(n):
        tx = {
            "transaction_id": str(uuid.uuid4()),
            "customer_id": f"CUST{random.randint(1,500)}",
            "amount": round(random.expovariate(1/50),2),
            "location": random.choice(locations),
            "card_type": random.choice(card_types),
            "time": (base - timedelta(minutes=random.randint(0, 100000))).isoformat()
        }
        rows.append(tx)
    with open(OUT, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)
    print("Generated", OUT)

if __name__ == "__main__":
    generate(1000)
