import hashlib
import itertools
import string

# Chuỗi hash MD5 cần giải mã
target_hash = "0e64a7b00c83e3d22ce6b3acf2c582b6"  # hash của "password"

# Tập ký tự cần thử (chữ thường + số)
charset = string.ascii_lowercase + string.digits

# Giới hạn độ dài chuỗi cần thử
max_length = 6

def brute_force_md5(hash_value, charset, max_len):
    for length in range(1, max_len + 1):
        print(f"🔍 Đang thử độ dài: {length}")
        for candidate in itertools.product(charset, repeat=length):
            word = ''.join(candidate)
            hashed = hashlib.md5(word.encode("utf-8")).hexdigest()
            if hashed == hash_value:
                print(f" Hash cracked! Giá trị gốc là: {word}")
                return
    print(" Không tìm được giá trị phù hợp trong phạm vi brute-force.")

#  Gọi hàm
brute_force_md5(target_hash, charset, max_length)