from rich import print

from participant import load_participants

data_path = "data/datathon_participants.json"
participants = load_participants(data_path)

print(participants[0])
