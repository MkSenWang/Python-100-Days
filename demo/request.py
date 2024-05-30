import requests

def get_app_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    payload = {"app_id": app_id, "app_secret": app_secret}
    response = requests.post(url, json=payload)
    return response.json().get("app_access_token")

def list_chats(access_token):
    url = "https://open.feishu.cn/open-apis/chat/v4/list"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers)
    return response.json()

# 使用示例
app_id = 'cli_a5a74dcaa1f8d02d'
app_secret = 'KCcwl5oDvr0q7Qu8mxyTkdks3NmzQOXh'

access_token = get_app_access_token(app_id, app_secret)
chats = list_chats(access_token)
print(chats)