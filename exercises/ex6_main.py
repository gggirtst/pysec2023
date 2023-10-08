# EXERCISE 6 and 7 !!!
import ex6_configuration

user_hostname = input("Enter hostname: ")
user_vlan_id = input("Set vlan (for example 'Vlan20'): ")
user_interface = input("Set interface for Vlan trunking: ")

def is_valid_ip(ip_str):
    octets = ip_str.split('.')
    
    if len(octets) != 4:
        return False
    
    try:
        for octet in octets:
            octet_int = int(octet)
            if octet_int < 0 or octet_int > 255:
                return False
    except ValueError:
        return False
    
    return True

# Exercise 7 for EXCEPTIONS!
while True:
    user_ip = input("Set IP address for Vlan interface: ")
    user_gateway = input("Set default gateway for the device: ")

    if is_valid_ip(user_ip):
        print("Valid IP address:", user_ip)
        break
    else:
        print("Invalid IP address. Please enter a valid IP address.")
    
    if is_valid_ip(user_gateway):
        print("Valid IP address:", user_gateway)
        break
    else:
        print("Invalid IP address. Please enter a valid IP address.")

device = ex6_configuration.create_config(user_hostname)
ex6_configuration.set_default_route(device, user_gateway)
ex6_configuration.set_vlan_interface(device, user_vlan_id, user_ip)
ex6_configuration.set_interface(device, user_interface, user_vlan_id)
device_config = ex6_configuration.get_config(device)

print(f"""Router Configuration:
      {device_config}
      """)
