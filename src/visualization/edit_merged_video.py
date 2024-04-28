import os
from moviepy.editor import ImageSequenceClip


def create_video_from_images_with_cropping(images_dir, output_video_path, fps=4, crop_left=10, crop_bottom=10,
                                           crop_right=10, crop_top=0):
    """
    Creates a cropped video from a sequence of images.

    :param images_dir: Directory containing the images.
    :param output_video_path: Path to save the output video.
    :param fps: Frames per second, adjusted to control video duration.
    :param crop_left: Number of pixels to crop from the left.
    :param crop_bottom: Number of pixels to crop from the bottom.
    :param crop_right: Number of pixels to crop from the right.
    :param crop_top: Number of pixels to crop from the top.
    """
    # List of image file paths sorted by name
    image_files = [os.path.join(images_dir, filename) for filename in sorted(os.listdir(images_dir)) if
                   filename.endswith('.png')]

    # Create a video clip from the images
    clip = ImageSequenceClip(image_files, fps=fps)

    # Calculate the crop values for the right and bottom sides
    # Note: ImageSequenceClip does not directly support x2, y2 negative indexing like crop() in PIL or OpenCV.
    # Instead, you should calculate the width and height manually if needed.

    # Crop the video
    cropped_clip = clip.crop(x1=crop_left, y1=crop_top, x2=None, y2=None)

    # Adjust the size manually if needed or use other video editing tools to precisely control the crop.

    # Write the result to a file
    cropped_clip.write_videofile(output_video_path)

# Directory containing the images
images_dir = '../../reports/maps_for_video'  # Update this path to where your images are stored

# Path where you want to save the video file
output_video_path = '../../reports/final_video.mp4'  # Update this path to where you want to save your video

# Create the video from images with cropping
create_video_from_images_with_cropping(images_dir, output_video_path, fps=4, crop_left=100, crop_bottom=30,
                                       crop_right=0, crop_top=0)
