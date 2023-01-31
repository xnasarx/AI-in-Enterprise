Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
input_list = [2, 7, 6, 3, 19, 8, 14, 26]
print("List : " + str(input_list))
List : [2, 7, 6, 3, 19, 8, 14, 26]
percent = (len(list(filter(lambda ele: ele % 2 == 0, input_list))) / len(input_list)) * 100
print("Percentage of number of even elements in the list : " + str(percent))
Percentage of number of even elements in the list : 62.5
