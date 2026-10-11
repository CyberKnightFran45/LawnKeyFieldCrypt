MASK32 = 0xFFFFFFFF

SHIFT_LEFT = 13
SHIFT_RIGHT = 19


def rotate_bits(v, left, right):
    v &= MASK32
    return ((v >> right) | (v << left)) & MASK32


def to_int32(v):
    v &= MASK32

    if v >= 0x80000000:
        return v - 0x100000000

    return v


def encrypt(v):
    u = v & MASK32
    x = u ^ SHIFT_LEFT

    return to_int32(
        rotate_bits(x, SHIFT_LEFT, SHIFT_RIGHT)
    )


def decrypt(v):
    u = v & MASK32
    x = rotate_bits(u, SHIFT_RIGHT, SHIFT_LEFT)

    return to_int32(x ^ SHIFT_LEFT)


def main():
    
    while True:
        
        print("\n==============================================")
        print("       PvZ2C LawnKeyField Cryptor")
        print("==============================================\n")
        
        print("0. Exit")
        print("1. Encrypt Int")
        print("2. Decrypt Int")
        
        print("==============================================\n")

        option = input("Select option: ").strip()
        
        print("\n")

        if option == "0":
            print("Closing...")
            break

        if option not in ("1", "2"):
            print("Invalid option.")
            continue

        try:
            val = int(input("Enter value: ").strip())

            if option == "1":
                result = encrypt(val)
                print(f"\nEncrypted: {result}")

            elif option == "2":
                result = decrypt(val)
                print(f"\nDecrypted: {result}")

        except ValueError:
            print("Value must be an integer.")

        input("\nPress ENTER to continue...")


if __name__ == "__main__":
    main()
