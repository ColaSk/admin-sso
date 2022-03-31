import json

def read_json(filepath: str):
    """读取接送文件"""
    with open(filepath, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data


