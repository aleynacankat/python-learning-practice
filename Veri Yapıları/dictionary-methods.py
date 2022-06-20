opel0bj = {
    "marka": "Opel",
    "model": "Corsa",
    "yil": 2020
}

sonuc = opel0bj["marka"]
sonuc = opel0bj.get("marka")

# for x in opel0bj:
#     print(x)

# for x in opel0bj:
#     print(opel0bj[x])

# for x in opel0bj.values():
#     print(x)

# for x,y in opel0bj.items():
#     print(x,y)

# sonuc = "marka" in opel0bj
# print(sonuc)

# sonuc = len(opel0bj)

# opel0bj["renk"] = "kırmızı"
# opel0bj.pop("renk")
# opel0bj.popitem()
# opel0bj.popitem()
# print(opel0bj)

# del opel0bj["marka"]
# print(opel0bj)

# obj =  opel0bj.copy()
# obj["marka"] = "Mazda"

# print(obj)
# print(opel0bj)

opel0bj.update({
    "marka": "Bmw",
    "renk": "Kırmızı"
})

print(opel0bj)
