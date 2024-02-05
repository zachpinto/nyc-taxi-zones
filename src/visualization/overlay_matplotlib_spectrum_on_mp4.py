from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip


def overlay_color_spectrum_on_video(video_path, overlay_image_path, output_video_path):
    # Load the main video clip
    video_clip = VideoFileClip(video_path)

    # Load the overlay image as a clip
    overlay_clip = ImageClip(overlay_image_path).set_duration(video_clip.duration).set_pos(("left", "center"))

    # Overlay the image clip onto the video clip
    final_clip = CompositeVideoClip([video_clip, overlay_clip])

    # Write the result to a new file
    final_clip.write_videofile(output_video_path, codec='libx264', audio_codec='aac')


# Paths
video_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/final_video.mp4'
overlay_image_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/color_spectrum_transparent.png'
output_video_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/final_video_with_spectrum.mp4'

overlay_color_spectrum_on_video(video_path, overlay_image_path, output_video_path)






