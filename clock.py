import tkinter as tk
import time
import math

def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Update analog clock hands
    update_analog_hand(hour_hand, hours * 30 + minutes * 0.5)
    update_analog_hand(minute_hand, minutes * 6)
    update_analog_hand(second_hand, seconds * 6)

    # Update digital clock
    current_time_str = time.strftime("%H:%M:%S", current_time)
    current_time_label.config(text=current_time_str)

    root.after(1000, update_clock)

def update_analog_hand(hand, angle):
    x = center_x + hand_length * math.cos(math.radians(90 - angle))
    y = center_y - hand_length * math.sin(math.radians(90 - angle))
    analog_canvas.coords(hand, center_x, center_y, x, y)

def toggle_clock_type():
    analog_visible = analog_frame.winfo_ismapped()
    
    if analog_visible:
        analog_frame.pack_forget()
        digital_frame.pack()
    else:
        digital_frame.pack_forget()
        analog_frame.pack()

root = tk.Tk()
root.title("Clock App")

# Create a frame for the analog clock
analog_frame = tk.Frame(root)

# Create a label for the analog clock
analog_label = tk.Label(analog_frame, text="Analog Clock")

# Create a canvas for the analog clock
analog_canvas = tk.Canvas(analog_frame, width=300, height=300)

# Analog clock constants
center_x = 150
center_y = 150
clock_radius = 100
hand_length = 80

# Create clock circle
analog_canvas.create_oval(center_x - clock_radius, center_y - clock_radius,
                          center_x + clock_radius, center_y + clock_radius, outline="black")

# Create numbers and lines on the clock face
for i in range(1, 13):
    angle = math.radians(90 - i * 30)
    number_x = center_x + (clock_radius - 20) * math.cos(angle)
    number_y = center_y - (clock_radius - 20) * math.sin(angle)
    analog_canvas.create_text(number_x, number_y, text=str(i), font=("Helvetica", 12))
    
    line_x1 = center_x + (clock_radius - 5) * math.cos(angle)
    line_y1 = center_y - (clock_radius - 5) * math.sin(angle)
    line_x2 = center_x + (clock_radius - 15) * math.cos(angle)
    line_y2 = center_y - (clock_radius - 15) * math.sin(angle)
    analog_canvas.create_line(line_x1, line_y1, line_x2, line_y2, width=2)

# Create analog clock hands
hour_hand = analog_canvas.create_line(center_x, center_y, center_x, center_y, width=5)
minute_hand = analog_canvas.create_line(center_x, center_y, center_x, center_y, width=3)
second_hand = analog_canvas.create_line(center_x, center_y, center_x, center_y, width=1)

analog_canvas.pack()

# Create a frame for the digital clock
digital_frame = tk.Frame(root)

# Create a label for the digital clock
digital_label = tk.Label(digital_frame, text="Digital Clock", font=("Helvetica", 16))

# Create a label for the current time
current_time_label = tk.Label(digital_frame, text="00:00:00", font=("Helvetica", 24))

digital_label.pack()
current_time_label.pack()

# Create a button to toggle the clock type
clock_type_button = tk.Button(root, text="Toggle Clock Type", command=toggle_clock_type)
clock_type_button.pack()

# Pack the frames
analog_frame.pack()
digital_frame.pack()

# Start updating the clocks
update_clock()

# Start the main loop
root.mainloop()
