from multiprocessing import Pool

from requests import get

# Replace String with your instance IPV4 Address or DNS name
DOMAIN = 'ec2-44-201-120-188.compute-1.amazonaws.com'

def send_request(val):
    while True:
        response = get(f'http://{DOMAIN}')
        data = response.json()
        print("Sent Request")
        print(data)


if __name__ == "__main__":
    with Pool(150) as p:
        p.map(send_request, range(150))


# https://cloudwatch.amazonaws.com/dashboard.html?dashboard=ApiGatewayTraffic&context=eyJSIjoidXMtZWFzdC0xIiwiRCI6ImN3LWRiLTEwNzk2Njk0NzUzOCIsIlUiOiJ1cy1lYXN0LTFfQ0kzSTVJeDJiIiwiQyI6IjFtNTExZ2Q4aTVuaWJvdWkyOGFocW5kMnE4IiwiSSI6InVzLWVhc3QtMTowYTdmZTI3NS1jZDA0LTRjM2ItYjI4Yi1iMzVjNWVhN2FhYWQiLCJPIjoiYXJuOmF3czppYW06OjEwNzk2Njk0NzUzODpyb2xlL3NlcnZpY2Utcm9sZS9DV0RCU2hhcmluZy1SZWFkT25seUFjY2Vzcy1BNzVFVVlJNSIsIk0iOiJVc3JQd1NpbmdsZSJ9&start=PT3H&end=null&autoRefresh=300        