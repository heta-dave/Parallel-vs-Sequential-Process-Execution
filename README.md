# Process Splitting & Execution Simulation

This project demonstrates the benefits of splitting a process into multiple threads versus executing tasks sequentially. Two versions of the simulation are provided:

1. **HTML/JavaScript Version:**  
   A web-based simulation that visually compares parallel and sequential execution using progress bars. Tailwind CSS is used for styling.

2. **Python Version:**  
   A desktop simulation built with Python and Tkinter that illustrates how a process can be split into threads and executed concurrently or sequentially.

---

## Features

- **Process Splitting:**  
  Simulate splitting a process into multiple threads (tasks) with each thread assigned a random processing time (cycles).

- **Parallel Execution Simulation:**  
  Each thread has its own progress bar updating concurrently. The overall simulated finish time is approximately equal to the longest individual task.

- **Sequential Execution Simulation:**  
  Tasks are executed one after another, shown via a single cumulative progress bar. The total time equals the sum of all tasks.

- **Visual Comparison:**  
  Both panels display execution times so you can easily see the benefit of parallel execution over sequential processing.

- **Modern UI (HTML version):**  
  Uses Tailwind CSS for a beautiful, responsive design.

---

## Prerequisites

### HTML/JavaScript Version

- A modern web browser (Chrome, Firefox, Edge, Safari, etc.)
- An internet connection to load Tailwind CSS via CDN.

### Python Version

- Python 3.x installed on your system.
- Tkinter (usually included with Python on Windows/macOS; on Linux, install with, for example, `sudo apt-get install python3-tk`).

---

## Installation & Running

### HTML/JavaScript Version

1. **Clone the Repository or Download Files:**
   - Ensure you have the `index.html` file in your project directory.

2. **Open in Browser:**
   - Simply open the `index.html` file in your favorite web browser.

3. **Usage:**
   - Click **"Split Process into Threads"** to generate simulated threads.
   - Click **"Simulate Parallel Execution"** to see individual progress bars update concurrently.
   - Click **"Simulate Sequential Execution"** to see a single cumulative progress bar run through the tasks sequentially.
   - Click **"Reset"** to clear the simulation and try again.

### Python Version

1. **Clone the Repository or Download Files:**
   - Ensure you have the `simulation.py` file in your project directory.

2. **Run the Script:**
   - Open a terminal or command prompt and execute:
     ```bash
     python3 simulation.py
     ```

3. **Usage:**
   - Use the buttons in the Tkinter window to split the process, simulate parallel execution, simulate sequential execution, or reset the simulation.

---

## Project Structure

