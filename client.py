import requests

# response = requests.post('http://127.0.0.1:5001/advert',
#                          json={
#                              'title': 'first01',
#                              'owner': 'man',
#                              'description': 'BlaBlaBla',
#                              'password': '1234'
#                          })

response = requests.get('http://127.0.0.1:5001/advert/36')
# response = requests.delete('http://127.0.0.1:5001/advert/36')

print(response.status_code)
print(response.json())
