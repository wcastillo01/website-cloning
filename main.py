from datetime import date  # core python module
import pandas as pd  # pip install pandas
# from deta import app
from send_email import send_email  # local python module


# Public GoogleSheets url - not secure!
SHEET_ID = "1Eyot_DcfKgKvD9iI2pjpErGtvlH41oXW3TLTGpWSwkI"
SHEET_NAME = "potential_users"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    parse_dates = ["email", "username"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


def query_data_and_send_emails(df):
    email_counter = 0
    for _, row in df.iterrows():        
        send_email(
            subject=f'Reset instagram password {row["username"]}',
            receiver_email=row["email"],
            name=row["username"],
        )
        email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = load_df(URL)
query_data_and_send_emails(df)