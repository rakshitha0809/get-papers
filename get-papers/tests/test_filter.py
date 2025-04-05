from get_papers.paper_filter import filter_non_academic


def test_filter_non_academic():
    authors = ["Alice Pharma", "Bob University", "Charlie Biotech"]
    affiliations = [
        "BioPharma Inc, New York",
        "University of California, Berkeley",
        "Bright Biotech Ltd, London",
    ]

    non_acads, companies = filter_non_academic(authors, affiliations)

    assert "Alice Pharma" in non_acads
    assert "Charlie Biotech" in non_acads
    assert "Bob University" not in non_acads

    assert any("pharma" in c.lower() or "biotech" in c.lower() for c in companies)
