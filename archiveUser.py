import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')

url = "https://staging-api.gethealthie.com/graphql"

# QUERY GOES HERE
body = """
mutation bulkUpdateClients($ids: [ID!], $active_status: Boolean) {
  bulkUpdateClients(input: { ids: $ids, active_status: $active_status } ) {
    users {
      id
    }
    messages {
      field
      message
    }
  }
}
"""

variables = {
    "ids": "600771",
    "active_status": False
}

headers = {
    "Authorization": f"Bearer {api_key}",
    "AuthorizationSource" : "API"
}

# Making a POST request (not GET)
response = requests.post(url, json={"query": body, "variables": variables}, headers=headers)

# Handling the response
print("Response status code:", response.status_code)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Query failed:", response.text)