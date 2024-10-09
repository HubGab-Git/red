import requests
import csv
import dns.resolver

def test_domain_redirects(domains):
    results = []
    for domain in domains:
        try:
            # Get HTTP response and handle redirects
            response = requests.get(f"http://{domain}", allow_redirects=True, verify=False)
            status_code = response.status_code
            final_url = response.url
            if response.history:
                status_code = response.history[-1].status_code
            target_domain = final_url if response.history else ''

            # Get nameservers
            try:
                answers = dns.resolver.resolve(domain, 'NS')
                nameservers = [rdata.to_text() for rdata in answers]
                nameservers_str = ', '.join(nameservers)
            except Exception as e:
                print(f"Error retrieving nameservers for {domain}: {e}")
                nameservers_str = 'Error retrieving nameservers'

            results.append([domain, status_code, target_domain, nameservers_str])
        except requests.RequestException as e:
            print(f"Error accessing {domain}: {e}")
            results.append([domain, 'Error', '', ''])
    return results

def save_results_to_csv(results, filename='domain_redirect_results.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['domain', 'response_code', 'target', 'nameservers'])
        writer.writerows(results)

def main():
    # Replace this with your actual list of domains
    
    list_of_domains = [
        "ataxian.de",
        "auventis.com",
        "auventis.de",
        "axuna.de",
        "brandprotection.partnersgroup.com",
        "convenis.de",
        "investmentgroup.ch",
        "notification.partnersgroup.com",
        "p3-privateequity.net",
        "partners.ch",
        "partnersgroup-privateequity.com",
        "partnersgroup.ae",
        "partnersgroup.asia",

    "partnersgroup.at",

    "partnersgroup.ba", "partnersgroup.biz",

    "partnersgroup.by", "partnersgroup.ch",

    "partnersgroup.cn",

    "partnersgroup.co.gg", "partnersgroup.co.id",

    "partnersgroup.co.il",

    "partnersgroup.co.kr",

    "partnersgroup.co.nz",

    "partnersgroup.co.uk",

    "partnersgroup.co.za",

    "partnersgroup.com.au",

    "partnersgroup.com.hk",

    "partnersgroup.com.my",

    "partnersgroup.com.ru",

    "partnersgroup.com.tr",

    "partnersgroup.com.tw",

    "partnersgroup.com.ua",

    "partnersgroup.com.vn",

    "partnersgroup.com",

    "partnersgroup.de",

    "partnersgroup.dk",

    "partnersgroup.es",

    "partnersgroup.fi",

    "partnersgroup.fr",

    "partnersgroup.gg",

    "partnersgroup.gr",

    "partnersgroup.hr",

    "partnersgroup.hu",

    "partnersgroup.id",

    "partnersgroup.ie",

    "partnersgroup.in",

    "partnersgroup.info",

    "partnersgroup.io",

    "partnersgroup.is",

    "partnersgroup.it",

    "partnersgroup.jp",

    "partnersgroup.kr",

    "partnersgroup.li",

    "partnersgroup.lt",

    "partnersgroup.lu",

    "partnersgroup.lv",

    "partnersgroup.my",

    "partnersgroup.net.au",

    "partnersgroup.net",

    "partnersgroup.nl",

    "partnersgroup.no",

    "partnersgroup.nz",

    "partnersgroup.ph",

    "partnersgroup.pt",

    "partnersgroup.ro",

    "partnersgroup.rs",

    "partnersgroup.sg",

    "partnersgroup.si",

    "partnersgroup.site",

    "partnersgroup.tw",

    "partnersgroup.vn",

    "partnersgroup.xxx",

    "partnersgroupaustralia.com.au",

    "partnersgroupprivateequity.com",

    "partnersgroupprivateequitylimited.com",

    "pearl-privateequity.net",

    "pg-globalvalue.net",

    "pg-impact.com",

    "pg-impact.org",

    "pggenerationsfund.com",

    "pggo.net",

    "pgimpact.com",

    "pgliquids.com",

    "pgpe-ltd.com",

    "pgpe.ch",

    "pgpe.gg",

    "pgpe.uk",

    "pgpel.com",

    "princess-privateequity.net",

    "taxunion.de"

    ]

    results = test_domain_redirects(list_of_domains)
    save_results_to_csv(results)
    print(f"Results saved to domain_redirect_results.csv")

if __name__ == "__main__":
    main()