buying = input('do you want a muffin or cupcake?')
muffins = 10
cupcakes = 10

while buying != "0":
        if buying == "muffin" and muffins  > 0:
                muffins = muffins -1
                if buying == "muffin" and muffins == 0:
                        print("muffins out of stock")
        if buying == "cupcake" and cupcakes  > 0:
                cupcakes = cupcakes -1
        if buying == "cupcakes" and cupcakes == 0:
                print ("cupcakes out of stock")
        buying = input('do you want a muffin or cupcake?')

print("muffins;", muffins, "cupcakes:", cupcakes)
