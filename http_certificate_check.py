#!/usr/bin/env python3
import subprocess
import json

#variables
org = 771
acu = 34342

# Run the external script
result = subprocess.run(['op', 'core', 'describe-acu', '--options', 'withShadows', f'{org}', f'{acu}'], capture_output=True, text=True)


#print(result)

#Parse the output string as JSON
try:
    output_data = json.loads(result.stdout)

    # Extract the specific field (e.g., "person")
    expiration_date = output_data.get("shadow", {}).get("state", {}).get("reported", {}).get("status", {}).get("httpCertificate", {}).get("notAfter", {})
    percent_life_remaining = output_data.get("shadow", {}).get("state", {}).get("reported", {}).get("status", {}).get("httpCertificate", {}).get("percentLifeRemaining", {})

    # Convert the data to a JSON-formatted string
    #json_data = json.dumps(specific_field, indent=2)

    #print(output_data)
    print("HTTP Certificate Experiation Date is",expiration_date)
    print("Percent of Certificate Life Remaining",percent_life_remaining)


    #if statement to detect if percent life remaining of the certificate is less then 15%
    if int(percent_life_remaining) < int(15):
        print("Certificate close to expiring")
    else:
        print("Certificate is in a good state")


except json.JSONDecodeError as e:
    print("Error decoding JSON:", e)
