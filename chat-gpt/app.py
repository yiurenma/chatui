# pip3 install openai
# pip3 install pyngrok
# pip3 install flask_ngrok
# pip3 install -U flask-cors
from flask import Flask, render_template
import os
import openai
from flask import request

os.environ["FLASK_DEBUG"] = "development"
app = Flask(__name__)
# port = 5000

# max_len = 10
# messages=[]
def greatAI(input):
  # if len(messages) >= max_len:
  #   messages.pop(0)
  # messages.append({'role': 'user', 'content': input})
  openai.api_key = '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'
  # print(messages)
  print(input)
  response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo-0301',
    # messages = messages
    messages = [{'role': 'user', 'content': input}]
  )
  # if len(messages) >= max_len:
  #     messages.pop(0)
  # messages.append({'role': 'assistant', 'content': response.choices[0].message.content})
  return response

@app.route("/chat")
def index():
  return greatAI(request.args.get('text'))

if __name__ == '__main__':
  # run app in debug mode on port 5000
  app.run(debug=True, port=5000, host='0.0.0.0')


