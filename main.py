import os  # noqa: I001
import requests
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

API_ORIGIN = os.environ["API_ORIGIN"]

def apiCall(message, *args):
    response = requests.post(
        url=API_ORIGIN + '/llm',
        json={
            "message":message
        }
    )
    print(response.json())
    return response.json()['message']


demo = gr.ChatInterface(fn=apiCall)
if __name__ == "__main__":
    demo.launch(server_port=7860)
