import yaml

def load_topics(filepath='config/topics.yaml'):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    return data['topics']