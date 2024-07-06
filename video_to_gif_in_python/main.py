# Import the VideoFileClip class from moviepy.editor module. The # type: ignore comment suppresses any type-related warnings.
from moviepy.editor import VideoFileClip  # type: ignore

# Load the video file "test.mp4" into a VideoFileClip object.
clip = VideoFileClip("test.mp4")

# Convert and save the VideoFileClip object as an animated GIF file named "test.gif".
clip.write_gif("test.gif") 
