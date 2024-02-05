from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

# Set the IMAGEMAGICK_BINARY environment variable
os.environ['IMAGEMAGICK_BINARY'] = '/opt/homebrew/bin/magick'

def create_year_week_overlay(year, week, video_size):
    """Generates an overlay image with year and week text."""
    text = f"{year}\nWeek {week}"
    text_clip = TextClip(text, fontsize=120, color='black', bg_color='#ffaf08')
    # Adjust position by specifying pixel values
    # Assuming video_size is a tuple (width, height), calculate position for center of top left quadrant
    position_x = video_size[0] * 0.15  # Move 25% to the right from the left edge
    position_y = video_size[1] * 0.15  # Move 10% down from the top edge
    return text_clip.set_position((position_x, position_y)).set_opacity(0.5)

def add_year_week_to_video(input_video_path, output_video_path, fps=1):
    video_clip = VideoFileClip(input_video_path)
    video_size = video_clip.size  # Get video size for calculating text overlay position
    clips = [video_clip]

    frame_duration = 1 / fps
    total_frames = int(video_clip.duration * fps)
    year, week = 2018, 0
    for frame in range(total_frames):
        week += 1
        if week > 52 or (year == 2020 and week > 53):
            year += 1
            week = 1

        overlay_clip = create_year_week_overlay(year, week, video_size).set_start(frame * frame_duration).set_duration(frame_duration)
        clips.append(overlay_clip)

    final_clip = CompositeVideoClip(clips, size=video_clip.size)
    final_clip.write_videofile(output_video_path, codec="libx264")

input_video_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/final_video_with_spectrum.mp4'
output_video_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/final_video_with_spectrum_and_yearweek_overlays.mp4'

add_year_week_to_video(input_video_path, output_video_path, fps=4)
