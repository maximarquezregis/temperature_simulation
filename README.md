# Temperature Simulation

&#x20;

## Description

This program simulates the evolution of temperature over time using the **Euler** method and the **Heun** method. The simulation results are automatically plotted and saved as `graphic.png`.

---

## Dependencies

* **Python 3** (version 3.6 or higher)
* **Gnuplot** (version 5.0 or higher)

> Make sure both are installed and available in your system PATH.

---

## Installation

Clone the repository:

   ```bash
   git clone https://github.com/maximarquezregis/temperature_simulation.git
   cd temperature-simulation
   ```

> **Note:** There are currently no additional Python dependencies beyond the standard library.

---

## Simulation Parameters

All simulation parameters are defined in `parameters.txt`. Available settings:

| Parameter  | Description                                    | Default Value |
| ---------- | ---------------------------------------------- | ------------- |
| `t_0`      | Initial temperature (°C)                       | 15            |
| `t_amb`    | Ambient temperature (°C)                       | 5             |
| `t_on`     | Heater activation temperature threshold (°C)   | 18            |
| `t_off`    | Heater deactivation temperature threshold (°C) | 22            |
| `k`        | Heat transfer coefficient (1/second)           | 0.1           |
| `q`        | Heating power constant                         | 4             |
| `h`        | Time step (seconds)                            | 0.1           |
| `sim_time` | Total simulation time (seconds)                | 200           |
| `method`   | Numerical method (`euler`, or `heun`)          | `heun`        |

> Adjust these values in `parameters.txt` as needed and rerun the simulation.

---

## Usage

Run the main script with Python:

```bash
python3 main.py
```

Once complete, the `graphic.png` file will be generated in the project root, showing the temperature vs. time curves for both methods.

---

## Author

Developed by **Máximo Pablo Márquez Regis, Florencia Hernández**.
