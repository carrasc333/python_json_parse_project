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
            org_ids = acu_list.get("org", {}).get("id", {})
            acu_ids = acu_list.get("id", {})

            #print(output_data)
            print(acu_ids, org_ids)

            #Parse the output string as JSON
            result = subprocess.run(['op', 'core', 'describe-acu', '--options', 'withShadows', f'{org_ids}', f'{acu_ids}'], capture_output=True, text=True)
            try:
                output_data = json.loads(result.stdout)

                # Extract the specific field (e.g., "person")
                expiration_date = output_data.get("shadow", {}).get("state", {}).get("reported", {}).get("status", {}).get("httpCertificate", {}).get("notAfter", {})
                percent_life_remaining = output_data.get("shadow", {}).get("state", {}).get("reported", {}).get("status", {}).get("httpCertificate", {}).get("percentLifeRemaining", {})
                vpn_connected = output_data.get("shadow", {}).get("state", {}).get("reported", {}).get("nebula", {}).get("vpnStatus", {})

                #print(percent_life_remaining)


                #if statement to detect if percent life remaining of the certificate is less then 15%
                if not percent_life_remaining:
                    pass
                elif vpn_connected == False:
                    pass
                elif int(percent_life_remaining) < int(15):
                    print("Certificate close to expiring on ORG:", f'{org_ids}', " ACU:",f'{acu_ids}')
                    print("HTTP Certificate Experiation Date is",expiration_date)
                    print("Percent of Certificate Life Remaining",percent_life_remaining)
                    print("VPN is Connected", vpn_connected)
                else:
                    pass


            except ValueError:
                pass


    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)

print("Script is complete")
