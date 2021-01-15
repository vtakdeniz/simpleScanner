import threading
import ipFetcher
from ipwhois import IPWhois
import pprint

info={}
unidentified=[]


# Splits lists into given number
def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def infoFetch(ip):
    for e in ip:
        try:
            obj = IPWhois(e)
        except:
            if (e.split(".")[0:3] == ipFetcher.returnLocalIp().split(".")[0:3]) or e.split(".")[0:3]=="127.0.0.0" :
                continue
            else:
                if e not in unidentified:
                    unidentified.append(e)
        else:
            res = obj.lookup_whois()
            if res['nets'][0]['description'] != None:
                string = res['nets'][0]['description']
                info[string] = {}
                info[string]["ip address"]=e
                if res['nets'][0]['address'] != None:
                    info[string]['address'] = res['nets'][0]['address']
                else:
                    info[string]['address'] = "No address information"

                if res['nets'][0]['city'] != None:
                    info[string]['city'] = res['nets'][0]['city']
                else:
                    info[string]['city'] = "No city information"

                if res['nets'][0]['country'] != None:
                    info[string]['country'] = res['nets'][0]['country']
                else:
                    info[string]['country'] = "No country information"

                if res['nets'][0]['postal_code'] != None:
                    info[string]['postal_code'] = res['nets'][0]['postal_code']
                else:
                    info[string]['postal_code'] = "No postal_code information"

                if res['nets'][0]['emails'] != None:
                    info[string]['emails'] = []
                    for e in res['nets'][0]['emails']:
                        info[string]['emails'].append(e)

                else:
                    info[string]['emails'] = "No email information"

            else:
                string = res["asn_description"]
                info[string] = {}
                info[string]["ip address"] = e
                if res['nets'][0]['address'] != None:
                    info[string]['address'] = res['nets'][0]['address']
                else:
                    info[string]['address'] = "No address information"

                if res['nets'][0]['city'] != None:
                    info[string]['city'] = res['nets'][0]['city']
                else:
                    info[string]['city'] = "No city information"

                if res['nets'][0]['country'] != None:
                    info[string]['country'] = res['nets'][0]['country']
                else:
                    info[string]['country'] = "No country information"

                if res['nets'][0]['postal_code'] != None:
                    info[string]['postal_code'] = res['nets'][0]['postal_code']
                else:
                    info[string]['postal_code'] = "No postal_code information"

                if res['nets'][0]['emails'] != None:
                    info[string]['emails'] = []
                    for e in res['nets'][0]['emails']:
                        info[string]['emails'].append(e)

                else:
                    info[string]['emails'] = "No email information"


# Scans network and writes to console with pprint
def scanToConsole():
    infoFetch()
    pprint.pprint(info)
    if len(unidentified)!=0:
        print("/////////// Unidentified Ip Addresses Below ; Further Control is Needed !!!!")
        for e in unidentified:
            print(e)

# Writes all info to a file in pformat
def write(path):
    if len(info)== 0:
        infoFetch()
    myfile= path
    output_s = pprint.pformat(info)
    with open(myfile + "/Results.txt", 'w') as file:
        file.write(output_s)
        if len(unidentified) != 0:
            file.write("\n")
            file.write("\n")
            file.write("/////////// Unidentified Ip Addresses Below ; Further Control is Needed !!!!")
            file.write("\n")
            for e in unidentified:
                file.write(e)
                file.write("\n")







# Divides ip address list and assigns a thread for each of them
def scan():
    info.clear()
    unidentified.clear()
    threads = []
    for i in chunks(ipFetcher.returnIP(), 2):
        t = threading.Thread(target=infoFetch, args=[i])
        t.start()
        threads.append(t)

    for thr in threads:
        thr.join()

