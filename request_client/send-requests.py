from multiprocessing import Pool

from requests import get

# Replace String with your instance IPV4 Address or DNS name
DOMAIN = 'ec2-54-92-247-37.compute-1.amazonaws.com'

def send_request(val):
    while True:
        response = get(f'http://{DOMAIN}')
        data = response.json()
        print("Sent Request")
        print(data)


if __name__ == "__main__":
    with Pool(150) as p:
        p.map(send_request, range(150))

        