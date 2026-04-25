from lexer import lexer
from parser import parsers

def main():
    print("==== HTML Construct Validator ====")
    print("1. Valid Comment")
    print("2. Matching Pairs")
    print("3. Table Structure")
    print("4. Self Closing Tags")
    print("5. Head and Body Tag")
    print("==================================")

    choice = input("Enter your choice (1-5): ")

    print("\nEnter your HTML content (Enter an empty line to finish input):")
    data_lines = []
    while True:
        try:
            line = input()
            if not line:
                break
            data_lines.append(line)
        except EOFError:
            break

    data = "\n".join(data_lines)

    if choice == '1':
        print("\n🔍 Checking Valid Comment...")
        parsers['comment'].parse(data, lexer=lexer)
    elif choice == '2':
        print("\n🔍 Checking Matching Pairs...")
        parsers['matching'].parse(data, lexer=lexer)
    elif choice == '3':
        print("\n🔍 Checking Table Structure...")
        parsers['table'].parse(data, lexer=lexer)
    elif choice == '4':
        print("\n🔍 Checking Self Closing Tag...")
        parsers['selfclose'].parse(data, lexer=lexer)
    elif choice == '5':
        print("\n🔍 Checking Head and Body Tag...")
        parsers['headbody'].parse(data, lexer=lexer)
    else:
        print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
