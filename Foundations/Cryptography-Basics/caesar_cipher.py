# cipher using dictionary comprehension

print("Cipher using dictionary comprehension:")

cipher = {chr(x):chr(x+1) for x in range(97, 123)}
cipher['z'] = 'a' 
eparts = [cipher[letter] for letter in "secretmessage"]

print("enciphered message:", "".join(eparts))

decipher = {value:key for key, value in cipher.items()}
dparts = [decipher[letter] for letter in "tfdsfunfttbhf"]

print("decyphered message:", "".join(dparts))

# cipher using string library with maketrans() and translate()

print("Cipher using string library with maketrans() and translate() functions:")

caesar = str.maketrans("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza")
decrypt_caesar = str.maketrans("bcdefghijklmnopqrstuvwxyza", "abcdefghijklmnopqrstuvwxyz")

print("enciphered message:",str.translate("secretmessage", caesar))
print("decyphered message:", str.translate("tfdsfunfttbhf", decrypt_caesar))

# cipher using codecs library 
import codecs

print("Cipher using codecs library:")
print("enciphered message:",codecs.encode("secretmessage", "rot_13"))
print("deciphered message:", codecs.encode("frpergzrffntr", "rot_13"))

print("Results are the same for each method!")