def decode(message, current, results):
    if len(message) == 0:
        results.append(current)
        return
    if message[0] != '0':
        num = int(message[0])
        letter = chr(64 + num)
        decode(message[1:], current + letter, results)
    if len(message) >= 2:
        num = int(message[:2])
        if 10 <= num <= 26:
            letter = chr(64 + num)
            decode(message[2:], current + letter, results)

def main():
    while True:
        print("Menu:")
        print("1. Decode a message")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            encoded = input("Enter the encoded message (digits only): ")
            if not encoded.isdigit():
                print("Error: Encoded message must contain digits only.")
                continue
            results = []
            decode(encoded, "", results)
            if results:
                print("Possible decodings:")
                for r in results:
                    print(r)
            else:
                print("No valid decodings found.")
        elif choice == "2":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
