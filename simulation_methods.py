# Global flag to remember the last derivative used
last_derivative = 0

def differential_equation(current_temp, ambient_temp, k, q, turn_on, turn_off):
    global last_derivative

    if current_temp < turn_on:
        last_derivative = 0
        return -k * (current_temp - ambient_temp) + q
    elif current_temp > turn_off:
        last_derivative = 1
        return -k * (current_temp - ambient_temp)
    else:
        if last_derivative == 0:
            # Continue heating
            return -k * (current_temp - ambient_temp) + q
        else:
            # Continue cooling
            return -k * (current_temp - ambient_temp)


def euler(ambient_temp, k, q, turn_on, turn_off, num_steps, initial_temp, h):
    global last_derivative

    # Preallocate the list of temperatures

    # Initialize temperatures' array with all 0.0
    # Array's size is num_steps
    temperatures = [0.0] * (int(num_steps / h) + 1)
    temperatures[0] = initial_temp

    # Array to save the heater status (1: on, 0: off)
    heater_states = [0] * (int(num_steps / h) + 1)

    # Initialize last_derivative based on the initial temperature
    if initial_temp < turn_on:
        last_derivative = 0
        heater_states[0] = 1
    elif initial_temp > turn_off:
        last_derivative = 1
        heater_states[0] = 0
    else:
        heater_states[0] = 1 if last_derivative == 0 else 0

    for i in range(int(num_steps/h)):
        temperatures[i + 1] = temperatures[i] + h * differential_equation(
            temperatures[i],
            ambient_temp,
            k,
            q,
            turn_on,
            turn_off
        )
        # Save heater state after updating last_derivative
        heater_states[i + 1] = 1 if last_derivative == 0 else 0

    return temperatures, heater_states
