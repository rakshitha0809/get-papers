from unittest.mock import patch, MagicMock
from get_papers.pubmed_client import fetch_pubmed_ids, fetch_details


@patch("get_papers.pubmed_client.Entrez.read")
@patch("get_papers.pubmed_client.Entrez.esearch")
def test_fetch_pubmed_ids(mock_esearch, mock_read):
    mock_read.return_value = {"IdList": ["12345", "67890"]}
    mock_handle = MagicMock()
    mock_esearch.return_value = mock_handle

    ids = fetch_pubmed_ids("cancer")
    assert ids == ["12345", "67890"]
    mock_esearch.assert_called_once()


@patch("get_papers.pubmed_client.Medline.parse")
@patch("get_papers.pubmed_client.Entrez.efetch")
def test_fetch_details(mock_efetch, mock_parse):
    fake_record = {"PMID": "12345", "TI": "Test Title"}
    mock_parse.return_value = [fake_record]

    mock_handle = MagicMock()
    mock_efetch.return_value = mock_handle

    details = fetch_details(["12345"])
    assert len(details) == 1
    assert details[0]["PMID"] == "12345"
    assert details[0]["TI"] == "Test Title"
