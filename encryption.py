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

# シーザー復号化関数
def caesar_decrypt(text, shift):
    decrypted_text = ""
    num_elements = len(elements)

    for char in text:
        if char in alphabet:  # アルファベットまたは数字の場合
            index = alphabet.index(char)
            new_index = (index - shift) % len(alphabet)  # シフト量を適用（逆方向）
            decrypted_text += alphabet[new_index]
        elif char in elements:  # 元素記号の場合
            index = elements.index(char)
            new_index = (index - shift) % num_elements  # シフト量を適用（逆方向）
            decrypted_text += elements[new_index]
        else:
            decrypted_text += char  # その他の文字はそのまま

    return decrypted_text

# ユーザー入力
mode = input("暗号化する場合は 'encrypt'、復号化する場合は 'decrypt' を入力してください: ").strip().lower()
text = input("テキストを入力してください: ")
shift_amount = int(input("シフト量を入力してください（整数）: "))

if mode == 'encrypt':
    encrypted = caesar_encrypt(text, shift_amount)
    print("暗号化されたテキスト:", encrypted)
elif mode == 'decrypt':
    decrypted = caesar_decrypt(text, shift_amount)
    print("復元されたテキスト:", decrypted)
else:
    print("無効なモードが選択されました。'encrypt' または 'decrypt' を入力してください。")

