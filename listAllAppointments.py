import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')

url = "https://staging-api.gethealthie.com/graphql"

# QUERY GOES HERE
body = """
query appointments(
  $user_id: ID,
  $filter: String,
  $sort_by: String,
  $should_paginate: Boolean,
  $offset: Int,
  $is_active: Boolean,
  $with_all_statuses: Boolean
) {
  appointmentsCount(user_id: $user_id, filter: $filter, is_org: true, is_active: $is_active)
  appointments(
    is_active: $is_active,
    user_id: $user_id,
    filter: $filter,
    is_org: true,
    sort_by: $sort_by,
    should_paginate: $should_paginate,
    offset: $offset,
    with_all_statuses: $with_all_statuses
  ) {
    id
    date
    contact_type
    length
    location
    provider {
      id
      full_name
    }

    appointment_type {
      name
      id
    }

    attendees {
      id
      full_name
      first_name
      avatar_url
      phone_number
    }
  }
}
"""

variables = {
    "id": "599713"
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