import codecs

encoded_string = input("Input your string to decode by ROT13: ")
decoded_string = codecs.decode(encoded_string, 'rot_13')
print(decoded_string)
