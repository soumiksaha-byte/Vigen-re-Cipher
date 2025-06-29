import streamlit as st

# Vigenère Cipher Functions
def vigenere_encrypt(plain_text, keyword):
    result = ""
    keyword = keyword.lower()
    k_len = len(keyword)
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = ord(keyword[i % k_len]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_decrypt(cipher_text, keyword):
    result = ""
    keyword = keyword.lower()
    k_len = len(keyword)
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            shift = ord(keyword[i % k_len]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result

# Streamlit UI
st.set_page_config(page_title="CipherShield", layout="centered")

st.title("🔐CipherShield: Secure Text with Vigenère Cipher & Streamlit")

text = st.text_area("Enter your text:", height=150)
keyword = st.text_input("Enter keyword:")

action = st.radio("Choose an action:", ["Encrypt", "Decrypt"])

if st.button("Submit"):
    if not text or not keyword:
        st.warning("Please enter both text and keyword.")
    else:
        if action == "Encrypt":
            result = vigenere_encrypt(text, keyword)
            st.success("✅ Encrypted Text:")
        else:
            result = vigenere_decrypt(text, keyword)
            st.success("🔓 Decrypted Text:")
        st.code(result, language="text")
