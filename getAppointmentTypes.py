import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('API_KEY')

url = "https://staging-api.gethealthie.com/graphql"

# QUERY GOES HERE
body = """
query getAppointmentTypes(
  $offset: Int,
  $should_paginate: Boolean,
  $page_size: Int,
  $keywords: String,
  $show_group: Boolean,
  $provider_id: String,
  $clients_can_book: Boolean,
  $appointment_type_ids: String,
  $with_deleted_appt_types: Boolean
) {
  appointmentTypes(
    offset: $offset,
    should_paginate: $should_paginate,
    page_size: $page_size,
    keywords: $keywords,
    show_group: $show_group,
    provider_id: $provider_id,
    clients_can_book: $clients_can_book,
    appointment_type_ids: $appointment_type_ids,
    with_deleted_appt_types: $with_deleted_appt_types
  ) {
    id
    name
    available_contact_types
    length
    is_group
    is_waitlist_enabled
  }
}
"""


headers = {
    "Authorization": f"Bearer {api_key}",
    "AuthorizationSource" : "API"
}

# Making a POST request (not GET)
response = requests.post(url, json={"query": body}, headers=headers)

# Handling the response
print("Response status code:", response.status_code)
if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Query failed:", response.text)