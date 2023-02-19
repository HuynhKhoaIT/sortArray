# nhập mảng từ người dùng
arr = input("Nhập mảng, cách nhau bằng dấu phẩy: ")
arr = arr.split(",")
arr = [int(x) for x in arr]

# sắp xếp mảng
arr.sort()

# in kết quả
print("Mảng sau khi sắp xếp: ", arr)
#Khoa