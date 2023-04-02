def check_response(response):
    for key, value in response.items():
        print(key, value)
        print('')
    
        
def save_response(response, name, path):
    # path = os.environ['ROOT']'
    
    # save the timeline
    with open(f'{path}/_data/timelines/{name.lower()}.yml', 'w') as f:
        f.write(response['timeline'])
        
    # create the .md file
    with open(f'{path}/src/name.md.temp', 'r') as f:
        md_template = f.readlines()
        
    updated_md = []
    for line in md_template:
        if line.startswith('name:'):
            updated_md.append(f'name: {name}\n')
        elif line.startswith('character:'):
            updated_md.append(f'character: {name.lower()}\n')
        elif line.startswith('description:'):
            updated_md.append(f"description: {response['basic_intro']}\n")
        elif line.startswith('url:'):
            updated_md.append(f"url: /characters/{name.lower()}\n")
        elif line.startswith('image:'):
            updated_md.append(f"image: {name.lower()}.png\n")
        else:
            updated_md.append(line)
            
    updated_md.append(response["description"])
            
    with open(f'{path}/_characters/{name.lower()}.md', 'w') as f:
        f.writelines(updated_md)

        
        