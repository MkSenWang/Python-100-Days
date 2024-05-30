import requests

def get_access_token(app_id, app_secret):
    url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    payload = {
        "app_id": app_id,
        "app_secret": app_secret
    }
    response = requests.post(url, json=payload)
    return response.json()['app_access_token']

def get_chat_members(chat_id, access_token):
    url = f"https://open.feishu.cn/open-apis/chat/v4/members?chat_id={chat_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

# 使用示例
app_id = 'cli_a5a74dcaa1f8d02d'
app_secret = 'KCcwl5oDvr0q7Qu8mxyTkdks3NmzQOXh'
chat_id = 'oc_9de5980208df520f0e4e3b3b43832674'

access_token = get_access_token(app_id, app_secret)
members_info = get_chat_members(chat_id, access_token)
print(members_info)