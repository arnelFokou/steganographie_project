from PIL import Image
import numpy as np 



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
    print(len(message))
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

def retrieve_message_from_picture(image):
    
    image_array = np.array(image)
 
    message_flat = (image_array - even_pixel_image(image_array)).flatten()
    message_binary="".join(str(char) for char in message_flat)
    message_final = binary_to_message(message_binary)
    print(message_final)







message = "Hello,Maman est fatiguée : pourquoi les parents râlent - stress, épuisement et moyens de retrouver la sérénité dans le quotidien familial"
# message_binary = message_to_binary(message)
# print(binary_to_message(message_binary))

image = Image.open("lion_king.png").convert('RGB')
insert_image_in_pictue(image,message)
image_watermarked = Image.open("image_watermarked.png")
retrieve_message_from_picture(image_watermarked)