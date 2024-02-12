import hashlib
import json
import os

# TheExit/Content/Configuration/MatchConfig/MatchConfig_ARC_BlastFurnace.uasset
# Json Asset Name MatchConfig_ARC_BlastFurnace
# Output Path: /Game/Content/Configuration/MatchConfig/MatchConfig_ARC_BlastFurnace.MatchConfig_ARC_BlastFurnace
# Output in MD5: ff58d310-2193c308-6da0b050-6492d794-Default


# config example:
# MatchConfig_SLU_DownTown = {"gameMode": "4b4bbb82b85e662e5121233ae06f9b1c-Default",
#                                 "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_SLU_DownTown.MatchConfig_SLU_DownTown"}
#
#     MatchConfig_Demo_HarvestYourExit_1v5 = {"gameMode": "789c81dfb11fe39b7247c7e488e5b0d4-Default",
#                                            "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_Demo_HarvestYourExit_1v5.MatchConfig_Demo_HarvestYourExit_1v5"}
#     MatchConfig_Demo = {"gameMode": "08d2279d2ed3fba559918aaa08a73fa8-Default",
#                         "MatchConfiguration": "/Game/Configuration/MatchConfig/MatchConfig_Demo.MatchConfig_Demo"}

root_path = "/Game/Configuration/MatchConfig/"
root_folder = "MatchConfig"

for file in os.listdir(root_folder):
    if file.endswith(".json"):
        asset_name = file.split(".")[0]
        #print(f"Json Asset Name {asset_name}")
        output_path = f"{root_path}{asset_name}.{asset_name}"
        #print(f"Output Path: {output_path}")
        md5 = hashlib.md5(output_path.encode('utf-8')).hexdigest()

        # Insert dash every 8 characters in the MD5 hash
        #md5_with_dashes = '-'.join(md5[i:i+8] for i in range(0, len(md5), 8))

        item = {asset_name: {"gameMode": f"{md5}-Default", "MatchConfiguration": output_path}}
        print(item)
