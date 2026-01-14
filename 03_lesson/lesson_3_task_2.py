from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S21", "+79261234567"),
    Smartphone("Xiaomi", "Mi 11", "+79361234567"),
    Smartphone("Google", "Pixel 6", "+79461234567"),
    Smartphone("Huawei", "P40", "+79561234567")
]

for phone in catalog:
    print(f"{phone.marka}, {phone.model}, {phone.number}")
