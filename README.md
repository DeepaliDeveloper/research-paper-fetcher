# research-paper-fetcher
A Python command-line tool that fetches research papers from PubMed based on user queries. It identifies papers where at least one author is affiliated with a pharmaceutical or biotech company and exports the results to a CSV file.



Prerequisites
Ensure you have:
✅ Python 3 installed
✅ Poetry installed for dependency management



Steps to Install
Clone the repository:
git clone https://github.com/DeepaliDeveloper/research-paper-fetcher.git
cd research-paper-fetcher



Install dependencies using Poetry:
poetry install



Basic Usage
To fetch research papers, use the following command:
poetry run get-papers-list "Quantum Computing" -f results.csv

"Quantum Computing" → Your search query
-f results.csv → File to save the results



Additional Command-line Options
-h or --help → Display usage instructions
-d or --debug → Enable debug mode




Example Output
The generated CSV file will contain the following columns:

PubmedID	Title	            Publication Date	Non-academic Author(s)	Company Affiliation(s)	Corresponding Author Email
12345678	Quantum Advances	2024-03-01	        Dr. John Doe	        QuantumTech Inc.	    johndoe@quantumtech.com



Run unit tests with:
poetry run pytest