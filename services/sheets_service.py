import streamlit as st
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def get_client():
    credentials_info = dict(st.secrets["gcp_service_account"])
    credentials = Credentials.from_service_account_info(
        credentials_info,
        scopes=SCOPES
    )
    client = gspread.authorize(credentials)
    return client

def get_spreadsheet():
    client = get_client()
    spreadsheet = client.open(st.secrets["google_sheet_name"])
    return spreadsheet

def read_sheet(sheet_name):
    spreadsheet = get_spreadsheet()
    worksheet = spreadsheet.worksheet(sheet_name)
    data = worksheet.get_all_records()
    return pd.DataFrame(data)

def append_row(sheet_name, row):
    spreadsheet = get_spreadsheet()
    worksheet = spreadsheet.worksheet(sheet_name)
    worksheet.append_row(row)

def update_cell(sheet_name, row, col, value):
    spreadsheet = get_spreadsheet()
    worksheet = spreadsheet.worksheet(sheet_name)
    worksheet.update_cell(row, col, value)
