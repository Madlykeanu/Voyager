import requests

class LocalLLM:
    def __init__(self, url="http://192.168.1.77:1000/v1/chat/completions"):
        self.url = url

    def send(self, prompt):
        data = {"prompt": prompt}
        response = requests.post(self.url, json=data)
        if response.status_code == 200:
            return response.json()['choices'][0]['text']
        else:
            raise Exception(f"Failed to get response from LLM: {response.text}")