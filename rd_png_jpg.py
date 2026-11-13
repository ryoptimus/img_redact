from PIL import Image
from pathlib import Path


def redact_img(input_path, output_path, x1, y1, x2, y2):
    """
    permanently replace a rectangular region with black pixels

    args:
        input_path: path to original photo
        output_path: path to redacted
        x1, y1, x2, y2: rectangle coords
    """

    with Image.open(input_path) as img:
        # convert to rgb
        img = img.convert("RGB")

        width, height = img.size

        # normalize coordinates
        left, right = sorted((x1, x2))
        top, bottom = sorted((y1, y2))

        # ensure rectangle stays within image boundaries
        left = max(0, min(left, width))
        right = max(0, min(right, width))
        top = max(0, min(top, height))
        bottom = max(0, min(bottom, height))

        if left >= right or top >= bottom:
            raise ValueError("invalid rectangle coordinates.")

        # replace original pixels with pure black
        img.paste((0, 0, 0), (left, top, right, bottom))

        # save a newly encoded img (no original metadata)
        output_path = Path(output_path)
        img.save(output_path)

    print(f"redacted image saved to: {output_path}")

# example
redact_img(
    input_path="input.jpg",
    output_path="output.png",
    x1=100,
    y1=300,
    x2=200,
    y2=400
)
