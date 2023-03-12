from PIL import Image

def encode_message(image_path, message):
    img = Image.open(image_path)
    pixels = img.load()

    # Check if the message is too long to fit into the image
    if len(message) > img.size[0] * img.size[1]:
        raise ValueError("Message is too long to fit into image")

    # Convert the message to binary
    message_bin = ''.join(format(ord(c), '08b') for c in message)

    # Modify the least significant bits of the pixels to encode the message
    index = 0
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if index < len(message_bin):
                pixel = list(pixels[i, j])
                pixel[0] = (pixel[0] & 254) | int(message_bin[index])
                pixels[i, j] = tuple(pixel)
                index += 1
            else:
                break

    # Save the modified image
    img.save('encoded_image.jpg')

# Example usage
encode_message('original_image.jpg', 'This is a hidden message')
