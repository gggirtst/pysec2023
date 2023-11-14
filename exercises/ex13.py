
from ftplib import FTP, Error as FTPError
import shodan
from multiprocessing import Pool
from threading import Lock

api_key = "API KEY" #ievietot savu API atslegu no shodan
api = shodan.Shodan(api_key)

query = 'port:21" "230 login successful'
num_results = 20

#saraksts ar FTP serveru adresem
ftp_addresses = ['34.226.107.176', '111.230.173.61', '128.223.51.20', '144.76.215.64', 
        '94.152.35.190', '208.72.21.40', '154.44.148.150', '209.104.252.69', 
        '115.68.231.224', '51.81.230.120', '115.159.112.175', '208.93.219.144', 
        '92.13.39.203', '93.49.169.150', '160.16.198.120', '124.120.129.209', 
        '94.152.63.217', '140.90.101.75', '18.117.165.249', '59.84.41.94']

"""
FTP ADRESU IEGUSANA IZMANTOJOT SHODAN.IO
try:
    results = api.search(query, limit=num_results)
    ftp_addresses.append(result["ip_str"] for result in results["matches"])

except shodan.APIError as e:
    print(f"Error: {e}")
"""

output_lock = Lock()

def ftp_directory(address):
    ftp = FTP(address)
    try:
        ftp.login()
        with output_lock:
            print(f"Directory listing in FTP Server {address}: ")
        ftp.retrlines('LIST', lambda line: print(line))
        ftp.quit()
    except FTPError as ftp_e:
        print(f"Failed to list directory content in FTP server {address}: {ftp_e}")


if __name__ == "__main__":
    with Pool(4) as p:
        p.map(ftp_directory, ftp_addresses)

