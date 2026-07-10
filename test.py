from tools.company_resolver import search_companies
companies = search_companies("AMD")

for company in companies:

    print(company)