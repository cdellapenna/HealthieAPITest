import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')

url = "https://staging-api.gethealthie.com/graphql"

# QUERY GOES HERE
body = """
mutation createClient($first_name: String, 
                      $last_name: String, 
                      $email: String, 
                      $skipped_email: Boolean, 
                      $phone_number: String, 
                      $dietitian_id: String, 
                      $user_group_id: String, 
                      $dont_send_welcome: Boolean ) {
  createClient(input: { first_name: $first_name, 
                        last_name: $last_name, email: $email,
                        skipped_email: $skipped_email, 
                        phone_number: $phone_number, 
                        dietitian_id: $dietitian_id, 
                        user_group_id: $user_group_id, 
                        dont_send_welcome: $dont_send_welcome  }) {
    user {
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
    "first_name": "Gary",
    "last_name":"The Snail",
    "skipped_email": True
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