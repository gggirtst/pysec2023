# creating 3 different dictionaries with ISP BGP data
LVRTC = {
    "name": "VAS LVRTC",
    "ASN": "AS8194",
    "prefixes": "31.24.192.0/21",
    "contact": "abuse@lvrtc.lv"
}

TET = {
    "name": "SIA Tet",
    "ASN": "AS6747",
    "prefixes": "91.200.64.0/22",
    "contact": "abuse@tet.lv"
}

Telia = {
    "name": "Telia Latvija SIA",
    "ASN": "AS5518",
    "prefixes": "62.63.128.0/21",
    "contact": "abuse@tet.lv"
}

#convert dictionaries in to list
Data = [LVRTC, TET, Telia]
print("Current ISP data:")
for isp in Data:
    print(f"""
    -------{isp["name"]}-------
    ASN: {isp['ASN']}
    Prefix: {isp["prefixes"]}
    Contact: {isp['contact']}
    """)

#combine organisation name, AS number, prefixes and contacts in to different lists
name = [LVRTC["name"], TET["name"], Telia["name"]]
ASN = [LVRTC["ASN"], TET["ASN"], Telia["ASN"]]
prefixes = [LVRTC["prefixes"], TET["prefixes"], Telia["prefixes"]]
contact = [LVRTC["contact"], TET["contact"], Telia["contact"]]

print(name)
print(ASN)
print(prefixes)
print(contact)

#convert AS numbers in to integers in sort in order
new_asn = [item.strip("AS") for item in ASN]

#change strings in list to integers and sort the new list in growing order 
new_asn_sorted = [int(item) for item in new_asn]
new_asn_sorted = sorted(set(new_asn_sorted))
print(f"sorted BGP AS data: {new_asn_sorted}")

#add prefix to ISP org
ISP_name = input(print("Input ISP: "))
PREFIX = input(print("Input new prefix: "))
new_prefixes = (PREFIX)
new_prefixes = list(new_prefixes)
for new_isp in Data:
    if new_isp["name"] == ISP_name:
        new_isp["prefixes"] == new_prefixes
print("NEW ISP DATA:")
for new_isp in Data:
    print(f"""
    -------{new_isp["name"]}-------
    ASN: {new_isp['ASN']}
    Prefix: {new_isp["prefixes"]}
    Contact: {new_isp['contact']}
    """)

