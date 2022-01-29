import secrets
import string

def gen_pass(length):
    chr = string.ascii_letters + string.digits
    sec_pass = ''.join(secrets.choice(chr) for i in range(length))
    return sec_pass

def main():
    pass_len = int(input("Number of password digits:"))
    print("Generated Password: ", gen_pass(pass_len))
    return 0
main()
