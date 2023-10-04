import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')

url = "https://staging-api.gethealthie.com/graphql"

# QUERY GOES HERE
body = """
query users(
  $offset: Int,
  $keywords: String,
  $sort_by: String,
  $active_status: String,
  $group_id: String,
  $show_all_by_default: Boolean,
  $should_paginate: Boolean,
  $provider_id: String,
  $conversation_id: ID,
  $limited_to_provider: Boolean,
) {
  usersCount(
    keywords: $keywords,
    active_status:$active_status,
    group_id: $group_id,
    conversation_id: $conversation_id,
    provider_id: $provider_id,
    limited_to_provider: $limited_to_provider
  )
  users(
    offset: $offset,
    keywords: $keywords,
    sort_by: $sort_by,
    active_status: $active_status,
    group_id: $group_id,
    conversation_id: $conversation_id,
    show_all_by_default: $show_all_by_default,
    should_paginate: $should_paginate,
    provider_id: $provider_id,
    limited_to_provider: $limited_to_provider
  ) {
      id
  }
}
"""

variables = {
    "active_status": "active",
    "sort_by": "last_name_desc"
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