with open("input.txt", "r") as f1:
    s = f1.read()

keys = s.split("\n\n")
print(keys)
# newkeys = keys[2:]
output_list = []

i = 0

# while i < len(keys):
#     start_strings = ["Prac.", "Lec.", "Tut.", "emptySlot"]
#     if keys[i] == "emptySlot":
#         print("encountered empty slot")
#         i += 1
    # else:
    #     if keys[i+4].isdigit():
    #         print("no lecturer name")
    #         i += 5
    #     else:
    #         print("lecturer name")
    #         i +=6
