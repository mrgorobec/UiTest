import os
import yaml


def read_from_yaml(file_name):
    with open(resolve_file_path(file_name)) as f:
        data = yaml.load(f)
        return data


def resolve_file_path(file_name):
    return os.path.join(project_root, file_name)


project_root = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

environment = read_from_yaml('config/enviroment_config.yaml')


