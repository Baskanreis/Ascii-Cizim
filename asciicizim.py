from PIL import Image

ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]

def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def grayscalify(image):
    return image.convert('L')

def modify(image, buckets=25):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def do(image, new_width=100):
    image = resize(image)
    image = grayscalify(image)

    pixels = modify(image)
    len_pixels = len(pixels)


    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

def runner(path):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
      
        return
    image = do(image)


    print(image)


    f = open('img.txt','w')
    f.write(image)
    f.close()


if __name__ == '__main__':
    import sys
    import urllib.request
    if sys.argv[1].startswith('http://') or sys.argv[1].startswith('https://'):
        urllib.request.urlretrieve(sys.argv[1], "asciify.jpg")
        path = "asciify.jpg"
    else:
        path = sys.argv[1]
    runner(path)