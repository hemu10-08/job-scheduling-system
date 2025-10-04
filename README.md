# Job Scheduling System

A **Python program** that simulates different **job scheduling algorithms** commonly used in operating systems. It also displays a **Gantt chart** to visualize the scheduling of jobs.

## Features

- Supports multiple scheduling algorithms:
  - **First Come First Serve (FCFS)**
  - **Shortest Job First (SJF)**
  - **Priority Scheduling**
  - **Round Robin (RR)**
- Calculates:
  - Completion Time
  - Turnaround Time
  - Waiting Time
- Visualizes job execution using **Gantt Chart** ('matplotlib')

---

## Installation

1. Make sure you have **Python 3.x** installed.
2. Install the required library:
   
   pip install matplotlib
   
   HOW TO RUN

1.Open the project folder.

2.Run the Python file:

python job_scheduling.py

3.Follow the on-screen prompts:

Enter the number corresponding to the scheduling algorithm:

1 → FCFS

2 → SJF

3 → Priority

4 → Round Robin

If Round Robin, enter the time quantum.

4.View the results:

Console output in IDLE/terminal

Saved example_output.txt

Saved Gantt chart in gantt_chart.png


Example Output

Console output (also saved in example_output.txt):
Job    Arrival    Burst    Priority    Completion    Turnaround    Waiting
J1       0         5         2           5            5            0
J2       1         3         1           8            7            4
J3       2         8         3          16           14            6
J4       3         6         2          22           19           13
Gantt chart is saved automatically as gantt_chart.png

TECH STACK

Python 3.x

matplotlib (for Gantt chart visualization)

AUTHOR
 HEMACHANDRAN NANDAKUMAR
 EMAIL:Hemac7692@gmail.com
 GITHUB:: https://github.com/hemu10-08
