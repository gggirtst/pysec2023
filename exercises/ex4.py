################## While Loop #####################
network_devices = ["router1", "router2", "core_router1", "edge_router1", "firewall"]
ip_base = "10.99.1."
device_count = len(network_devices)
print(f"Devices in network: {device_count}")

IP_list = []
i = 0

while i < device_count:
    i += 1
    ip_add = ip_base + str(i)
    IP_list.append(ip_add)
    
for device, IP in zip(network_devices, IP_list):
   print(f"Connecting to {device} on IP: {IP}")

# Generating full list of available IP addresses

full_ip_list = [ip_base + str(x)for x in range(1,17)]
print(f"Full list of available IP addresses: {full_ip_list}")


