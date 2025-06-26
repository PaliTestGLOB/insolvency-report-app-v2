import tkinter as tk
from tkinter import messagebox
from insolvency_report_tool import get_company_number, get_insolvency_info, get_filing_history, search_london_gazette, generate_pdf_report
from datetime import datetime
import re

def run_report():
    company_name = entry.get()
    if not company_name:
        messagebox.showwarning("Missing Input", "Please enter a company name.")
        return

    result = get_company_number(company_name)
    if not result:
        messagebox.showerror("Not Found", "Company not found. Please check the name and try again.")
        return

    number, official_name = result
    insolvency = get_insolvency_info(number)
    filings = get_filing_history(number)
    gazette = search_london_gazette(official_name)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = re.sub(r'[^A-Za-z0-9]+', '_', official_name.strip())
    filename = f"{safe_name}_{timestamp}.pdf"
    generate_pdf_report(official_name, insolvency, filings, gazette, filename)
    messagebox.showinfo("Success", f"Report generated: {filename}")

# GUI Setup
root = tk.Tk()
root.title("Insolvency Report Tool")
root.geometry("400x200")

label = tk.Label(root, text="Enter Company Name:")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

submit_button = tk.Button(root, text="Generate Report", command=run_report)
submit_button.pack(pady=20)

root.mainloop()
