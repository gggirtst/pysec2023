import configuration

user_hostname = input("Enter hostname: ")
user_gateway = input("Set default gateway for the device: ")
user_vlan_id = input("Set vlan (for example 'Vlan20'): ")
user_ip = input("Set IP address for Vlan interface: ")
user_interface = input("Set interface for Vlan trunking: ")


device = configuration.create_config(user_hostname)
configuration.set_default_route(device, user_gateway)
configuration.set_vlan_interface(device, user_vlan_id, user_ip)
configuration.set_interface(device, user_interface, user_vlan_id)
device_config = configuration.get_config(device)

print(f"""Router Configuration:
      {device_config}
      """)