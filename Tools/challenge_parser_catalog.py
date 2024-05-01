import json
import os


def extract_challenge_info(data):
    challenge_info = {}
    for item in data:
        if "RequiredChallengesToComplete" in item.get("Properties", {}):
            challenges = item["Properties"]["RequiredChallengesToComplete"]
            for challenge in challenges:
                challenge_id = challenge.get("ChallengeId")
                if challenge_id:
                    challenge_data = {
                        "challengeBlueprint": challenge["ChallengeAsset"]["AssetPathName"],
                        "ChallengeCompletionValue": challenge["ChallengeCompletionValue"]
                    }
                    challenge_info[challenge_id] = challenge_data
    return challenge_info


def log_challenge_info(challenge_info, filename):
    with open(filename, "a") as f:
        for challenge_id, info in challenge_info.items():
            f.write(f"{challenge_id}: {info}\n")


if __name__ == "__main__":
    output_folder = r"X:\tmp\Output\Exports\TheExit\Content\Items"
    log_folder = os.path.join(output_folder, "Logs")
    os.makedirs(log_folder, exist_ok=True)

    broken_items_file = os.path.join(log_folder, "broken_items.txt")
    challenge_log_file = os.path.join(log_folder, "challenge_log.txt")

    for root, _, files in os.walk(output_folder):
        for file in files:
            if file.endswith(".json"):
                json_file = os.path.join(root, file)
                with open(json_file, "r") as f:
                    data = json.load(f)

                challenge_info = extract_challenge_info(data)
                if challenge_info:
                    log_challenge_info(challenge_info, challenge_log_file)
                else:
                    with open(broken_items_file, "a") as broken_f:
                        broken_f.write(f"{json_file}\n")
