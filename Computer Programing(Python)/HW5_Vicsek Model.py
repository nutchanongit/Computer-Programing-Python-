
#-------------------------------------------
# HW5: Vicsek Model
# ID: 6430110921  ณัฐชนน คงแก้ว

def gen_data(N, W, H):
    x = [0.0]*N
    y = [0.0]*N
    dx = [0.0]*N
    dy = [0.0]*N


    for i in range(N):
        import random
        x[i] = random.uniform(0,W)
        y[i] = random.uniform(0,H)

        import math
        degree = random.uniform(0,360)
        rad = math.radians(degree)

        dx[i] = math.cos(rad)
        dy[i] = math.sin(rad)

    return(x,y,dx,dy)

#-------------------------------------------
def move_all(x, y, dx, dy, d, W, H):
    for i in range(len(x)) :
        dtX = d*dx[i]
        dtY = d*dy[i]
        x2 = x[i] + dtX
        y2 = y[i] + dtY
        

        if 0 <= x2 <= W :
            x[i] = x2
        else :
            x[i] = abs(W-abs(x2))
        
        if 0 <= y2 <= W :
            y[i] = y2
        else :
            y[i] = abs(H-abs(y2))

#-------------------------------------------
def neighbor_average_direction(x, y, dx, dy, k, R):
    N = len(x)
    aroundx = [0.0]*N
    aroundy = [0.0]*N
     
    for i in range(N) :
        if ((x[k] - x[i])**2) + ((y[k] - y[i])**2) <= R**2 :
            aroundx += [dx[i]]
            aroundy += [dy[i]]

    sigma_dx = sum(aroundx)
    sigma_dy = sum(aroundy)
    numbirdR_X = len(aroundx)
    numbirdR_Y = len(aroundy)
    
    avr_dx = sigma_dx / numbirdR_X
    avr_dy = sigma_dy / numbirdR_Y

    import math
    peta = math.sqrt(((avr_dx)**2) + ((avr_dy)**2))

    avr_dx = (avr_dx)/(peta)
    avr_dy = (avr_dy)/(peta)

    return(avr_dx,avr_dy)


    

        
    
        
        
        
        



#-------------------------------------------
main()