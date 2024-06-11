import re
import requests

API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.abuseipdb.com/api/v2/check'

def get_user_ip():
    while True:
        ip_address = input("Enter an IP address to check: ")
        if re.match(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', ip_address):
            return ip_address
        else:
            print("Invalid IP format. Please try again.")

def check_ip_malicious(ip_address):
    headers = {
        'Accept': 'application/json',
        'key': API_KEY
    }
    response = requests.get(f"{API_URL}?ipAddress={ip_address}", headers=headers)
    data = response.json()
    return data['data']['isPublic']

def main():
    ip_address = get_user_ip()
    is_malicious = check_ip_malicious(ip_address)
    if is_malicious:
        print(f"The IP address {ip_address} is potentially malicious.")
    else:
        print(f"The IP address {ip_address} appears to be safe.")

if __name__ == '__main__':
    main()