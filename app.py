from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model='gpt-4-vision-preview',
    messages = [
        {
            'role': 'user',
            'content' : [
                {
                    'type' : 'text', 
                    'text': 'What is in this image?'
                },
                {
                    'type' : 'image_url',
                    'image_url': {
                        'url': 'https://static1.squarespace.com/static/607f89e638219e13eee71b1e/60a5de2d343ab05906685029/646c549369f8011c28cd5843/1684821591871/michael-sum-LEpfefQf4rU-unsplash.jpg?format=1500w'
                    },
                },
            ],
    
        }
    ],
    max_tokens=300,
)

print('Completion Tokens:', response.usage.completion_tokens)
print('Prompt Tokens:', response.usage.prompt_tokens)
print('Total Tokens', response.usage.total_tokens)
print(response.choices[0].message)
print(response.choices[0].message.content)
