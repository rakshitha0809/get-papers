# get_papers/paper_filter.py

from typing import List, Tuple


academic_keywords = [
    "university",
    "college",
    "institute",
    "department",
    "school",
    "hospital",
    ".edu",
    ".ac.",
]

company_keywords = ["pharma", "biotech", "inc", "ltd", "corp", "gmbh", "llc"]


def is_academic_affiliation(affiliation: str) -> bool:
    affiliation = affiliation.lower()
    return any(keyword in affiliation for keyword in academic_keywords)


def is_company_affiliation(affiliation: str) -> bool:
    affiliation = affiliation.lower()
    return any(keyword in affiliation for keyword in company_keywords)


def filter_non_academic(
    authors: List[str], affiliations: List[str]
) -> Tuple[List[str], List[str]]:
    """
    Returns:
        - non_academic_authors: List of authors with non-academic affiliations
        - company_affiliations: Extracted company names
    """
    non_academic_authors = []
    company_affiliations = []

    for author, aff in zip(authors, affiliations):
        if not is_academic_affiliation(aff):
            non_academic_authors.append(author)
            if is_company_affiliation(aff):
                company_affiliations.append(aff)

    return non_academic_authors, company_affiliations
