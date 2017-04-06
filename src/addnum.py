with open("110000.dat","r") as fi:
    with open("110000num.dat","w") as fo:
        i=1
        for l in fi.readlines():
            if i%100 == 0:
                fo.write(l.strip()+" #"+str(i)+"\n")
            else:
                fo.write(l)
            i = i+1
