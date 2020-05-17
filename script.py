import json
import yaml

with open('input.json') as file:
    data = json.load(file)
    
print(json.dumps(data, indent=2))

print(data['status'])



with open('output.json', 'w') as file:
    json.dump(data, file, indent=2)



with open('output.yaml', 'w') as file:
    yaml.dump(data, file, indent=2)



with open('mkarimi.json', 'w') as file:
    data['owner'] = 'Mohammad Karimi'
    json.dump(data, file, indent=2)


