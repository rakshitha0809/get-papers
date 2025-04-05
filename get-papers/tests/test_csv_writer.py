import os
from get_papers.csv_writer import write_csv


def test_write_csv(tmp_path):
    output_file = tmp_path / "test_output.csv"
    data = [
        {
            "PubmedID": "123456",
            "Title": "Test Paper",
            "Publication Date": "2023",
            "Non-academic Author(s)": "Dr. Pharma",
            "Company Affiliation(s)": "Cool Biotech Inc.",
            "Corresponding Author Email": "dr@biotech.com",
        }
    ]

    write_csv(data, filename=str(output_file))

    assert output_file.exists()
    content = output_file.read_text()
    assert "Test Paper" in content
