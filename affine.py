class Affine:
    def __init__(self, keya, keyb):
        if self.gcd(keya, 26) != 1:
            print("Key may not satisfy the condition")
        else:
            self.a = keya
            self.b = keyb
            self.alph = [chr(ord('a') + i) for i in range(26)]

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def inverse_modulo(self, a):
        a = a % 26
        for i in range(1, 26):
            if (a * i) % 26 == 1:
                return i
        return -1

    def encrypt(self, pt):
        ct = ""
        for char in pt:
            k = self.alph.index(char)
            ct += self.alph[(self.a * k + self.b) % 26]

        return ct.upper()

    def decrypt(self, ct):
        pt = ""
        for char in ct.lower():
            k = self.alph.index(char)
            x = self.inverse_modulo(self.a)
            pt += self.alph[(x * (k - self.b) + 26 * 10) % 26]

        return pt

    def attack(self, ct):
        ct = ct.lower()
        a_values = [i for i in range(1, 26) if self.gcd(i, 26) == 1]
        count = 0

        for a in a_values:
            for b in range(1, 27):
                count += 1
                pt = ""
                inv = self.inverse_modulo(a)

                for char in ct:
                    k = self.alph.index(char)
                    pt += self.alph[(inv * (k - b + 2600) % 26)]

                print(f"a: {a}, b: {b}, pt: {pt}")

        print("Total Possibilities:", count)


if __name__ == "__main__":
    affine = Affine(7, 11)
    print(affine.encrypt("sastra"))
    print(affine.decrypt("HLHOAL"))
    affine.attack(affine.encrypt("sastra"))

