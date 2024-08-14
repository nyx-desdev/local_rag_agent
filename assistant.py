import ollama 

# output = ollama.generate(model='llama3.1', prompt='Who is the prime minister on India?')
# response = output['response']

# print(response)

convo = []

while True:
    prompt = input('User: \n')
    convo.append({ 'role': 'user', 'content' : prompt})
    
    output = ollama.chat(model='llama3.1', messages=convo)
    response = output['message']['content']
    
    print(f'Assitant: \n{response} \n')
    convo.append({'role': 'assistant', 'content': response})