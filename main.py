from simulation_methods import euler


def read_parameters(filename):
    parameters = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)
                parameters[key.strip()] = value.strip()

    return parameters


if __name__ == "__main__":

    file = 'parameters.txt'
    parameters = read_parameters(file)

    for key, value in parameters.items():
        print(f"{key}: {value}")

    # Convert string parameters to appropriate types
    t_amb = float(parameters["t_amb"])
    k = float(parameters["k"])
    q = float(parameters["q"])
    turn_on = float(parameters["t_on"])
    turn_off = float(parameters["t_off"])
    num_steps = int(parameters["sim_time"])
    initial_temp = float(parameters["t_0"])
    h = float(parameters["h"])

    result = euler(t_amb, k, q, turn_on, turn_off, num_steps, initial_temp, h)

    # Print the result temperatures
    for i, temp in enumerate(result):
        print(f"Step {i}: {temp}")
