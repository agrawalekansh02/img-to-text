import pytesseract, sys
from PIL import Image

def main():
    print(pytesseract.image_to_string(Image.open(sys.argv[1])))


if __name__ == '__main__':
    main()
