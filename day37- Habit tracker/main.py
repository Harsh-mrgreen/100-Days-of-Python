from datetime import datetime
import requests
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "harshvsingh"
TOKEN = "q1w2e3r4t5y669329wekf"
GRAPH_ID = "graph1"
# setting up user account on pixela

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

#create a graph
graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "ajisai"
}
# we are creating headers to not use the usual api key method due to safty concerns
headers = {
    "X-USER-TOKEN": TOKEN
}

#graph_response = requests.post(url = graph_endpoint,json = graph_config, headers= headers)
#print(graph_response.text)

# Adding a pixel using post request.

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

#today = datetime.now()
today  = datetime.now()
#strftime is used to edit the date into any format we want.
pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity": input("how much work did you complete today?"),
    
}
response = requests.post(url = pixel_endpoint, json= pixel_config, headers=headers)
print(response.text)

#updating the pixel using put request

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "3.8"

}

# response = requests.put(url = update_endpoint, json= new_pixel_data, headers=headers)
# print(response.text)


#deleting pixed using delete request

# response = requests.delete(url = update_endpoint, headers=headers)
# print(response.text)