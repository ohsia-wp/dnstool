import whois

def main():
    domain = whois.whois(input("Enter domain: "))
    dig(domain)

def dig(domain):
    print("Domain name:", domain.domain_name)
    print("Registrar:", domain.registrar)
    print("Created:", domain.creation_date)
    print("Expiration:", domain.expiration_date)
    print("Country:", domain.country)
    print("Name Servers:", domain.name_servers)
    print("Status:", domain.status)

# Call the main function to start
main()
