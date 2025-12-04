from PIL import Image

# load my image source from the file to te image variable
image = Image.open("image_lion_king.jpg")

# function that takes an image object and x,y coordinates as imput and returns the value of the pixel
def get_pixel_image(image,pos_x,pos_y):
    return image.getpixel((pos_x,pos_y))

def decimal_to_binary(number):
    binary_number =""
    while number > 0:
        binary_number += str(number%2)
        number = number // 2
    if len(binary_number) < 8:
        binary_number += "0" *(8-len(binary_number))
    return binary_number[::-1]



def text_to_binary(message):

    # convert each character to its ordinal value
    message_ordinal = [ ord(character) for character in message]
    # convert each ordinal value to its binary representation
    message_bits = [decimal_to_binary(number) for number in message_ordinal]
    print(message_bits)
    return "".join(message_bits)

print(text_to_binary("Helloa1#()"))

