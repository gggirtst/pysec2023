################## Exercise 5 #####################
class NetworkDevice:
    def __init__(self, hostname, ip_address) -> None:
        self.hostname = hostname
        self.ip_address = ip_address


class Router(NetworkDevice):
    def __init__(self, hostname, ip_address) -> None:
        super().__init__(hostname, ip_address)
        self.credentials_dict = {}

    def credentials(self, username, password):
        self.credentials_dict['username'] = username
        self.credentials_dict['password'] = password

    def printInfo(self):
        print(f'''
            Hostname: {self.hostname}
            IP: {self.ip_address}
            Credentials: 
                Username: {self.credentials_dict.get('username', 'N/A')}
                Password: {self.credentials_dict.get('password', 'N/A')}
              ''')

switch = Router("edge_router1", "192.168.1.1")
switch.credentials('Username', 'Password')
switch.printInfo()
