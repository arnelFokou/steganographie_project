from PIL import Image
import numpy as np 

# load my image source from the file to te image variable
# image = Image.open("image_lion_king.jpg")
# size = image.size

# # function that takes an image object and x,y coordinates as imput and returns the value of the pixel
# def get_pixel_image(image,pos_x,pos_y):
#     return image.getpixel((pos_x,pos_y))

# # take a number and convert it to octet 
# def decimal_to_binary(number):
    
#     binary_number =""
#     while number > 0:
#         binary_number += str(number%2)
#         number = number // 2
#     if len(binary_number) < 8:
#         binary_number += "0" *(8-len(binary_number))
#     return binary_number[::-1]

# def text_to_binary(message):
#     # convert each character to its ordinal value
#     message_ordinal = [ ord(character) for character in message]
#     print(message_ordinal)
#     # convert each ordinal value to its binary representation
#     message_bits = [decimal_to_binary(number) for number in message_ordinal]
#     return "".join(message_bits)



# def composant_to_pixel_value(composant):
#     """
#     Docstring for composant_to_pixel_value
    
#     :param composant: tuple of integers representing the color components of a pixel (R, G, B)
#     :return: integer value representing the pixel
#     """
#     pixel_value = 0
#     significant_composant = 65_536
#     for element in composant:
#         pixel_value = pixel_value +( element * significant_composant )
#         significant_composant /= 256
    
#     return int(pixel_value)


# def pixel_to_composant(pixel_value):
#     """
#     Docstring for pixel_to_composant
    
#     :param pixel_value: integer value representing the pixel
#     :return : tuple of integers representing the color components of a pixel (R, G, B)
#     """
#     list_composant = []
#     significant_composant = 65_536
#     for _ in range(3):
#         resultat = pixel_value // significant_composant
#         pixel_value = pixel_value % significant_composant
#         list_composant.append(int(resultat))
#         significant_composant /=256
#     return tuple(list_composant)

# def pair_pixel(image):
#     liste_pixel_pairs = []
#     for pixel in list(image.getdata()):
#         value_pixel = composant_to_pixel_value(pixel)
#         liste_pixel_pairs.append(int(value_pixel) if value_pixel % 2 == 0 else int(value_pixel -1))
    
#     return liste_pixel_pairs

# def encode_message_in_image(image,message):
#     value_pixels = pair_pixel(image)
#     message_bits = text_to_binary(message)
#     final_pixels = []
#     final_components = []
#     for bit_pos,bit_value in enumerate(message_bits):
#         final_pixels.append(value_pixels[bit_pos] + int(bit_value))

#     for pixel in final_pixels + value_pixels[bit_pos+1:]:
#         final_components.append( pixel_to_composant(pixel))

#     return final_components

    
#pixels = get_pixel_image(image)
# pixels_pairs = pair_pixel(image)

#print(composant_to_pixel_value((list(image.getdata()))[9]))
# print(list(image.getdata())[9])
# print(list(image.getdata())[:10])
#print(pixel_to_composant(116714))

# print(image.size)
# print(len(encode_message_in_image(image,"Hello")))



def message_to_binary(message):
    
    """
    Docstring for message_to_binary
    
    :param message: string message to convert to binary representation
        the program will take one by one each character of the message and convert it to its binary representation
        we take 21 bits to represent each character beacuse we use utf-8 encoding which can use up to 21 bits per character
    :return: string binary representation of the message    
    """
    liste_of_bits = [bin(ord(char))[2:].zfill(21) for char in message] 
    return "".join(liste_of_bits)

def binary_to_message(binary_message):

    message=[]
    for bit_elt in range(0, len(binary_message)-1, 21):
        char_value = chr(int(binary_message[bit_elt:bit_elt+21],2))
        message.append(char_value)
    return "".join(message)

def even_pixel_image(matrice_image):
    return matrice_image - matrice_image % 2

def insert_image_in_pictue(image,message):
    image =  even_pixel_image(np.array(image))
    print(image.shape)
    row_number, col_number, canal_number = image.shape
    message_crypted = message_to_binary(message)

    idx_message=0
    for row in range(0,row_number):
        for col in range(0,col_number):
            for canal in range(0,canal_number):
                if idx_message == len(message_crypted):
                    break
                else:
                    image[row,col,canal] += int(message_crypted[idx_message])
                    idx_message +=1

    Image.fromarray(image).save("image_watermarked.png")
                

   




message = "Hello,Maman est fatiguée : pourquoi les parents râlent - stress, épuisement et moyens de retrouver la sérénité dans le quotidien familial"
# message_binary = message_to_binary(message)
# print(binary_to_message(message_binary))

image = Image.open("lion_king.png").convert('RGB')

insert_image_in_pictue(image,message)