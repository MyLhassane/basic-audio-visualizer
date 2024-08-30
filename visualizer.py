from pydub import AudioSegment
from pydub.utils import make_chunks
import matplotlib.pyplot as plt
import numpy as np

# Load your song (replace 'your_song.mp3' with the actual file path)
song = AudioSegment.from_file("your_song.mp3")

# Break the song into chunks (e.g., 50ms)
chunk_length_ms = 50
chunks = make_chunks(song, chunk_length_ms)

# Calculate the volume (RMS) for each chunk
volumes = [chunk.rms for chunk in chunks]

# Create a time axis in seconds
time_axis = np.linspace(0, len(song) / 1000.0, num=len(volumes))

# Plot the volume data
plt.figure(figsize=(12, 6))
plt.plot(time_axis, volumes)
plt.xlabel("Time (s)")
plt.ylabel("Volume (RMS)")
plt.title("Basic Volume Visualizer")
plt.show()
