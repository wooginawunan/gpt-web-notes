# %%
import os, sys
import openai
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import save_response, check_response
# openai.organization = "org-aQCFZvZK0fuWYMTKkfMmrNVK"
openai.api_key = os.getenv("OPENAI_API_KEY")
gpt_version = 'gpt-3.5-turbo'
max_rounds = 5

assert os.environ['ROOT']=='/Users/nanwu/Desktop/ResearchProjects/GPT'

class ContentGenerator:
    def __init__(self, model, prompts, fields):
        
        self.prompts = prompts
        self.model = model
        self.fields = fields
        
    def generate(self, name):
        self.context = []
        response = dict.fromkeys(self.fields)
        prompts = [x.replace('$NAME$', name) for x in self.prompts]
        
        for field, prompt in zip(self.fields, prompts):
            self.context.append({"role": "user", "content":  prompt})
            
            completion = openai.ChatCompletion.create(
                model=self.model,
                messages=self.context
            )
            message = completion.choices[0].message
            
            self.context.append(message)
            response[field] = message["content"]
            
        return response

# %%

if __name__=='__main__':
    
    # Load the JSON file of character
    with open(f'{os.environ["ROOT"]}/src/characters.json', 'r') as f:
        data = json.load(f)
    characters = data['characters']

    print("All characters in DST:\n\t", '\n\t'.join(characters))

    # Load the JSON file of character
    with open(f'{os.environ["ROOT"]}/src/prompts.json', 'r') as f:
        prompts = json.load(f)

    prompts_templates = [value for key, value in prompts.items()]
    fields = [key for key, value in prompts.items()]
    
    gpt_generator = ContentGenerator(gpt_version, prompts_templates, fields)
    for name in characters:
        with_timeline = False
        round_counts = 1
        while not with_timeline and (round_counts<=max_rounds):
            print(f'Generation round {round_counts}...')
            response = gpt_generator.generate(name)   
            if ("```" in response['timeline']) or ("- day:" in response["timeline"]):
                with_timeline = True
                print(f'timeline included!')
            round_counts += 1
            check_response(response)

        response['timeline'] = response['timeline'].split("```")[1].replace("yaml", "")

        save_response(response, name, os.environ['ROOT'])
        print(f'Character {name} is generated!')

# %%
""