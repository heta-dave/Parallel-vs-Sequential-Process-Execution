import tkinter as tk
from tkinter import ttk
import random
import time

# Colors for thread states.
STATE_COLORS = {
    "Ready": "lightgray",
    "Running": "lightgreen",
    "Completed": "red"
}

# A simple class to represent a simulated thread (task).
class SimulatedThread:
    def __init__(self, tid):
        self.tid = tid
        # Random processing cycles between 3 and 10 seconds.
        self.initial_cycles = random.randint(3, 10)
        self.remaining_cycles = self.initial_cycles

# Main GUI Application.
class ProcessSimulationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Parallel vs Sequential Execution Simulation")
        self.geometry("950x600")
        self.resizable(False, False)

        # Store simulated threads (tasks)
        self.simulated_threads = []

        # Top frame: buttons for process splitting and simulation.
        control_frame = tk.Frame(self)
        control_frame.pack(side=tk.TOP, pady=10)

        self.split_btn = tk.Button(control_frame, text="Split Process into Threads", command=self.split_process)
        self.split_btn.pack(side=tk.LEFT, padx=5)

        self.parallel_btn = tk.Button(control_frame, text="Simulate Parallel Execution", command=self.simulate_parallel, state=tk.DISABLED)
        self.parallel_btn.pack(side=tk.LEFT, padx=5)

        self.sequential_btn = tk.Button(control_frame, text="Simulate Sequential Execution", command=self.simulate_sequential, state=tk.DISABLED)
        self.sequential_btn.pack(side=tk.LEFT, padx=5)

        self.reset_btn = tk.Button(control_frame, text="Reset", command=self.reset_simulation, state=tk.DISABLED)
        self.reset_btn.pack(side=tk.LEFT, padx=5)

        # Middle frame: Two side-by-side panels for simulation.
        sim_frame = tk.Frame(self)
        sim_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left panel for Parallel Simulation.
        parallel_frame = tk.LabelFrame(sim_frame, text="Parallel Execution Simulation", padx=10, pady=10)
        parallel_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.parallel_progress_bars = {}  # Map thread id -> progress bar
        self.parallel_status_label = tk.Label(parallel_frame, text="Total Parallel Time: Not Simulated", font=("Helvetica", 12))
        self.parallel_status_label.pack(side=tk.BOTTOM, pady=5)

        self.parallel_container = tk.Frame(parallel_frame)
        self.parallel_container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Right panel for Sequential Simulation.
        sequential_frame = tk.LabelFrame(sim_frame, text="Sequential Execution Simulation", padx=10, pady=10)
        sequential_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        self.sequential_progress = ttk.Progressbar(sequential_frame, orient="horizontal", mode="determinate")
        self.sequential_progress.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)
        self.sequential_status_label = tk.Label(sequential_frame, text="Total Sequential Time: Not Simulated", font=("Helvetica", 12))
        self.sequential_status_label.pack(side=tk.BOTTOM, pady=5)
        
        # For timing the simulation.
        self.start_time = None

    def split_process(self):
        """Split the process into a fixed number of simulated threads."""
        self.reset_simulation()
        num_threads = 5
        self.simulated_threads = [SimulatedThread(tid=i) for i in range(num_threads)]
        
        # Create progress bars for parallel simulation.
        for st in self.simulated_threads:
            frame = tk.Frame(self.parallel_container)
            frame.pack(pady=5, fill=tk.X)
            label = tk.Label(frame, text=f"Thread {st.tid} (Cycles: {st.initial_cycles})", width=20, anchor="w")
            label.pack(side=tk.LEFT)
            pb = ttk.Progressbar(frame, orient="horizontal", mode="determinate", maximum=st.initial_cycles)
            pb.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
            self.parallel_progress_bars[st.tid] = pb
        
        self.parallel_btn.config(state=tk.NORMAL)
        self.sequential_btn.config(state=tk.NORMAL)
        self.reset_btn.config(state=tk.NORMAL)
        self.split_btn.config(state=tk.DISABLED)

    def simulate_parallel(self):
        """Simulate parallel execution: all threads run concurrently."""
        # Reset progress bars.
        for st in self.simulated_threads:
            self.parallel_progress_bars[st.tid]['value'] = 0
            st.remaining_cycles = st.initial_cycles
        
        self.start_time = time.time()
        self.run_parallel_cycle()

    def run_parallel_cycle(self):
        """Run one cycle for each thread in parallel simulation."""
        done = True
        for st in self.simulated_threads:
            if st.remaining_cycles > 0:
                done = False
                # Simulate one cycle (1 second).
                st.remaining_cycles -= 1
                # Update progress bar.
                current_value = st.initial_cycles - st.remaining_cycles
                self.parallel_progress_bars[st.tid]['value'] = current_value

        if done:
            total_time = time.time() - self.start_time
            self.parallel_status_label.config(text=f"Total Parallel Time: {total_time:.1f} seconds")
            self.parallel_btn.config(state=tk.DISABLED)
        else:
            # Schedule next cycle after 1 second.
            self.after(1000, self.run_parallel_cycle)

    def simulate_sequential(self):
        """Simulate sequential execution: threads run one after another."""
        # Compute total cycles as sum of each thread's cycles.
        total_cycles = sum(st.initial_cycles for st in self.simulated_threads)
        self.sequential_progress['maximum'] = total_cycles
        self.sequential_progress['value'] = 0

        self.start_time = time.time()
        self.run_sequential_cycle(0)

    def run_sequential_cycle(self, current_thread_index):
        """Simulate sequential processing of threads one by one."""
        if current_thread_index >= len(self.simulated_threads):
            total_time = time.time() - self.start_time
            self.sequential_status_label.config(text=f"Total Sequential Time: {total_time:.0f} seconds")
            self.sequential_btn.config(state=tk.DISABLED)
            return

        st = self.simulated_threads[current_thread_index]
        if st.initial_cycles > 0:
            # Simulate one cycle for the current thread.
            st.initial_cycles -= 1
            # Increase overall progress.
            self.sequential_progress['value'] += 1
            self.after(1000, lambda: self.run_sequential_cycle(current_thread_index))
        else:
            # Move to next thread.
            self.after(1000, lambda: self.run_sequential_cycle(current_thread_index + 1))

    def reset_simulation(self):
        """Reset simulation: clear progress bars and reset variables."""
        # Clear parallel container.
        for widget in self.parallel_container.winfo_children():
            widget.destroy()
        self.parallel_progress_bars = {}
        # Reset sequential progress bar.
        self.sequential_progress['value'] = 0
        self.simulated_threads = []
        self.split_btn.config(state=tk.NORMAL)
        self.parallel_btn.config(state=tk.DISABLED)
        self.sequential_btn.config(state=tk.DISABLED)
        self.reset_btn.config(state=tk.DISABLED)
        self.parallel_status_label.config(text="Total Parallel Time: Not Simulated")
        self.sequential_status_label.config(text="Total Sequential Time: Not Simulated")

if __name__ == "__main__":
    app = ProcessSimulationApp()
    app.mainloop()
