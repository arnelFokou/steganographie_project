from PIL import Image

# load my image source from the file to te image variable
image = Image.open("image_lion_king.jpg")

# function that takes an image object and x,y coordinates as imput and returns the value of the pixel
def get_pixel_image(image,pos_x,pos_y):
    return image.getpixel((pos_x,pos_y))


print(get_pixel_image(image,100,130))

