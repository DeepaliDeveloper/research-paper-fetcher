# research-paper-fetcher

# Research Paper Fetcher  

A Python command-line tool to fetch research papers from PubMed based on user queries.  
It filters papers that have at least one author affiliated with a pharmaceutical or biotech company and exports results to a CSV file.  

## Installation  

Ensure you have Python 3 and [Poetry](https://python-poetry.org/docs/) installed.  

Clone the repository:  
```sh
git clone https://github.com/DeepaliDeveloper/research-paper-fetcher.git
cd research-paper-fetcher

poetry install


# #### **Installing from TestPyPI**  
# ```md
# If you want to install the package directly from TestPyPI, run:  
# ```sh
# pip install --index-url https://test.pypi.org/simple/ research-paper-fetcher


---

### **3️⃣ Usage Instructions**  
```md
## Usage  

Run the following command to fetch papers:  
```sh
poetry run get-papers-list "Quantum Computing" -f results.csv



---

### **4️⃣ Example Output**  
```md
## Example Output  

The generated CSV file will contain the following columns:  
- **PubmedID** → Unique paper ID  
- **Title** → Research paper title  
- **Publication Date** → Date of publication  
- **Non-academic Author(s)** → Authors from non-academic institutions  
- **Company Affiliation(s)** → Pharma/Biotech companies  
- **Corresponding Author Email** → Contact email  

Example:
| PubmedID | Title | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
|----------|------------------|------------------|----------------------|----------------------|----------------------|
| 12345678 | Quantum Advances | 2024-03-01 | Dr. John Doe | QuantumTech Inc. | johndoe@quantumtech.com |


## Development & Contribution  

1. Clone the repository  
2. Create a virtual environment using Poetry  
3. Install dependencies  
4. Make your changes in a separate branch  
5. Submit a pull request  

**Running Tests**  
Run unit tests with:  
```sh
poetry run pytest



# ---

# ### **6️⃣ Publishing to TestPyPI (For Maintainers)**  
# ```md
# ## Publishing the Package  

# Ensure you have configured TestPyPI:  
# ```sh
# poetry config pypi-token.testpypi YOUR_API_TOKEN


poetry build
poetry publish --repository testpypi
