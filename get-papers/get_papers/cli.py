# get_papers/cli.py

import argparse
from get_papers.pubmed_client import fetch_pubmed_ids, fetch_details
from get_papers.paper_filter import filter_non_academic
from get_papers.csv_writer import write_csv


def main():
    parser = argparse.ArgumentParser(
        description="Fetch PubMed papers with pharma/biotech authors."
    )
    parser.add_argument("query", type=str, help="Search query for PubMed.")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename.")
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug output."
    )

    args = parser.parse_args()

    if args.debug:
        print(f"🔍 Query: {args.query}")

    ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"📄 Found {len(ids)} paper IDs")

    records = fetch_details(ids)

    output_data = []

    for paper in records:
        try:
            title = paper.get("TI", "N/A")
            pmid = paper.get("PMID", "N/A")
            date = paper.get("DP", "N/A")
            email = paper.get("EM", "N/A")
            authors = paper.get("AU", [])
            affiliations = paper.get("AD", [])

            if not authors or not affiliations:
                continue

            if isinstance(affiliations, str):
                affiliations = [affiliations] * len(authors)

            non_acads, companies = filter_non_academic(authors, affiliations)

            if non_acads:
                output_data.append(
                    {
                        "PubmedID": pmid,
                        "Title": title,
                        "Publication Date": date,
                        "Non-academic Author(s)": "; ".join(non_acads),
                        "Company Affiliation(s)": "; ".join(companies),
                        "Corresponding Author Email": email,
                    }
                )
        except Exception as e:
            if args.debug:
                print(f"⚠️ Skipped paper due to error: {e}")
            continue

    write_csv(output_data, filename=args.file)
