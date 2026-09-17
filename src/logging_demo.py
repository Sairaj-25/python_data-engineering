import os
import logging

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Pipeline Started")

try:
    amount = "100"
    total = int(amount) + 50
    logging.info(f"Total amount calculated: {total}")
except Exception as e:
    logging.error(f"pipeline falied: {e}")

logging.info("pipeline finished")