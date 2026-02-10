import requests
import getpass
import urllib3
import ast
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("-----------------------------------------")
username = input("Username: ")
password = getpass.getpass(prompt="Password: ")
print("-----------------------------------------")

with open('fabric-lists.txt', 'r') as f:
    data_string = f.read()
    fabrics = ast.literal_eval(data_string)

for key, fabric_url in fabrics.items():
    # print(key, fabric_url)
    payload = {"aaaUser":{"attributes":{"name":""+username+"","pwd":""+password+""}}}
    r = requests.post('https://'+fabric_url+'/api/aaaLogin.json', json=payload, verify=False)
    r_json = r.json()
    token = r_json["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}

    print("Login to...", fabric_url, "status code:", r.status_code)
    print("-----------------------------------------")

    logout = requests.post('https://'+fabric_url+'/api/aaaLogout.json', cookies=cookie, verify=False)
    print("Loggin out...", fabric_url, "status code:", logout.status_code)
    print("-----------------------------------------")
