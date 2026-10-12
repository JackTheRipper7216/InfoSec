from encodings.punycode import T


alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def encrypt(txt,k):
	res = ""
	for c in txt:
		if c == " ":
			res+=" "
			continue
		else:
			i = alp.index(c)
			res += alp[(i+k)%26]
	print(res)
#encrypt("CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ",4)



def decrypt(cipher, k):
	res = ""
	for c in cipher:
		if c == " ":
			res += " "
		else:
			i = alp.index(c)
			res += alp[(i-k)%26]
	print(res)

#decrypt("GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA")	

#ROOM1
corresp_alp = "QMJZTGFKPWLSBOXNCRYEVHIADU"
def encrypt(txt):
        res = ""
        for c in txt:
                if c == " ":
                        res+=" "
                        continue
                else:
                        i = alp.index(c)
                        res += corresp_alp[i]
        print(res) 



#encrypt("KEEP THE SECRET SAFE")


def decrypt(txt):
        res = ""
        for c in txt:
                if c == " ":
                        res+=" "
                        continue
                else:
                        i = corresp_alp.index(c)
                        res += alp[i]
        print(res)



#decrypt("ERVYE DXVR SXFPJ")



ciphertext = "EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,MVE PE FPHTY Q FXXZ YEQRE.SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,QOZ YKXRE IXRZY.IKTO DXV RTJXHTR EKT BTYYQFT,EKT HPFTOTRT LTD KQY GXVR STEETRY."

def counter(txt):

    freq = {letter: 0 for letter in alp}

    for letter in txt.upper():
        if letter in freq:
            freq[letter] += 1

    total = sum(freq.values())
    ranked = sorted(freq.items(), key=lambda item: item[1], reverse=True)

    print("Letter | Count | Percentage")
    for letter, count in ranked:
        if count > 0:
            percentage = count / total * 100
            print(f"{letter:6} | {count:5} | {percentage:.2f}%")

    return ranked

#counter(ciphertext)



def decrypt_partial(txt, mapping):
    result = ""

    for letter in txt.upper():
        if letter in alp:
            result += mapping.get(letter, "_")
        else:
            result += letter

    return result


ranked = counter(ciphertext)
english_order = "ETRSOAHNDIGL"

mapping = {}

for (cipher_letter, count), plain_letter in zip(ranked, english_order):
    if count > 0:
        mapping[cipher_letter] = plain_letter


#print(decrypt_partial(ciphertext, mapping))

#after correction 
 
mapping.update({
    "Y": "S",
    "X": "O",
    "J": "C",
    "B": "M",
    "N": "P",
    "G": "F",
    "C": "Q",
    "V": "U",
    "D": "Y",
    "H": "V",
    "I": "W",
    "L": "K",
    "M": "B",
})


#print(decrypt_partial(ciphertext, mapping))


#output : THE SECRET MESSAGE IS HIDDEN IN THIS PARAGRAPH.LETTER FREQUENCY DOES NOT REVEAL THE WHOLE KEY,BUT IT GIVES A GOOD START.LOOK FOR COMMON WORDS, REPEATED PATTERNS,AND SHORT WORDS.WHEN YOU RECOVER THE MESSAGE,THE VIGENERE KEY HAS FOUR LETTERS.




n_ciphertext = (
    "VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL"
    "GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC"
    "OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL"
    "GOFGGGVAQFGIEZLTUS"
)

# Each group uses the same key letter.
groups = [n_ciphertext[i::4] for i in range(4)]

key = ""

for i, group in enumerate(groups):
    print(f"\nGroup {i + 1}:")
    ranked = counter(group)
    most_frequent = ranked[0][0]

    # Assume the most frequent ciphertext letter represents E.
    shift = (alp.index(most_frequent) - alp.index("E")) % 26
    key += alp[shift]

print("\nKey:", key)


def decrypt_vigenere(txt, key):
    result = ""
    key_position = 0

    for letter in txt.upper():
        if letter in alp:
            shift = alp.index(key[key_position % len(key)])
            result += alp[(alp.index(letter) - shift) % 26]
            key_position += 1
        else:
            result += letter

    return result


print("\n")
print("Plaintext:")

print(decrypt_vigenere(n_ciphertext, key))

#CODE / ECLIPSE