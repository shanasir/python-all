from fileinput import filename
from operator import index

import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime

from PIL.ImageColor import colormap
from docutils.nodes import description, label
from fontTools.misc.plistlib import end_date

from data_entry import get_date,get_category,get_amount,get_description

class CSV:
    CSV_FILE = "finance.csv"
    Columns = ["date","amount","category","description"]
    FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df=pd.DataFrame(columns=cls.Columns)
            df.to_csv(cls.CSV_FILE,index=False)

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }

        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            write = csv.DictWriter(csvfile,fieldnames=cls.Columns)
            write.writerow(new_entry)
        print("Entry added successfully")


    @classmethod
    def get_transaction(cls,start_date,end_date):
        df=pd.read_csv(cls.CSV_FILE)
        df["date"]=pd.to_datetime(df["date"],format=CSV.FORMAT)
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        start_date=datetime.strptime(start_date,CSV.FORMAT)
        end_date=datetime.strptime(end_date,CSV.FORMAT)

        mask=(df["date"]>= start_date)&(df["date"]<= end_date)
        filtered_df = df.loc[mask]

        if filtered_df.empty:
            print("No transaction found in the given date range")

        else:
            print(f" Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")

            print(filtered_df.to_string(index=False,formatters={"date":lambda x:x.strftime(CSV.FORMAT)}))


            total_income = filtered_df[filtered_df["category"]=="Income"]["amount"].sum()
            total_expense = filtered_df[filtered_df["category"]!="Income"]["amount"].sum()
            print("\n Summary:")
            print(f"Total Income : ${total_income:.2f}")
            print(f"Total expense : ${total_expense:.2f}")
            print(f" Net Savings : ${(total_income - total_expense):.2f}")

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date("Enter a date of the transactions( dd-mm-yyyy) format or  Tap enter for today's date: " ,allow_default=True)
    amount = get_amount()
    category = get_category()
    descriptions = get_description()
    CSV.add_entry(date,amount,category,descriptions)

CSV.get_transaction("01-01-2002","01-01-2025")



def plot(df):
    df.set_index("date",inplace=True)

    income_df=(
        df[df["category"]=="Income"]
        .resample("D")
        .sum()
        .reindex(df.index,fill_value=0)
    )

    expense_df = (
        df[df["category"] != "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )

    plt.figure(figsize=(10,5))
    plt.plot(income_df.index,income_df["amount"],label="Income",color="r")
    plt.plot(expense_df.index,expense_df["amount"],label="Expense",color="g")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income and Expense Over time")
    plt.legend()
    plt.grid(True)
    plt.show()

def show_expense_pie_chart(df):
    expense_df = df[df["category"] != "Income"]

    category_totals = expense_df.groupby("category")["amount"].sum()

    # Plot the pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(
        category_totals,
        labels=category_totals.index,
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Expense Distribution by Category")
    plt.grid(True)
    plt.axis("equal")
    plt.show()


def main():
    while True:
        print("\n1. Add a new transactions")
        print("2. View transaction and summary within a date range")
        print("3. Exit")
        choice = input("\n Enter your choice (1-3):")

        if choice =="1":
            add()
        elif choice =="2":
            start_date = get_date("Enter the start date (dd-mm-yyyy):")
            end_date = get_date("Enter the end date (dd-mm-yyyy):")
            df = CSV.get_transaction(start_date,end_date)
            if input("Do you want to see a plot ?(y/n)").lower() == "y":
                plot(df)
            if not df.empty and input("Do you want to see a pie chart of expenses? (y/n): ").lower() == "y":
                show_expense_pie_chart(df)
        elif choice =="3":
            print("Exiting......")
            break
        else:
            print("Invalid choice .Enter 1,2 or 3.")



if __name__=="__main__":
    main()