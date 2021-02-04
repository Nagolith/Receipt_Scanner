import pytesseract
from pytesseract import Output
import cv2
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/HEAD-49865ad/bin/tesseract'

img = cv2.imread('/Users/jonathanhald/Documents/SAI/receipt_scanner/Receipt_Scanner/receipt.png')
# img = cv2.imread('/Users/jonathanhald/Documents/SAI/receipt_scanner/receipt_2.jpg')
window_name = 'img'
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# cv2.imshow(window_name, img)

# #waits for user to press any key  
# #(this is necessary to avoid Python kernel form crashing) 
# cv2.waitKey(0)  
  
# #closing all open windows  
# cv2.destroyAllWindows()  

extracted_text = pytesseract.image_to_string(img, lang = 'deu')

# receipt_ocr = {}

# splits = extracted_text.splitlines()
# restaurant_name = splits[0] + '' + splits[1]

print(extracted_text)

# import re
# # regex for date. The pattern in the receipt is in 30.07.2007 in DD:MM:YYYY

# date_pattern = r'(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d'
# date = re.search(date_pattern, extracted_text).group()
# receipt_ocr['date'] = date
# print(date)

# # get lines with chf
# lines_with_chf = []
# for line in splits:
#     if re.search(r'CHF', line):
#         lines_with_chf.append(line)
#     # added in to include total
#     elif re.search(r'CHE', line):
#         lines_with_chf.append(line)


# print(lines_with_chf)