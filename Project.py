import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to add a new exercise entry
def add_exercise():
    frame = tk.Frame(window)
    frame.pack(pady=5)

    label = tk.Label(frame, text=f"Choose exercise {len(exercise_frames) + 1}:")
    label.pack(side=tk.LEFT)

    exercise_dropdown = ttk.Combobox(frame, values=choices)
    exercise_dropdown.pack(side=tk.LEFT, padx=5)

    sets_label = tk.Label(frame, text="Sets:")
    sets_label.pack(side=tk.LEFT)
    sets_entry = tk.Entry(frame, width=5)
    sets_entry.pack(side=tk.LEFT, padx=5)

    reps_label = tk.Label(frame, text="Reps:")
    reps_label.pack(side=tk.LEFT)
    reps_entry = tk.Entry(frame, width=5)
    reps_entry.pack(side=tk.LEFT, padx=5)

    weight_label = tk.Label(frame, text="Weight (lbs):")
    weight_label.pack(side=tk.LEFT)
    weight_entry = tk.Entry(frame, width=5)
    weight_entry.pack(side=tk.LEFT, padx=5)

    exercise_frames.append((exercise_dropdown, sets_entry, reps_entry, weight_entry))

# Function to calculate the total volume lifted
def calculate_total_volume():
    total_volume = 0
    for exercise_dropdown, sets_entry, reps_entry, weight_entry in exercise_frames:
        try:
            sets = int(sets_entry.get())
            reps = int(reps_entry.get())
            weight = float(weight_entry.get())

            total_volume += sets * reps * weight
        except ValueError:
            pass  # Ignore invalid inputs

    total_volume_label.config(text=f"Total Volume Lifted: {total_volume:} lbs")

# Function to store the workout
def complete_workout():
    workout = []
    for exercise_dropdown, sets_entry, reps_entry, weight_entry in exercise_frames:
        try:
            exercise = exercise_dropdown.get()
            sets = int(sets_entry.get())
            reps = int(reps_entry.get())
            weight = float(weight_entry.get())
            workout.append((exercise, sets, reps, weight))
        except ValueError:
            continue  # Ignore invalid inputs

    if workout:
        workouts.append(workout)
        messagebox.showinfo("Workout Saved", "Your workout has been saved!")
        clear_entries()
    else:
        messagebox.showwarning("No Data", "Please enter at least one valid exercise.")

# Function to clear the current entries
def clear_entries():
    for exercise_dropdown, sets_entry, reps_entry, weight_entry in exercise_frames:
        exercise_dropdown.set('')
        sets_entry.delete(0, tk.END)
        reps_entry.delete(0, tk.END)
        weight_entry.delete(0, tk.END)
    

# Function to view previous workouts
def view_previous_workouts():
    if not workouts:
        messagebox.showinfo("Previous Workouts", "No workouts recorded.")
        return

    previous_workouts = "\n\n".join(
        [f"Workout {i + 1}:\n" + "\n".join([f"{ex[0]}: {ex[1]} sets, {ex[2]} reps, {ex[3]} lbs" for ex in workout]) 
         for i, workout in enumerate(workouts)]
    )
    messagebox.showinfo("Previous Workouts", previous_workouts)

# Create main window
window = tk.Tk()
window.geometry("600x400")
window.title("Workout Tracker App")
window.config(bg="Black")

# Label for the app
label = tk.Label(window, text="Workout Tracker", bg="Black", fg="White", font=('Arial', 14))
label.pack(pady=10)

# Exercise choices
choices = ['Benchpress', 'Squat', 'Deadlift', 'Pullups', 'Pushups', 'Situps']

# List to store the exercise dropdowns and their respective entries
exercise_frames = []
workouts = []  # List to store completed workouts

# Button to add new exercise dropdown
add_button = tk.Button(window, text="Add Exercise", command=add_exercise)
add_button.pack(pady=10)

# Button to calculate total volume lifted
calculate_button = tk.Button(window, text="Calculate Total Volume", command=calculate_total_volume)
calculate_button.pack(pady=10)

# Button to complete workout
complete_button = tk.Button(window, text="Complete Workout", command=complete_workout)
complete_button.pack(pady=10)

# Button to view previous workouts
view_button = tk.Button(window, text="View Previous Workouts", command=view_previous_workouts)
view_button.pack(pady=10)

# Label to display total volume lifted
total_volume_label = tk.Label(window, text="Total Volume Lifted: 0 lbs", bg="Black", fg="White", font=('Arial', 12))
total_volume_label.pack(pady=10)

# Start the main event loop
window.mainloop()
