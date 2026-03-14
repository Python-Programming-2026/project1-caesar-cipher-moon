from colorama import Fore,init
init(autoreset=True)     # 加入colorma库，增加彩色输出+过程动画  
# 凯撒密码函数
def caesar_cipher(text,shift,mode='encrypt'):
    result=""
    if mode=='decrypt':
        shift=-shift # 如果是解密，则偏移量反过来
    for char in text:
        if char.isalpha():
            ascii_base=ord('A') if char.isupper() else ord('a')
            new_char=chr((ord(char)-ascii_base+shift)%26+ascii_base)
            result+=new_char
        else:
            result+=char
    return result
# 逐字符显示（动画效果）
def show_step(text,shift):
    print(Fore.CYAN+"===移位过程===")
    for char in text:
        if char.isalpha():
            new_char=caesar_cipher(char,shift)
            print(f"{char}->{new_char}",end=" ")
    print("\n")
# 暴力破解
def brute_force(cipher):
    print(Fore.MAGENTA+"===暴力破解所有可能===")
    for k in range(26):
        print(f"偏移{k}:{caesar_cipher(cipher,k,mode='decrypt')}")
if __name__=='__main__':
    while True:
        print("=====凯撒密码工具=====")
        print("1.加密")
        print("2.解密")
        print("3.暴力破解")
        print("4.退出")
        choice=input("请选择：")
        if choice=="1":
            text=input("请输入明文：")
            shift=input("请输入密钥：")
            shift=int(shift)
            show_step(text,shift)
            print(Fore.GREEN+"密文："+caesar_cipher(text,shift,mode='encrypt'))
        elif choice=="2":
            text=input("请输入密文：")
            shift=input("请输入密钥：")
            shift=int(shift)
            print(Fore.GREEN+"密文"+caesar_cipher(text,shift,mode='decrypt'))
        elif choice=="3":
            text=input("请输入密文：")
            brute_force(text)
        elif choice=="4":
            break
        else:
            print("请输入有效选项")
            break
