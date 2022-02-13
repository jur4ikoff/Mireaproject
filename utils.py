# Login: -1 if incorrect signature. -2 if len(users) == 0. or user that has the most similar signature

# Imports
import numpy as np
import cv2
import imutils
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sqlite3
import io
from skimage.metrics import structural_similarity as ssim
from imutils.convenience import resize
from config import *

class User():
    def __init__(self, name, surname, email, sign) -> None:
        self.name=name
        self.surname=surname
        self.email=email
        self.sign=sign

# Utils
def resize(orig):
    # resulting resolution is 500x330px

    height, width, channels = orig.shape

    ratio = WIDTH / width
    new_height = height * ratio

    new_img = resize(orig, WIDTH, new_height)
    return new_img

def findBorder(array):
    left, top, right, bottom = 500,500,0,0

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]!=0:
                if j < left:
                    left = j

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]!=0:
                if i < top:
                    top = i

    for i in range(len(array), 0):
        for j in range(len(array[0])):
            if array[i][j]!=0:
                if j > right:
                    right = j

    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]!=0:
                if i > bottom:
                    bottom = i

    return left-1, top-1, len(array[0]) - right+1, bottom+1

def process_image(new_img):
    # print(type(new_img))
    img = np.array(new_img, dtype="uint8")

    original = img.copy()

    # Converting to grayscale image

    # gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
    # grayWithBlur = cv2.GaussianBlur(original,(5,5),0)

    final = cv2.Canny(original,80,200)

    final_arr = np.array(final)
    # left, top, right, bottom = findBorder(final_arr)

    # return final[top:bottom, left:right]
    return final

def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out)

# Register ndarray type for sqlite

def register_types():
    # Converts np.array to TEXT when inserting
    sqlite3.register_adapter(np.ndarray, adapt_array)

    # Converts TEXT to np.array when selecting
    sqlite3.register_converter("array", convert_array)
    
def try_login(input_signature):
    register_types()
    
    input_image = process_image(input_signature)

    conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    conn.commit()

    res = cursor.execute("SELECT * FROM DATA").fetchall()

    cursor.close()
    conn.close()

    users=[]
    for i in range(len(res)):
        users.append(User(res[i][1], res[i][2], res[i][3], res[i][4]))

    best_user=None
    max=0

    if len(users) == 0:
        return -2

    for i in users:
        # plt.imshow(i.sign, cmap='gray')
        
        current = ssim(input_image, i.sign)
        if current > max:
            best_user=i
            max=current

    if max < MIN_SIMILARITY:
        print('INCORRECT SIGNATURE!')
        return -1

    # print(best_user.name)
    return best_user

def register(name, surname, email, input_signature):
    register_types()
    
    processed_sign = process_image(input_signature)
    
    conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO DATA(name, surname, mail, sign) VALUES(?,?,?,?)", (name, surname, email, processed_sign))
    conn.commit()

    cursor.close()
    conn.close()