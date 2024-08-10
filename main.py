import csv
from datetime import datetime
import pandas as pd


class CSV:
    CSV_FILE = "finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

    @classmethod
    def initialize_csv(cls):
        try:
            #Trying to Read the file
            pd.read_csv(cls.CSV_FILE)
        #If not found it will create File
        except FileNotFoundError:
            #Creating pandas Dataframe which contains mentions columns
            df = pd.DataFrame(columns= cls.COLUMNS)
            #Creating a CSV file based on the created DataFrame
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        #Creating the entry as Dictionary
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description
        }
        #Opening the csv File in Append Mode and "with open" will automatically close the file and manage memory leaks
        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            #Creating a Writer object which can able to write a dictionary to given CSV file
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            #Appending the new entry to CSV file
            writer.writerow(new_entry)
        print("Entry Added Successfully")


CSV.initialize_csv()
CSV.add_entry("10-08-2024", 350, "Expense" , "Lunch")