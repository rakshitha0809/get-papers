# get_papers/csv_writer.py

import csv
from typing import List, Dict, Optional


def write_csv(data: List[Dict], filename: Optional[str] = None) -> None:
    fieldnames = [
        "PubmedID",
        "Title",
        "Publication Date",
        "Non-academic Author(s)",
        "Company Affiliation(s)",
        "Corresponding Author Email",
    ]

    if filename:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"✅ Output written to: {filename}")
    else:
        print("📋 Output:")
        print(",".join(fieldnames))
        for row in data:
            print(",".join([str(row[field]) for field in fieldnames]))
