import csv
import requests

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

def test_domain_redirects(domains):
    results = []
    for domain in domains:
        try:
            response = requests.get(f"http://{domain}", allow_redirects=True, verify=False)
            status_code = response.status_code
            
            # Get the final URL after all redirects
            final_url = response.url
            
            # If there were redirects, get the last redirect's status code
            if response.history:
                status_code = response.history[-1].status_code
            
            # The target domain is the final URL, but only if there was a redirect
            target_domain = final_url if response.history else ''
            
            results.append([domain, status_code, target_domain])
        except requests.RequestException as e:
            print(f"Error accessing {domain}: {e}")
            results.append([domain, 'Error', ''])
    return results

def save_results_to_csv(results, filename='domain_redirect_results.csv'):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['domain', 'response_code', 'target'])
        writer.writerows(results)

def main():
    # Get domains from user input
    # print("Enter domains to test (comma-separated):")
    # user_input = input().strip()
    # domains_to_test = [domain.strip() for domain in user_input.split(',')]
    # for domain in list_of_domains:
    #     test_domain_redirects(domain)
    results = test_domain_redirects(list_of_domains)
    save_results_to_csv(results)
    print(f"Results saved to domain_redirect_results.csv")

if __name__ == "__main__":
    main()