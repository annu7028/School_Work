def ChargePod(k, pod):
    #set variable = to distance traveled
    dis = 0
    charge = list()
    #traverse through list
    for i in range(len(pod)):
        #if point in list minus dis is greater than k
        if(pod[i] - dis > k):
            #then previous element in list is location of charge
            charge.append(pod[i-1])
            #and set the distance equal to that element
            dis = pod[i-1]
    return charge