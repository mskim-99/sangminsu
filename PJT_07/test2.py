# import requests
# from requests.auth import HTTPBasicAuth
# from urllib.parse import urlencode

# # 인증 URL
# auth_url = "https://accounts.spotify.com/api/token"

# # 클라이언트 ID와 시크릿
# client_id = "3c9d7c27a8fc4870ad2ee601957018e7"
# client_secret = "92b5af97fffc47b9821989244352c48e"

# # 인증 요청
# auth = HTTPBasicAuth(client_id, client_secret)
# data = {
#     "grant_type": "client_credentials"
# }
# response = requests.post(auth_url, data=data, auth=auth)


# token = response.json().get("access_token")

# print(f"Access Token: {token}")


# headers = {
#     "Authorization": f"Bearer {token}"
# }

# params = {
#     "seed_genres": "rock",
#     "limit": 10,
# }

# rec_url = f"https://api.spotify.com/v1/recommendations?{urlencode(params)}"
# print('checkpoint1')
# rec_response = requests.get(rec_url, headers=headers, params=params)
# print('checkpoint2')
# # 응답 상태 코드 확인
# if rec_response.status_code != 200:
#     print(f"Error: {rec_response.status_code} - {rec_response.text}")
# # else:
# #     token = response.json().get("access_token")
# #     print(f"Access Token: {token}")


# recommendations = rec_response.json()

# for track in recommendations["tracks"]:
#     print(track["name"], "-", track["artists"][0]["name"])


# print(rec_response.text)  # 응답 본문 출력


#---------------------------------------
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode

# 인증 URL
auth_url = "https://accounts.spotify.com/api/token"

# 클라이언트 ID와 시크릿
client_id = "3c9d7c27a8fc4870ad2ee601957018e7"
client_secret = "92b5af97fffc47b9821989244352c48e"

# 인증 요청
auth = HTTPBasicAuth(client_id, client_secret)
data = {
    "grant_type": "client_credentials"
}
response = requests.post(auth_url, data=data, auth=auth)

# 인증 상태 코드 확인
if response.status_code != 200:
    print(f"Error: {response.status_code} - {response.text}")
    exit()  # 인증 실패 시 종료

token = response.json().get("access_token")

# 토큰이 없으면 종료
if not token:
    print("Error: No access token received")
    exit()

print(f"Access Token: {token}")

headers = {
    "Authorization": f"Bearer {token}"
}

params = {
    "seed_genres": "rock",
    "limit": 10,
}

# API 요청 URL
rec_url = "https://api.spotify.com/v1/recommendations"
rec_response = requests.get(rec_url, headers=headers, params=params)

# 응답 상태 코드 확인
print(f"Response status: {rec_response.status_code}")

# 응답이 200일 때만 JSON 처리
if rec_response.status_code == 200:
    try:
        recommendations = rec_response.json()
        for track in recommendations["tracks"]:
            print(track["name"], "-", track["artists"][0]["name"])
    except KeyError:
        print("Error: 'tracks' not found in response.")
        print(rec_response.json())  # 실제 응답 본문을 출력하여 문제를 진단
else:
    print(f"Error: {rec_response.status_code} - {rec_response.text}")