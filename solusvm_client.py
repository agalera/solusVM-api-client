import requests

class solusVM_Client(self):
    def __init__(self, url, api_id, api_key):
        self.url = "best ip dot com"
        self.key = "*****-*****-*****"
        self.hash = "best hash"

    def sQuery(self, values):

        values.update({'rdtype':'json','hash':self.hash,'key': self.key})
        response = requests.get('https://'+self.url+':5656/api/client/command.php', params=self.values, timeout=10)
        return response.text

    def get_status(self):
        return sQuery({'action': 'status'})

    def get_info(self):
        return sQuery({'action': 'info', 'ipaddr': 'true', 'hdd': 'true', 'mem': 'true','bw': 'true'})

    def shutdown(self):
        return sQuery({'action': 'shutdown'})

    def boot(self):
        return sQuery({'action': 'boot'})

    def reboot(self):
        return sQuery({'action': 'reboot'})
