import utils
from PassGenerator import PasswordGenerator

def main():
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    include_numbers = input("Include numbers? (y/n): ").lower() == "y"
    include_special_characters = input("Include special characters? (y/n): ").lower() == "y"

    password_gen = PasswordGenerator(length, include_uppercase, include_lowercase, include_numbers, include_special_characters)

    while True:
        generated_password = password_gen.generate_password()
        print('Generated Password:', generated_password)
        # is_secure = utils.is_password_secure(generated_password)
        is_secure = password_gen.is_password_secure(generated_password)
        if is_secure:
            print("Password is secure.")
            response = input("Are you satisfied with this password? (yes/no): ")
            if response.lower() == "yes":
                break
        else:
            print("Password is not secure. Generating a new password...")

    print("Final password:", generated_password)

if __name__ == "__main__":
    main()