#!/usr/bin/env python3
import subprocess
import json

# Run the external script
result = subprocess.run(['op', 'core', 'describe-acu', '--options', 'withShadows', '771', '34342'], capture_output=True, text=True)

#print(result.stdout)

# Parse the output string as JSON
try:
    output_data = json.loads(result)

    # Extract the specific field (e.g., "person")
    #specific_field = output_data.get("httpCertificate", {})

    print(output_data)
    #print(specific_field)



except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
