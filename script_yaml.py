import yaml

with open('constants.yaml', 'r') as constants:
    vars = yaml.safe_load(constants)
    print(vars.get('browsers'))
