from scapy.all import IP, TCP, sr
from multiprocessing import Pool

def scan_port(ip_port):
    ip, port = ip_port
    try:
        syn = IP(dst=ip) / TCP(dport=port, flags="S")
        response = sr(syn, timeout=1, verbose=0)
        if response and response[0] and response[0][1] and response[0][1][TCP].flags == "SA":
            return port
    except Exception as e:
        pass
    return None

def tcp_scan(ip, ports, num_processes=4):
    ip_port_list = [(ip, port) for port in ports]
    pool = Pool(num_processes)
    open_ports = pool.map(scan_port, ip_port_list)
    pool.close()
    pool.join()
    return [port for port in open_ports if port is not None]

if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Replace with your target IP address
    target_ports = range(1, 1025)  # Replace with your desired port range

    try:
        scan_result = tcp_scan(target_ip, target_ports)
        if scan_result:
            print(f"Open ports on {target_ip}: {scan_result}")
        else:
            print(f"No open ports found on {target_ip}")
    except Exception as e:
        print(f"Error: {e}")
