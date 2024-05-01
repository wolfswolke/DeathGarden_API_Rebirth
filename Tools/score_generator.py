import random
import string


def generate_player_id():
    letters = string.ascii_lowercase
    return '-'.join([''.join(random.choice(letters) for _ in range(1)),
                     ''.join(random.choice(string.digits) for _ in range(1)),
                     ''.join(random.choice(letters) for _ in range(1)),
                     ''.join(random.choice(string.digits) for _ in range(1))])


def generate_player_name():
    names = ["Mark", "John", "Emily", "Sarah", "David", "Michael", "Lisa", "Jennifer", "Chris", "Alex"]
    return random.choice(names)


def generate_entries(num_entries):
    entries = []
    rank = 0
    for _ in range(num_entries):
        player_id = generate_player_id()
        player_name = generate_player_name()
        rank = rank + 1
        # rank = random.randint(1, 10)  # Scaled from 1 to 10
        score = random.randint(1, 10)  # Scaled from 1 to 10
        # percentile = random.randint(1, 100)  # Scaled from 1 to 100
        entry = {
            "Id": player_id,
            "Score": score,
            "Rank": rank,
            "PlayerName": player_name
        }
        entries.append(entry)
    return entries


# Generate 50 entries
num_entries = 50
entries = generate_entries(num_entries)

# Print the entries
for entry in entries:
    entry = str(entry).replace("'", "\"")
    print(f"{entry},")
