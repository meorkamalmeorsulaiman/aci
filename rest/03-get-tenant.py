import requests
import getpass
import json
import ast
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_tenant(username, password, fabric_url ):

    payload = {"aaaUser":{"attributes":{"name":""+username+"","pwd":""+password+""}}}
    login = requests.post('https://'+fabric_url+'/api/aaaLogin.json', json=payload, verify=False)
    json_string = login.json()
    print("Login... status code:", login.status_code)
    print("-----------------------------------------")
    token = json_string["imdata"][0]["aaaLogin"]["attributes"]["token"]
    cookie = {'APIC-cookie':token}

    get_tenant = requests.get('https://'+fabric_url+'/api/node/class/fvTenant.json', cookies=cookie, verify=False)
    json_string = get_tenant.json()

    for tenant in json_string['imdata']:
        print(tenant['fvTenant']['attributes']['name'])

    logout = requests.post('https://'+fabric_url+'/api/aaaLogout.json', cookies=cookie, verify=False)
    print("-----------------------------------------")
    print("Loggin out... status code:", logout.status_code)



username = input("Username: ")
password = getpass.getpass(prompt="Password: ")
payload = {"aaaUser":{"attributes":{"name":""+username+"","pwd":""+password+""}}}
print("-----------------------------------------")

print("List of fabrics:")
print("-----------------------------------------")

with open('fabric-lists.txt', 'r') as f:
    data_string = f.read()
    fabrics = ast.literal_eval(data_string)

for key, value in fabrics.items():
    print(key, value)
print("-----------------------------------------")

fabric_id = int(input("Please select the which fabric: "))
print("-----------------------------------------")

if fabric_id in fabrics:

    fabric_url = fabrics[fabric_id]
    print("Connecting to", fabric_url, "...")
    print("-----------------------------------------")

    get_tenant(username, password, fabric_url)
    print("-----------------------------------------")

    con_option = str(input("Do you want to check in different fabric? yes(Y) or no (N): "))

    while con_option == "y" or con_option == "y":
        with open('fabric-lists.txt', 'r') as f:
            data_string = f.read()
            fabrics = ast.literal_eval(data_string)

        for key, value in fabrics.items():
            print(key, value)
        
        print("-----------------------------------------")

        fabric_id = int(input("Please select the which fabric: "))
        print("-----------------------------------------")
        
        if fabric_id in fabrics:
            fabric_url = fabrics[fabric_id]
            print("Connecting to", fabric_url, "...")
            print("-----------------------------------------")
            get_tenant(username, password, fabric_url)
            print("-----------------------------------------")
        
        con_option = str(input("Do you want to check in different fabric? yes(Y) or no (N): "))
