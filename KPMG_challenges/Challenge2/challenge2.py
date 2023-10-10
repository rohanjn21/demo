import requests
import json

# Azure instance application details
tenant_id = "{azure-tenantId}"
client_id = "{clientId}"
client_secret = "{client secret of registered app}"
subscription_id = "{azure-subscriptionId}"
resource_group_name = "{azure-resourceGroupName}"
vm_name = "{azure-vm-name}"

# Authenticate and acquire access token
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"
token_data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "resource": "https://management.azure.com/"
}

token_response = requests.post(token_url, data=token_data)
access_token = token_response.json()["access_token"]

# Set up the request headers with the access token
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# API endpoint for getting VM details
vm_endpoint = f"https://management.azure.com/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Compute/virtualMachines/{vm_name}?api-version=20231010"

# Make the API request to get VM details
response = requests.get(vm_endpoint, headers=headers)

if response.status_code == 200:
    vm_details = response.json()
    print("-------------------Get VM Details--------------------------")
    print(json.dumps(vm_details, indent=4))
else:
    raise Exception(f"Failed to retrieve VM metadata: {response.status_code} - {response.reason}")