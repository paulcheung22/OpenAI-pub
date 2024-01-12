"""
File: openai2.py
Author: Paul Cheung
Date: 2023-7-22 Sat.
Location: Tim Horton

Description:
    1. 这段脚本使用使用ChatGPT API，实现请求和响应；
    2. 参数取自openai.ini；
"""


import openai
import os
import configparser

version = '© GPT35-Turbo | Paul Cheung 2023. v1.00'
# 打印版本号
print(version)
print('=' * 75)

# 读取配置文件
config = configparser.ConfigParser()
config.read('openai2.ini')

# 从配置文件获取参数
OPENAI_API_KEY = config['DEFAULT']['OPENAI_API_KEY']
TEMPERATURE = float(config['OPENAI']['TEMPERATURE'])  # temperature=0.7
MAX_TOKENS = int(config['OPENAI']['MAX_TOKENS'])  # max_tokens=1000
DEPLOYMENT_NAME = config['OPENAI']['DEPLOYMENT_NAME']  # deployment_name="gpt-35-turbo"
OPENAI_API_TYPE = config['OPENAI']['OPENAI_API_TYPE']  # openai.api_type = "azure"
OPENAI_API_BASE = config['OPENAI']['OPENAI_API_BASE']  # openai.api_base = "https://hsai5.openai.azure.com/"
OPENAI_API_VERSION = config['OPENAI']['OPENAI_API_VERSION']  # openai.api_version = "2023-05-15"

# 全局变量用于存储对话历史
chat_history = []


def retrieve_chat_history():
    # 简单地返回全局变量中的对话历史
    return chat_history


def store_chat_history(updated_history):
    # 将更新的对话历史存储到全局变量中
    global chat_history
    chat_history = updated_history


def chat_openai_v11(user_query, deployment_name=DEPLOYMENT_NAME, temperature=TEMPERATURE, max_tokens=MAX_TOKENS):
    openai.api_type = OPENAI_API_TYPE
    deployment_name = deployment_name
    openai.api_base = OPENAI_API_BASE
    openai.api_version = OPENAI_API_VERSION
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Fetch the chat history from a storage or memory
    chat_history = retrieve_chat_history()  # Implement this function according to your use case

    # Append the user query to the chat history
    chat_history.append({"role": "user", "content": user_query})

    # Send the complete chat history to OpenAI API for response
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=chat_history,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Retrieve the response from OpenAI API
    resp = response['choices'][0]['message']['content']

    # Update the chat history with the response received
    chat_history.append({"role": "assistant", "content": resp})

    # Store the updated chat history back to storage or memory for future reference
    store_chat_history(chat_history)  # Implement this function according to your use case

    return resp


if __name__ == "__main__":
    while True:
        try:
            print('-' * 95)
            user_input = input(">>Prompt: \n")
            response = chat_openai_v11(user_input)
            print('\n>>response: \n' + response)
        except KeyboardInterrupt:
            print("Exit")
            break
