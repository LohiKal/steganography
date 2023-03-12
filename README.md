# steganography

In this example, the encode_message function takes two arguments: the path to the original JPEG image and the message to be encoded. The function loads the image using the Pillow library, converts the message to binary, and modifies the least significant bits of the image's pixels to encode the message. The modified image is then saved as a new JPEG file.  To decode the hidden message from the encoded image, you can use a similar approach to extract the least significant bits of the pixels and convert them back to text.
