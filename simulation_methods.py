def differential_equation(current_temp, ambient_temp, k, q, heater_on):
    if heater_on:
        return -k * (current_temp - ambient_temp) + q
    else:
        return -k * (current_temp - ambient_temp)


def euler(ambient_temp, k, q, turn_on, turn_off, num_steps, initial_temp, h):
    # Preallocate the list of temperatures

    # Initialize temperatures' array with all 0.0
    # Array's size is num_steps
    temperatures = [0.0] * (int(num_steps / h) + 1)
    temperatures[0] = initial_temp

    # Array to save the heater status (1: on, 0: off)
    heater_states = [1] * (int(num_steps / h) + 1)

    for i in range(int(num_steps/h)):
        temperatures[i + 1] = temperatures[i] + h * differential_equation(
            temperatures[i],
            ambient_temp,
            k,
            q,
            heater_states[i]
        )
    
        if temperatures[i + 1] < turn_on:
            heater_states[i] = 1
        elif temperatures[i + 1] > turn_off:
            heater_states[i] = 0

        heater_states[i + 1] = heater_states[i]

    return temperatures, heater_states

def heun(ambient_temp, k, q, turn_on, turn_off, num_steps, initial_temp, h):
    # Preallocate the list of temperatures

    # Initialize temperatures' array with all 0.0
    # Array's size is num_steps
    temperatures = [0.0] * (int(num_steps / h) + 1)
    temperatures[0] = initial_temp

    # Array to save the heater status (1: on, 0: off)
    heater_states = [1] * (int(num_steps / h) + 1)

    for i in range(int(num_steps/h)):

        k1 = differential_equation(temperatures[i],
            ambient_temp,
            k,
            q,
            heater_states[i])

        k2 = differential_equation(temperatures[i] + h * k1,
                                   ambient_temp,
                                   k,
                                   q,
                                   heater_states[i])

        temperatures[i + 1] = temperatures[i] + 0.5 * h * (k1 + k2)

        differential_equation(temperatures[i + 1],
            ambient_temp,
            k,
            q,
            heater_states[i])

        # Save heater state
        if temperatures[i + 1] < turn_on:
            heater_states[i] = 1
        elif temperatures[i + 1] > turn_off:
            heater_states[i] = 0

        heater_states[i + 1] = heater_states[i]

    return temperatures, heater_states