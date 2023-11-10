#!/usr/bin/env python3

import json

# Sample JSON data with varying indentation
json_data = '''
{
  "person": {
    "name": "John",
    "age": 30,
    "city": "New York"
  },
  "pets": [
    {
      "type": "dog",
      "name": "Buddy"
    },
    {
      "type": "cat",
      "name": "Whiskers"
    }
  ]
}
'''

# Parse the JSON data
try:
    parsed_data = json.loads(json_data)

    # Extract the specific field (e.g., "person")
    specific_field = parsed_data.get("person", {})

    # Reformat the specific field with 2 spaces of indentation
    formatted_data = json.dumps(specific_field, indent=2)
    print(formatted_data)

except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
