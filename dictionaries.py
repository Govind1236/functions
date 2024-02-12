dic = {
    "Govind": 355,
     355 : "Basnet",
     321 : "Pranamitol"
      
}
# print(dic[321])
# # to get the data in define key
# print(dic.get("Govind"))
# # to get all keys
# print(dic.keys())
# # to get value in keys
# print(dic.values())
# for info in dic.keys():
#     print(dic[info])
print(dic.items())
for info, value in dic.items():
    print(f"The value in {info} is {value}")