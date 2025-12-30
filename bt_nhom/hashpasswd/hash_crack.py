import argparse
import hashlib

parser = argparse.ArgumentParser(description="Hash Cracker (MD5 & SHA-1)")
parser.add_argument("-w", "--wordlist", help="Wordlist file", required=True)
parser.add_argument("-H", "--hash", help="Hash value to crack", required=True)
parser.add_argument("-t", "--type", help="Hash type: md5 or sha1", choices=["md5", "sha1"], required=True)
args = parser.parse_args()

def main():
    try:
        with open(args.wordlist, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip()
                if args.type == "md5":
                    hashed = hashlib.md5(word.encode("utf-8")).hexdigest()
                elif args.type == "sha1":
                    hashed = hashlib.sha1(word.encode("utf-8")).hexdigest()
                else:
                    print("Không tìm được loại mã hóa phù hợp")
                    return

                if hashed == args.hash:
                    print(f"Gía trị là : {word}")
                    return
        print("Thât bại không có mật khẩu trong words.txt")
    except FileNotFoundError:
        print("Không tìm được file words")

if __name__ == "__main__":
    main()