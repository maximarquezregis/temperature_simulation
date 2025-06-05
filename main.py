import simulation_methods

def read_parameters(filename):
    parameters = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                parameters[key.strip()] = value.strip()

    return parameters

file = 'parameters.txt'
parameters = read_parameters(file)

for key, value in parameters.items():
    print(f"{key}: {value}")
