from typing import List, Dict
from Bio import Entrez, Medline
import time

Entrez.email = "your.email@example.com"


def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    """
    Fetch PubMed IDs matching the search query.

    Args:
        query (str): PubMed search query.
        max_results (int): Maximum number of results to retrieve.

    Returns:
        List[str]: List of PubMed IDs.
    """
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    return record["IdList"]


def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    """
    Fetch metadata for a list of PubMed IDs.

    Args:
        pubmed_ids (List[str]): List of PubMed IDs.

    Returns:
        List[Dict]: List of parsed MEDLINE records.
    """
    try:
        handle = Entrez.efetch(
            db="pubmed", id=",".join(pubmed_ids), rettype="medline", retmode="text"
        )
        records = Medline.parse(handle)
        return list(records)
    except Exception as e:
        print(f"❌ Error fetching paper details: {e}")
        return []
