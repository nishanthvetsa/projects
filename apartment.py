class appartment():
    def __init__(self):
        self.firstfloor=tuple(f"f{i}" for i in range(1,11))
        self.secondfloor=tuple(f"s{i}" for i in range(1,11))
        self.thirdfloor=tuple(f"t{i}" for i in range(1,11))
        self.groundfloor=tuple(f"s{i}" for i in range(1,31))

        self.first_owner=[]
        self.second_owner=[]
        self.third_owner=[]

        self.House_owners=[]
        self.House_numbers=[]
        self.Parking_Number=[]
        self.propert={}


    def house_owner_names(self):
        for i in range(1,31):
            owner_name=f"name{i}"
            if i<=10:
                self.first_owner.append(owner_name)
            elif 10 < i <=20:
                self.second_owner.append(owner_name)
            elif 20 < i <= 30:
                self.third_owner.append(owner_name)
            else:
                print("chusuko bro error vachindi!!\n")

    def property(self):
        house_numbers=list(self.firstfloor+self.secondfloor+self.thirdfloor)
        owners=self.first_owner+self.second_owner+self.third_owner
        self.House_numbers=house_numbers
        self.House_owners=owners
        self.propert=dict(zip(house_numbers,owners))

    def parking(self):
        self.Parking_Number=list(range(1,31))
        parking_slot={}
        for i in range(30):
            parking_slot[self.House_numbers[i]]=self.Parking_Number[i]
        return parking_slot

    def edit_owner(self,house_numbers,new_house_owners):
        if house_numbers in self.propert:
            self.propert[house_numbers]= new_house_owners
            print(f"the house owner details {house_numbers} updated succesfully")
        else :
            print("vacancy ledu bro!!")

    def search(self,house_numbers):
        if house_numbers in self.propert:
            owner_name=self.propert[house_numbers]
            parking=self.parking()[house_numbers]
            print(f"owner name is{owner_name}, and his parking alloted is{parking} ")

        else:
            print("evarru sir meru!!")

appartments=appartment()
appartments.house_owner_names()
appartments.property()


print("house numbers=",appartments.House_numbers)
print("house owners=",appartments.House_owners)
print("property is=",appartments.propert)
print("parking =",appartments.parking())

appartments.edit_owner("f11","new_house_owner")
print("updated appartment details",appartments.propert)

appartments.search("f1")