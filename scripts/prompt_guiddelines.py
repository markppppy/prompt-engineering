# import openai
import os 
# from tools import get_openai_key 
# from tools import get_completion
from tools import get_completion_from_baidu



# os.environ['HTTPS_PROXY'] = 'https://127.0.0.1:7890'
# os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7890'
# openai.api_key = get_openai_key()

# client = openai.OpenAI()
# get_completion(client, 'hello gpt')

text = f"""
您应该提供尽可能清晰、具体的指示，以表达您希望模型执行的任务。\
这将引导模型朝向所需的输出，并降低收到无关或不正确响应的可能性。\
不要将写清晰的提示词与写简短的提示词混淆。\
在许多情况下，更长的提示词可以为模型提供更多的清晰度和上下文信息，从而导致更详细和相关的输出。
"""

prompt = f"""
把用三个反引号括起来的文本总结成一句话。
```{text}```
"""

text = get_completion_from_baidu(prompt)

print(text['result'])  

""" 完整的响应示例
{'id': 'as-pra1ejvdqy', 'object': 'chat.completion', 'created': 1701600075, 'result': '提供清晰、具体的指示可以帮助模型更好地理解任务，并减少无关或不正确的响应。提示词应该尽可能详细，不要混淆简短和清晰。更长的提示词可以提供更多的清晰度和上下文
信息，导致更详细和相关的输出。', 'is_truncated': False, 'need_clear_history': False, 'finish_reason': 'normal', 'usage': {'prompt_tokens': 93, 'completion_tokens': 51, 'total_tokens': 144}}
"""

