import requests
from datetime import datetime

USERNAME = "ahsan112"
TOKEN = "adkfhaodkgj23432afaksdjf"

pixela_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# graph_config = {
#     "id": "graph1",
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "momiji"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_post_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometers did you run today? "),
}

response = requests.post(url=post_endpoint, json=pixel_post_config, headers=headers)
print(response.text)

# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# pixel_pre_config = {
#     "quantity": "4.21",
# }
# response = requests.put(url=update_endpoint, json=pixel_pre_config, headers=headers)
# print(response.text)


# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
