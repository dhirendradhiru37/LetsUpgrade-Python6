import math

class cone:
    def __init__(self,r=1,h=1):
        self.r=r
        self.h=h
        self.volume=0
        self.surface_area=0
        
    def volume_func(self):
        self.volume=math.pi*self.r*self.r*(self.h/3)
        return self.volume
    def surface_Area_Func(self):
        base=math.pi*self.r*self.r
        side=math.pi*self.r*math.sqrt(self.r**2+self.h**2)
        self.surface_area=base+side
        return self.surface_area
        
cone1=cone(5,8)
print("Volume of cone= ",cone1.volume_func())
print("Surface Area of cone= ",cone1.surface_Area_Func())