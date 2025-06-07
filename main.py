import subprocess
from simulation_methods import euler, heun


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

    result, heater_states = euler(t_amb, k, q, turn_on, turn_off, num_steps, initial_temp, h)

    # Print the result temperatures
    with open("results.txt", "w") as f:
        for i, (temp, heater) in enumerate(zip(result, heater_states)):
            state = "ON" if heater == 1 else "OFF"
            print(f"Step {i}: {temp} ({state})")
            f.write(f"{i} {temp} {state}\n")

    # Create Gnuplot script
    gnuplot_script = """set terminal png size 800,600
        set output 'grafico.png'
        set xlabel 'Tiempo (s)'
        set ylabel 'Temperatura (°C)'
        set title 'Evolución de la Temperatura T(n)'
        set grid
        plot "results.txt" using ($1/10.0):2 with lines lw 2 lc rgb "red" title "Temperatura"
        set output
        """

    with open("plot.gp", "w") as script_file:
        script_file.write(gnuplot_script)

    # Execute Gnuplot
    subprocess.run(["gnuplot", "plot.gp"])
