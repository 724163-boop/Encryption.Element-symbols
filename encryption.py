# Encryption.Element-symbols
Encryption.Element symbols
# 元素記号のリスト
elements = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ag", "Au"
]

# アルファベットと数字のリスト
alphabet = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

# シーザー暗号化関数
def caesar_encrypt(text, shift):
    encrypted_text = ""
    num_elements = len(elements)

    for char in text:
        if char in alphabet:  # アルファベットまたは数字の場合
            index = alphabet.index(char)
            new_index = (index + shift) % len(alphabet)  # シフト量を適用
            encrypted_text += alphabet[new_index]
        elif char in elements:  # 元素記号の場合
            index = elements.index(char)
            new_index = (index + shift) % num_elements  # シフト量を適用
            encrypted_text += elements[new_index]
        else:
            encrypted_text += char  # その他の文字はそのまま

    return encrypted_text

# 使用例
original_text = "I am y-redhat"
shift_amount = 3
encrypted = caesar_encrypt(original_text, shift_amount)

print("元のテキスト:", original_text)
print("暗号化されたテキスト:", encrypted)
