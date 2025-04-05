# 🧬 get-papers

A Python CLI tool that fetches PubMed research papers based on a search query and identifies those with at least one **non-academic author affiliated with a pharmaceutical or biotech company**.

---

## ✨ Features

- 🔍 Search PubMed using any valid query (full syntax supported)
- 🏢 Identify papers with non-academic affiliations (e.g., biotech, pharma)
- 📧 Extract key metadata like title, publication date, company affiliations, and emails
- 📄 Output results to CSV or print to console
- ✅ Typed Python, modular design, and fully tested
- ⚙️ CLI interface with `--help`, `--debug`, and `--file` options

---

## 📦 Installation

```bash
pip install -i https://test.pypi.org/simple get-papers
```

> Uses TestPyPI — requires Python 3.9+

---

## 🚀 Usage

```bash
get-papers-list "cancer immunotherapy"
```

Optional flags:

| Flag            | Description                                |
|-----------------|--------------------------------------------|
| `--file` or `-f`  | Save output to CSV (default is console)    |
| `--debug`        | Show detailed logs                         |
| `--help` or `-h` | Display usage instructions                 |

Example:

```bash
get-papers-list "covid-19 vaccine" --file results.csv --debug
```

---

## 🛠 Project Structure

```
get-papers/
├── get_papers/
│   ├── pubmed_client.py      # Fetch PubMed data
│   ├── paper_filter.py       # Filter pharma/biotech authors
│   ├── csv_writer.py         # Output to CSV or console
│   └── cli.py                # Command-line interface
├── tests/
│   ├── test_filter.py
│   ├── test_csv_writer.py
│   └── test_pubmed_client.py
├── pyproject.toml
├── README.md
```

---

## 🧪 Running Tests

```bash
poetry install
poetry run pytest
```

Includes tests for:
- Filtering logic
- CSV output
- Mocked PubMed API fetch

---

## 🔐 Heuristics for Filtering

- Excludes academic affiliations containing:
  - `university`, `college`, `institute`, `.edu`, `department`, etc.
- Includes company affiliations containing:
  - `pharma`, `biotech`, `inc`, `ltd`, `gmbh`, `llc`, `corp`, etc.

---

## 📚 Dependencies

- [Biopython](https://biopython.org/) – PubMed API access
- [Poetry](https://python-poetry.org/) – Dependency management
- [pytest](https://docs.pytest.org/) – Testing
- Python Standard Library (`csv`, `argparse`, `typing`, `time`, etc.)

---

## 🧠 Built With Help From

- ChatGPT for initial architecture and CLI generation
- PubMed Entrez API
- Biopython's Medline parser

---

