import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)

print(primrose.get_color())

print(sunflower.get_color()) #even though it is a flower, it can call the methods in the super clas (plant)
print(sunflower.get_petals())


#print(primrose.get_petals()) it cannot do this- method is only in the subclass
