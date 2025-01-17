import json
import yaml

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def filter_strings(strings, whitelist):
    filtered_strings = {}
    for path, keys in whitelist.items():
        if path in strings:
            filtered_strings[path] = {key: strings[path][key] for key in keys if key in strings[path]}
    return filtered_strings

def main():
    whitelist_path = 'whitelist.yaml'
    strings_path = 'string.json'
    output_path = 'filtered_string.json'

    whitelist = load_yaml(whitelist_path)
    strings = load_json(strings_path)

    filtered_strings = filter_strings(strings, whitelist)

    save_json(filtered_strings, output_path)
    print(f'Filtered strings saved to {output_path}')

if __name__ == '__main__':
    main()
