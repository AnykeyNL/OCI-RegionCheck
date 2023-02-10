import urllib.request, json
from ping3 import ping, verbose_ping
regionurl = "https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json"


with urllib.request.urlopen(regionurl) as url:
    data = json.load(url)
rc =0
regions = data["regions"]
for region in regions:
    print (region["region"])
    rc = rc + 1
    cidrs = region["cidrs"]
    for cidr in cidrs:
        if "OBJECT_STORAGE" in cidr["tags"]:
            #print (cidr)
            cidrblock = cidr["cidr"]
            regioip_elements = cidrblock.split(".")
            startID = 1
            while False:
                regionip = "{}.{}.{}.{}".format(regioip_elements[0],regioip_elements[1],regioip_elements[2], startID)
                print ("Pinging: {}".format(regionip))
                r = ping(regionip)
                if r:
                    print (r)
                    break
                else:
                    startID = startID + 1


print ("Region count: {}".format(rc))