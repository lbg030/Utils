def xywh_to_xyxy(image_size, label):
    """
    Converts YOLO label format (xywh) to xyxy format.

    Args:
        image_size (tuple): Tuple containing (width, height) of the image.
        label (list): List containing [x, y, w, h] values.

    Returns:
        list: List containing [x_min, y_min, x_max, y_max] values.
    """
    width, height = image_size
    x, y, w, h = label
    x_min = (x - (w / 2)) * width
    y_min = (y - (h / 2)) * height
    x_max = (x + (w / 2)) * width
    y_max = (y + (h / 2)) * height

    return [x_min, y_min, x_max, y_max]