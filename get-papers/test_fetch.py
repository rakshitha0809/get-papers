# test_fetch.py

from get_papers.pubmed_client import fetch_pubmed_ids, fetch_details

query = "cancer immunotherapy"
ids = fetch_pubmed_ids(query)
print(f"Fetched {len(ids)} IDs")

papers = fetch_details(ids)

for paper in papers:
    print("=" * 80)
    print("Title:", paper.get("TI", "N/A"))
    print("Authors:", paper.get("AU", []))
    print("Affiliations:", paper.get("AD", "N/A"))
    print("Publication Date:", paper.get("DP", "N/A"))
    print("Email:", paper.get("EM", "N/A"))  # Sometimes present
