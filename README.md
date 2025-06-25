# LOTS_CSV

```
    ############### ############## ##############
    #             # #            # #            #
    #             # #            # #            #
    #                   LOTS_CSV                #
    #             # #            # #            #
    #             # #            # #            #
    ############### ############## ##############
    =========================================
    LOTS_CSV - LOTS Project CSV Extractor
    =========================================   
    Extracts domains and links from the LOTS project website.
    Written by Kamran Saifullah - @deFr0ggy
    https://linkedin.com/in/kamransaifullah
    https://github.com/deFr0ggy
    https://x.com/deFr0ggy

    Usage: python lots_csv.py
    Requirements: requests, beautifulsoup4, lxml
    License: MIT License
```
LOTS_CSV - LOTS Project CSV Extractor is a simple `Python3` implementation to scrape out the list of domains from the `LOTS-Project`. 

The main reason was to have this automated i.e. to list down all the domain, remove the `*.` and have then with `https://`, so that i can have these tested quickly within the environment to validate if anything is not blocked over the proxy or content security tools that restricts a number of websites. 

So, eventually came up with this small tool. It does the following. 

1. Scrapes the list of domains from the `LOTS Project`. 
2. Removes the `*.`.
3. Adds `https://`. 

Finally generates `CSV` files that can be used quickly. Either use `gowitness` or any other tool that can open up the full list within the browser in case proxy is not allowing to use `curl` or `http`. 

Thus, you can easily validate which domains are opening within the environment and if those are really required to be blocked or not. 

---

At the time of making this repo public, i have executed the tool and latest list can be found in the excel sheets within this repository. 

1. `Domains_Links.csv` is the scraped data from the `LOTS Project`. 
2. `Https_Domains_Cleaned.csv` is the clean list of domains that can be run through within the environemnt. 

## Credits

Special credits goes to `Mr. d0x` for his amazing work and for always inspiring me to do better than before and to come up with unique ideas in the cyber domains. 

Thank you! 
