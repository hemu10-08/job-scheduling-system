import matplotlib.pyplot as plt

class Job:
    def __init__(self, name, arrival, burst, priority=0):
        self.name = name
        self.arrival = arrival
        self.burst = burst
        self.priority = priority
        self.remaining = burst
        self.completion = 0
        self.turnaround = 0
        self.waiting = 0

def fcfs(jobs):
    jobs.sort(key=lambda x: x.arrival)
    time = 0
    timeline = []
    for job in jobs:
        if time < job.arrival:
            time = job.arrival
        start = time
        time += job.burst
        job.completion = time
        job.turnaround = job.completion - job.arrival
        job.waiting = job.turnaround - job.burst
        timeline.append((job.name, start, time))
    return jobs, timeline

def sjf(jobs):
    jobs.sort(key=lambda x: (x.arrival, x.burst))
    time, completed = 0, []
    ready = []
    timeline = []
    while jobs or ready:
        while jobs and jobs[0].arrival <= time:
            ready.append(jobs.pop(0))
        if ready:
            ready.sort(key=lambda x: x.burst)
            job = ready.pop(0)
            start = time
            time += job.burst
            job.completion = time
            job.turnaround = job.completion - job.arrival
            job.waiting = job.turnaround - job.burst
            completed.append(job)
            timeline.append((job.name, start, time))
        else:
            time += 1
    return completed, timeline

def priority_scheduling(jobs):
    jobs.sort(key=lambda x: (x.arrival, x.priority))
    time, completed, ready = 0, [], []
    timeline = []
    while jobs or ready:
        while jobs and jobs[0].arrival <= time:
            ready.append(jobs.pop(0))
        if ready:
            ready.sort(key=lambda x: x.priority)
            job = ready.pop(0)
            start = time
            time += job.burst
            job.completion = time
            job.turnaround = job.completion - job.arrival
            job.waiting = job.turnaround - job.burst
            completed.append(job)
            timeline.append((job.name, start, time))
        else:
            time += 1
    return completed, timeline

def round_robin(jobs, quantum=2):
    time, completed = 0, []
    queue = []
    timeline = []
    jobs.sort(key=lambda x: x.arrival)
    while jobs or queue:
        while jobs and jobs[0].arrival <= time:
            queue.append(jobs.pop(0))
        if queue:
            job = queue.pop(0)
            start = time
            if job.remaining > quantum:
                time += quantum
                job.remaining -= quantum
                queue.append(job)
                timeline.append((job.name, start, time))
            else:
                time += job.remaining
                job.remaining = 0
                job.completion = time
                job.turnaround = job.completion - job.arrival
                job.waiting = job.turnaround - job.burst
                completed.append(job)
                timeline.append((job.name, start, time))
        else:
            time += 1
    return completed, timeline

def draw_gantt(timeline, title):
    fig, gnt = plt.subplots()
    gnt.set_title(title)
    gnt.set_xlabel("Time")
    gnt.set_ylabel("Jobs")
    gnt.set_yticks([15])
    gnt.set_yticklabels(["Jobs"])
    colors = {}
    for i, (name, start, end) in enumerate(timeline):
        if name not in colors:
            colors[name] = f"C{i}"
        gnt.broken_barh([(start, end - start)], (10, 10), facecolors=colors[name])
        gnt.text((start + end) / 2, 15, name, ha="center", va="bottom")
    plt.savefig("gantt_chart.png")  # Save Gantt chart as PNG
    plt.show()

if __name__ == "__main__":
    jobs = [
        Job("J1", 0, 5, 2),
        Job("J2", 1, 3, 1),
        Job("J3", 2, 8, 3),
        Job("J4", 3, 6, 2)
    ]

    print("Choose Scheduling Algorithm:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Priority")
    print("4. Round Robin")
    choice = int(input("Enter choice (1-4): "))

    if choice == 1:
        result, timeline = fcfs(jobs)
        title = "First Come First Serve (FCFS)"
    elif choice == 2:
        result, timeline = sjf(jobs)
        title = "Shortest Job First (SJF)"
    elif choice == 3:
        result, timeline = priority_scheduling(jobs)
        title = "Priority Scheduling"
    elif choice == 4:
        q = int(input("Enter Time Quantum: "))
        result, timeline = round_robin(jobs, q)
        title = "Round Robin"
    else:
        print("Invalid Choice")
        exit()

    # Print results to console
    print("\nJob\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting")
    for j in result:
        print(f"{j.name}\t{j.arrival}\t{j.burst}\t{j.priority}\t\t{j.completion}\t\t{j.turnaround}\t\t{j.waiting}")

    # Save console output to a text file
    with open("example_output.txt", "w") as f:
        f.write("Job\tArrival\tBurst\tPriority\tCompletion\tTurnaround\tWaiting\n")
        for j in result:
            f.write(f"{j.name}\t{j.arrival}\t{j.burst}\t{j.priority}\t{j.completion}\t{j.turnaround}\t{j.waiting}\n")

    # Draw and save Gantt chart
    draw_gantt(timeline, title)

