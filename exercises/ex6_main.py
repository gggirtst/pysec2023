import ex6_configuration

user_hostname = input("Enter hostname: ")
user_gateway = input("Set default gateway for the device: ")
user_vlan_id = input("Set vlan (for example 'Vlan20'): ")
user_ip = input("Set IP address for Vlan interface: ")
user_interface = input("Set interface for Vlan trunking: ")


device = ex6_configuration.create_config(user_hostname)
ex6_configuration.set_default_route(device, user_gateway)
ex6_configuration.set_vlan_interface(device, user_vlan_id, user_ip)
ex6_configuration.set_interface(device, user_interface, user_vlan_id)
device_config = ex6_configuration.get_config(device)

print(f"""Router Configuration:
      {device_config}
      """)