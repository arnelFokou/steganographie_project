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
    for start_idx in range(0, len(binary_message)-1, 21):
        char_value = chr(int(binary_message[start_idx:start_idx+21],2))
        message.append(char_value)
    return "".join(message)

def even_pixel_image(matrice_image):
    return matrice_image - matrice_image % 2

def insert_message_in_pictue(image,message):
    even_matrix =  even_pixel_image(np.array(image))
    row_number, col_number, canal_number = even_matrix.shape
    message_crypted = message_to_binary(message)
    length_message = len(message_crypted)
    
    image_octets = even_matrix.flatten()
    liste_octets_crypted=[]

    for pos, value in enumerate(image_octets):
        if pos < length_message:
            liste_octets_crypted.append(value + int(message_crypted[pos]))
        else:
            break
                         
    if pos == length_message:
        liste_octets_crypted.extend(image_octets[pos:]) 
    print(len(liste_octets_crypted),len(image_octets))
    matrix_messaged = np.array(liste_octets_crypted).reshape(row_number,col_number,canal_number)

    Image.fromarray(matrix_messaged).save("image_watermarked.png")

def retrieve_message_from_picture(image):
    
    image_array = np.array(image)
 
    message_flat = (image_array - even_pixel_image(image_array)).flatten()
    message_binary="".join(str(char) for char in message_flat)
    message_final = binary_to_message(message_binary)
    print(message_final)


message = "Bravo, tu as réussi à extraire ce texte !"
image = Image.open("lion_king.png").convert('RGB')
insert_message_in_pictue(image,message)
image_watermarked = Image.open("image_watermarked.png")
retrieve_message_from_picture(image_watermarked)