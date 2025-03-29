import argparse
import time
from pubmed_fetcher import fetch_pubmed_papers, fetch_paper_details, save_to_csv

def main():
    """
    Parses command-line arguments, fetches PubMed papers, and saves the results.
    """
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed based on a query.")
    parser.add_argument("query", type=str, help="Search query (supports full PubMed syntax)")
    parser.add_argument("-f", "--file", type=str, default="results.csv", help="Filename to save results (default: results.csv)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers for query: {args.query}")
    
    pmids = fetch_pubmed_papers(args.query)
    if not pmids:
        print("No results found.")
        return
    
    results = []
    for pmid in pmids:
        print(f"Fetching details for PMID: {pmid}") 
        paper_details = fetch_paper_details(pmid)
        if paper_details:
            results.append(paper_details)
        time.sleep(1)  # Delay to prevent hitting API rate limits
    
    save_to_csv(results, args.file)

if __name__ == "__main__":
    main()
