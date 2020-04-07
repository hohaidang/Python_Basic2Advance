import json
import requests

# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgesuian"
#     }
# }
#
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file, indent=4)
#
# json_string = json.dumps(data, indent=4)
# print(json_string)
#
# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
#
# print(data)

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

todos_by_user = {}

# Increment complete TODOs count for each user.
for todo in todos:
    if todo["completed"]:
        try:
            # Increment the existing user's count.
            todos_by_user[todo["userId"]] += 1
        except KeyError:
            # This user has not been seen. Set their count to 1.
            todos_by_user[todo["userId"]] = 1

top_users = sorted(todos_by_user.items(),
                   key=lambda x: x[1], reverse=True)

max_complete = top_users[0][1]

# Create a list of all users who have completed
# the maximum number of TODOs.
users = []
for user, num_complete in top_users:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = " and ".join(users)
print(max_users)