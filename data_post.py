import requests
payload = {
    "Id": 12345,
    "Customer": "John Smith",
    "Quantity": 1,
    "Price": 10.00  
}
header = {
    'Authorization': 'Bearer mt0dgHmLJMVQhvjpNXDyA83vA_PxH23Y',
    'Content-Type': 'application/json',
    'Content-Length': '80'
}
r = requests.post('https://httpbin.org/post', json=payload, headers=header)
print(r)
print(r.text)