import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pydub import AudioSegment
from pydub.utils import make_chunks

# Load your audio file
song = AudioSegment.from_file("your_song.mp3")
chunk_length_ms = 100  # Split audio into chunks of 100ms
chunks = make_chunks(song, chunk_length_ms)

# Calculate RMS values for each chunk
rms_values = [chunk.rms for chunk in chunks]
times = np.arange(len(rms_values))

# Set up the figure and axis
fig, ax = plt.subplots()
line, = ax.plot(times, rms_values, color='purple')

# Animation function
def update(num, rms_values, line):
    line.set_ydata(np.roll(rms_values, -num))  # Shift the data for animation
    return line,

# Setting the limits for the axis
ax.set_ylim(0, max(rms_values))
ax.set_xlim(0, len(rms_values))

# Create the animation
ani = animation.FuncAnimation(
    fig, update, frames=len(rms_values), fargs=(rms_values, line), interval=50, blit=True)

plt.show()
