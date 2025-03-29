import requests
import re
import csv
import time
from typing import List, Dict

from bs4 import BeautifulSoup

def fetch_pubmed_papers(query, max_results=10):
    """
    Fetches a list of PubMed paper IDs (PMIDs) based on the given search query.
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "xml",
        "retmax": max_results
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "xml")
        pmids = [id_tag.text for id_tag in soup.find_all("Id")]
        return pmids
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PubMed data: {e}")
        return []

def fetch_paper_details(pmid):
    """
    Fetches details of a specific research paper using its PubMed ID (PMID).
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "xml")
        
        title = soup.find("ArticleTitle").text if soup.find("ArticleTitle") else "N/A"
        pub_date = soup.find("PubDate").text if soup.find("PubDate") else "N/A"
        authors = soup.find_all("Author")
        
        non_academic_authors = []
        company_affiliations = []
        email = "N/A"
        
        for author in authors:
            aff_tag = author.find("Affiliation")
            if aff_tag:
                affiliation = aff_tag.text
                if any(keyword in affiliation.lower() for keyword in ["pharma", "biotech", "inc", "ltd", "gmbh", "corp"]):
                    non_academic_authors.append(author.find("LastName").text if author.find("LastName") else "Unknown")
                    company_affiliations.append(affiliation)
                
            email_tag = author.find(string=re.compile(r"@"))
            if email_tag:
                email = email_tag.strip()
        
        return {
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(non_academic_authors) if non_academic_authors else "N/A",
            "Company Affiliation(s)": ", ".join(company_affiliations) if company_affiliations else "N/A",
            "Corresponding Author Email": email
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching paper details for PubMed ID {pmid}: {e}")
        return None

def save_to_csv(results, filename):
    """
    Saves the fetched paper details to a CSV file.
    Handles file permission errors if the file is open.
    """
    max_retries = 1  # Try 5 times before giving up
    retry_delay = 2   # Wait 2 seconds before retrying

    for attempt in range(max_retries):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=[
                    "PubmedID", "Title", "Publication Date", "Non-academic Author(s)",
                    "Company Affiliation(s)", "Corresponding Author Email"
                ])
                writer.writeheader()
                writer.writerows(results)
            print(f"✅ Results saved to {filename}")
            return  # Exit if successful

        except PermissionError:
            print(f"⚠️ File '{filename}' is open! Close it and retrying ({attempt + 1}/{max_retries})...")
            time.sleep(retry_delay)

    print(f"❌ Failed to save {filename}. Make sure it's closed and try again!")

def is_non_academic(affiliation: str) -> bool:
    """Check if an author is from a non-academic institution"""
    academic_keywords = ["University", "Institute", "Academy", "Labs"]
    return not any(keyword in affiliation for keyword in academic_keywords)

def extract_non_academic_authors(authors: List[Dict[str, str]]) -> List[str]:
    """Return non-academic authors from a list of authors"""
    return [author["name"] for author in authors if is_non_academic(author["affiliation"])]

