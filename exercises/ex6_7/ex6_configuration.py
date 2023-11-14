def create_config(hostname):
    config = {
        "hostname": hostname,
        "gateway": None,
        "vlans": {},
        "ip": None,
        "interfaces": {},
    }
    return config

def create_vlan(config, vlan_id):
    config["vlans"][vlan_id] = {}

def set_default_route(config, gateway):
    config["gateway"] = gateway

def set_ip(config, ip_address):
    config["ip"] = ip_address

def set_vlan_interface(config, vlan_id, ip_address):
    config["vlans"][vlan_id] = ip_address

def set_interface(config, interface, vlan_id):
    config["interfaces"][interface] = vlan_id

def get_config(config):
    configuration = f"\nhostname {config['hostname']}\n"
    configuration += f"ip route 0.0.0.0 0.0.0.0 {config['gateway']}\n"
    for interface, vlan in config['interfaces'].items():
        configuration += f"interface {interface}\n"
        configuration += f" switchport mode trunk\n"
        configuration += f" switchport mode trunk allowed {vlan}\n"
    for vlan, ip in config['vlans'].items():
        configuration += f"interface {vlan}\n"
        configuration += f"  ip address {ip}\n"
    return configuration
