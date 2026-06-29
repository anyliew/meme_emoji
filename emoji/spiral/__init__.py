import math
from datetime import datetime
from pil_utils import BuildImage
from meme_generator import add_meme
from meme_generator.utils import FrameAlignPolicy, Maker, make_gif_or_combined_gif
def spiral(images: list[BuildImage], texts, args):
    canvas_size = 600
    center = canvas_size / 2
    num_layers = 7
    pigs_per_layer = 12
    total_frames = 50
    def maker(i: int) -> Maker:
        def make(imgs: list[BuildImage]) -> BuildImage:
            base_img = imgs[0].convert("RGBA")
            canvas = BuildImage.new("RGBA", (canvas_size, canvas_size), "white")
            base_width = canvas_size * 0.22
            for layer in reversed(range(num_layers)):
                layer_scale_base = 0.70 ** layer
                current_radius = 210 * (layer_scale_base ** 1.4)
                if 1 <= layer <= 3:
                    size_factor = (1.0 - (layer * 0.14)) ** 3.2
                else:
                    size_factor = (1.0 - (layer * 0.14)) ** 2.6
                current_w = max(5, base_width * size_factor)
                current_h = int(current_w * base_img.height / base_img.width)
                pig = base_img.resize_canvas((int(base_img.width * 1.3), int(base_img.height * 1.3)))
                pig = pig.resize((int(current_w), current_h))
                direction = 1 if layer % 2 == 0 else -1
                frame_rotation = i * (360 / total_frames) * direction
                for p in range(pigs_per_layer):
                    angle_deg = p * (360 / pigs_per_layer) + frame_rotation
                    angle_rad = math.radians(angle_deg)
                    x = center + current_radius * math.cos(angle_rad) - pig.width / 2
                    y = center + current_radius * math.sin(angle_rad) - pig.height / 2
                    rotated_pig = pig.rotate(-angle_deg)
                    canvas.paste(rotated_pig, (int(x), int(y)), alpha=True)
            return canvas
        return make
    return make_gif_or_combined_gif(
        images, maker, total_frames, 0.07, FrameAlignPolicy.extend_loop
    )
add_meme(
    "spiral",
    spiral,
    min_images=1,
    max_images=1,
    keywords=["螺旋转", "漩涡"],
    date_created=datetime(2026, 5, 28),
    date_modified=datetime(2026, 5, 28),
)
