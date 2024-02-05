from PIL import Image
import os
from moviepy.editor import ImageSequenceClip


def resize_images_to_uniform_size(input_dir, output_dir, target_size=(1920, 1080)):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.png'):
            img_path = os.path.join(input_dir, filename)
            img = Image.open(img_path)
            img_resized = img.resize(target_size, Image.LANCZOS)  # Use LANCZOS for high-quality downsampling
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)


def create_video_from_images(images_dir, output_video_path, fps=5):
    image_files = sorted(
        [os.path.join(images_dir, filename) for filename in os.listdir(images_dir) if filename.endswith('.png')])
    clip = ImageSequenceClip(image_files, fps=fps)
    clip.write_videofile(output_video_path)


# Set directories and target size
input_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps_merged'
output_dir = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/maps_for_video'
output_video_path = '/Users/pintoza/Desktop/dev/data-science/taxi-demand-forecast/reports/taxi_zone_changes_over_time.mp4'

# Resize images
resize_images_to_uniform_size(input_dir, output_dir, target_size=(1920, 1080))

# Create video
create_video_from_images(output_dir, output_video_path, fps=1)
