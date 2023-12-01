#!/usr/bin/env python3
import subprocess
import json

for offset in range(0, 45000, 1000):
    #run list acus script
    list_acus_script = subprocess.run(['op', 'mm', 'list-acus', '--limit', f'{1000}', '--offset', f'{offset}'], capture_output=True, text=True)

    #Parse the output string as JSON
    try:
        output_data = json.loads(list_acus_script.stdout)

        for acu_list in output_data:
            # Extract the specific field (e.g., "person")
            acu_ids = acu_list.get("org", {}).get("id", {})
            org_ids = acu_list.get("id", {})

        #print(output_data)
            print(acu_ids, org_ids)

        #print(output_data)

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
