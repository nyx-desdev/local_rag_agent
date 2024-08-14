import ollama 

# output = ollama.generate(model='llama3.1', prompt='Who is the prime minister on India?')
# response = output['response']

# print(response)

convo = []

def stream_content(prompt):
    convo.append({ 'role': 'user', 'content' : prompt})
    response = ''
    stream =  ollama.chat(model='llama3.1', messages=convo, stream=True)
    
    print('\nAssitant:')
    
    for chunk in stream: 
        content = chunk['message']['content']
        response += content
        print(content, end='', flush=True)
        
    print('\n')
    convo.append({'role': 'assistant', 'content': response})
    
while True:
    prompt = input('User: \n')
    stream_content(prompt)
