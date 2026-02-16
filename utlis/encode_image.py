import base64
def encode_image_to_base64(img_bytes):
    return base64.b64encode(img_bytes).decode()