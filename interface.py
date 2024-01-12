"""
File: interface.py
Author: Paul Cheung
Date: 2023-7-21 Fri.
Location: Hundsun Center C2417

Description:
    1. 该脚本接收用户的多行输入并调用 openai2.py 中的 chat_openai_v11 函数
"""

import openai2


def multi_line_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return '\n'.join(lines)


if __name__ == "__main__":
    while True:
        try:
            user_input = multi_line_input(">>Prompt: (Press ENTER on an empty line to send)")
            response = openai2.chat_openai_v11(user_input)
            print('>>Response: \n' + response + '\n')
            print('-' * 75)
        except KeyboardInterrupt:
            print("Exit.")
            break
