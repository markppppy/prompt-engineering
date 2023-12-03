import os
import openai
from dotenv import load_dotenv, find_dotenv
import requests 
import json 

def get_openai_key():
    _ = load_dotenv(find_dotenv())
    return os.environ['OPENAI_API_KEY']

def get_completion(client, prompt, model='gpt-3.5-turbo'):  # , temperature=0
    '''
    用于调用opanai api
    model: 模型选择，可用的有 'gpt-4'、'gpt-3.5-turbo'
    '''
    messages = [{'role': 'user', 'content': prompt}]
    completion = client.chat.completions.create(
      model=model,
      messages=messages
    #   temperature=temperature  # 模型输出的温度系数，控制输出的随即程度
    )
    return completion.choices[0].message['content']

def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    _ = load_dotenv(find_dotenv())
    API_KEY = os.environ['API_KEY']
    SECRET_KEY = os.environ['SECRET_KEY']
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

def get_completion_from_baidu(prompt, temperature=0.95):
    """
    model: ERNIE-Bot-4
    temperature: 较高的数值会使输出更加随机，而较低的数值会使其更加集中和确定
    """
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
        , "temperature": temperature
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return dict(json.loads(response.text))
