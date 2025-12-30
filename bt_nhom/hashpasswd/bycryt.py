import bcrypt

#  Nhập mật khẩu cần mã hóa

plain_password = input("Nhập mật khẩu muốn mã hóa: ")
#  Tạo salt ngẫu nhiên và mã hóa mật khẩu
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(plain_password.encode("utf-8"), salt)

#  In kết quả
print("----------------------------")
print(f"Mật khẩu gốc: {plain_password}")
print(f"Salt: {salt.decode()}")
print(f"Mật khẩu đã mã hóa (bcrypt): {hashed_password.decode()}")