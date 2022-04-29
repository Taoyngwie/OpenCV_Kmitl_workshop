import requests
 
url = "https://api.aiforthai.in.th/lpr-v2"
payload = {'crop': '1', 'rotate': '1'}
files = {'image':open(r'D:\Destop\kmitl_opencv\car2.jpg', 'rb')}
 
headers = {
    'Apikey': "pDNZf5l5Q41NMlid71henxwlomey6RJ7",
    }
 
response = requests.post( url, files=files, data = payload, headers=headers)
 
print(response.json())