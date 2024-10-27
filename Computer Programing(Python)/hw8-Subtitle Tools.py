# Subtitle Tools
# Your ID 6430110921

def changesec(t):  #เปลี่ยนt1,t2 ที่ได้มาเป็นรูปแบบ 04,442
    n = 5
    k ="0"*(max(len(str(t)),n)-len(str(t))) + str(t)
    lst =[]
    for e in k :
        lst.append(e)
    lst.insert(2,',')
    milsec = ''
    for e in lst :
        milsec+= e
    return milsec

def changeHrMin(t):  #เปลี่ยนt1,t2 ที่ได้มาเป็นรูปแบบ 04,442
    n = 2
    k ="0"*(max(len(str(t)),n)-len(str(t))) + str(t)
    lst =[]
    for e in k :
        lst.append(e)
    lst.insert(2,',')
    milsec = ''
    for e in lst :
        milsec+= e
    return k


def time_that_shift(h1,m1,s1,time_shift) :
    t1 = (h1*3600000)+(m1*60000)+s1
    t2 = time_shift
    dt = t1 +t2
    dh = dt//3600000%24 #shoild = 0
    dm = dt//60000%60 #should = 0
    ds = dt%60000
    milsec = changesec(ds)
    minn = changeHrMin(dm)
    hr = changeHrMin(dh)
    time = str(hr)+":"+str(minn)+":"+str(milsec)
    if dt > 0 :
        return time
    else :
        return 'ku'

def time_that(h1,m1,s1) :
    t1 = (h1*3600000)+(m1*60000)+s1
    
    dt = t1 
    dh = dt//3600000%24 #shoild = 0
    dm = dt//60000%60 #should = 0
    ds = dt%60000
    milsec = changesec(ds)
    minn = changeHrMin(dm)
    hr = changeHrMin(dh)
    time = str(hr)+":"+str(minn)+":"+str(milsec)
    if dt > 0 :
        return time
    else :
        return 'ku'

def data_to_lst(opfile) :
    data =''
    for line in opfile :  
        data+=line
    x = data.split('\n')
    mini = []
    lst = []
    de1 = []
    bignew = []
    BIGNEw = []

    for e in x :
        if '0'< e < '9999999' :
            de1.append(e)

    for i in range(len(x)) :
        d = x[i]
        while d != '' :
            mini.append(d)
            break
        if d == '':
            k = []
            k+= mini
            lst.append(k)
            mini =[]
    

    for e in lst :
        if e == [] :
            lst.remove([])
    return lst

def ttmilsec(h1,m1,s1) :
    ttms = (h1*3600000)+(m1*60000)+s1
    return ttms

def Hi_superlistENG(nume,superlist) :
    t = superlist[0][nume][1].split(' --> ') 
    s11 = int(t[0][6:8] +t[0][9:12])
    m1 = int(t[0][3:5])
    h1 = int(t[0][0:2])
    totalmilseceng = ttmilsec(h1,m1,s11)

    return totalmilseceng

def Hi_superlistTHAI(numt,superlist) :
    m = superlist[1][numt][1].split(' --> ')
    sm11 = int(m[0][6:8] +m[0][9:12])
    mm1 = int(m[0][3:5])
    hm1 = int(m[0][0:2])
    totalmilsecthai = ttmilsec(hm1,mm1,sm11)

    return totalmilsecthai

def contimeE(nume,superlist) :
    t = superlist[0][nume][1].split(' --> ')
    s11 = int(t[0][6:8] +t[0][9:12])
    s21 = int(t[1][6:8] +t[1][9:12])
    m1 = int(t[0][3:5])
    m2 = int(t[1][3:5])
    h1 = int(t[0][0:2])
    h2 = int(t[0][0:2])
    tt1 = time_that(h1,m1,s11)
    tt2 = time_that(h2,m2,s21)
    tt =  tt1 + ' --> ' + tt2
    
    return tt

def contimeT(numt,superlist) :
    m = superlist[1][numt][1].split(' --> ') 
    sm11 = int(m[0][6:8] +m[0][9:12])
    mm1 = int(m[0][3:5])
    hm1 = int(m[0][0:2])
    hm2 = int(m[0][0:2])
    mm2 = int(m[1][3:5])
    sm21 = int(m[1][6:8] +m[1][9:12])
    mm1 = time_that(hm1,mm1,sm11)
    mm2 = time_that(hm2,mm2,sm21)
    mm = mm1 + ' --> ' + mm2

    return mm
    # ------------------------------------------


def shift(file_in, time_shift, file_out):
    op1 = open(file_in , encoding = 'utf-8')
    data ='' #1\n00:00:04,000 --> 00:00:05,000\nEEEEE, E'E EEEEEE EEEE.
    for line in op1 :
        data+=line
    x = data.split('\n')
    mini = []
    big = []
    de1 = []
    bignew = []
    BIGNEw = []
#data = ['1', '00:00:04,000 --> 00:00:05,000',"EEEEE, E'E EEEEEE EEEE.", '', '2', '00:00:05,000 --> 00:00:08,000', '[EEEEE EEEEEEEE EEE EEEEEEEEEE]', '', '3', '00:00:08,000 --> 00:00:11,000', '[EEEEEE EEEEEEE EEEEE EEEEEEE] â™ªâ™«', '', '4', '00:00:11,000 --> 00:00:12,500', 'â™ªâ™ªâ™ª', '', '5', '00:00:13,000 --> 00:00:17,000', "â™ª E EEEE EEE EEEEE E EEEEE'", "EE'E EEEEEEE EEEEE EEE EEEE â™ª", '', '']
    for e in x :
        if '0'< e < '9999999' :
            de1.append(e)

    for i in range(len(x)) :
        d = x[i]
        while d != '' :
            mini.append(d)
            break
        if d == '':
            mini += ['']
            k = []
            k+= mini
            big.append(k)
            mini =[]
    time_shift = int(input())

    for e in big :
        if e == [''] :
            big.remove([''])
    
    count = 0
    for e in big :
        
        t = e[1].split(' --> ') 
        s11 = int(t[0][6:8] +t[0][9:12])  #ตัวแรก
        s21 = int(t[1][6:8] +t[1][9:12])  #ตัวหลัง
        m1 = int(t[0][3:5])
        m2 = int(t[1][3:5])
        h1 = int(t[0][0:2])
        h2 = int(t[0][0:2])

        if time_shift   > 0 :
            tt1 = time_that_shift(h1,m1,s11,time_shift) 
            tt2 = time_that_shift(h2,m2,s21,time_shift) 

            tt = tt1 + ' --> ' + tt2 
            count +=1
  
            bignew.append(count)
            bignew.append(tt)
            for i in range(2,len(e)) :
                bignew.append(e[i])
            ppp = []
            ppp += bignew
            BIGNEw.append(ppp)
            bignew = []
        
        if time_shift  < 0 :
            
            tt1 = time_that_shift(h1,m1,s11,time_shift) 
            tt2 = time_that_shift(h2,m2,s21,time_shift)

            if tt1 != 'ku'  and tt2 != 'ku' :
                tt =  tt1 + ' --> ' + tt2 
                count += 1
                bignew.append(count)
                bignew.append(tt)
                for i in range(2,len(e)) :
                    bignew.append(e[i])
                ppp = []
                ppp += bignew
                BIGNEw.append(ppp)
                bignew = []

            if tt1 == 'ku'  and tt2 != 'ku' :
                tt1 = '00:00:00,000'
                tt =  tt1 + ' --> ' + tt2 
                count += 1
                
                bignew.append(count)
                bignew.append(tt)
                for i in range(2,len(e)) :
                    bignew.append(e[i])
                ppp = []
                ppp += bignew
                BIGNEw.append(ppp)
                bignew = []


            if tt1 == 'ku'  and tt2 == 'ku':
                count +=0
    op1.close()
        

    op2 = open(file_out,'w',encoding ='utf-8')

    for e in BIGNEw:
        k = e
        for i in k:
            op2.write(str(i)+'\n')
    op2.close()    

    return

#shift('test1_en.srt', 4444, 'out_put.srt')

# ------------------------------------------
def merge(base_file, merge_file, threshold, file_out):
    openg = open(base_file , encoding = 'utf-8')
    opthai = open(merge_file , encoding = 'utf-8')
    #lstsubeng = data_to_lst(openg)
    #lstsubthai = data_to_lst(opthai)
    #openg = open('test4_en.srt' , encoding = 'utf-8')
    #opthai = open('test4_th.srt' , encoding = 'utf-8')

    lstsubeng = data_to_lst(openg)
    lstsubthai = data_to_lst(opthai)
    superlist = []
    superlist.append(lstsubeng)
    superlist.append(lstsubthai)
#superlist = [ [ [1,เวลา,subeng],[2,เวลา,subeng],[3,เวลา,subeng] ]  ,  [ [1,เวลา,ซับไทย],[2,เวลา,ซับไทย],[3,เวลา,ซับไทย] ] ]
#print(superlist)
    import math
    mac = max(len(superlist[0]),len(superlist[1]))
    out = []
    numt = 0
    nume = 0
    num = 1
    for i in range(mac-2) :
    
        jettdiff = abs(Hi_superlistTHAI(numt,superlist) - Hi_superlistENG(nume,superlist))
        tt = contimeE(nume,superlist)  #xxxx --> xxxx
        mm = contimeT(numt,superlist)  #xxxx --> xxxx

        if jettdiff <= threshold :
            out.append(num)
            num += 1
            out.append(tt)
            for k in range(2,len(superlist[0][nume])) :
                out.append(superlist[0][nume][k])
            nume +=1
    
            for k in range(2,len(superlist[1][numt])) :
                out.append(superlist[1][numt][k])
            out.append('')
            numt +=1

        if jettdiff > threshold :
            out.append(num)
        
            if Hi_superlistENG(nume,superlist) < Hi_superlistTHAI(numt,superlist) : #ปริ้นตัวeng เพราะเวลาน้อยกว่า
                out.append(tt)

                for k in range(2,len(superlist[0][nume])) :
                    out.append(superlist[0][nume][k])
                out.append('')

                nume += 1
                num +=1

                while  Hi_superlistENG(nume,superlist) < Hi_superlistTHAI(numt,superlist)  and abs(Hi_superlistTHAI(numt,superlist) - Hi_superlistENG(nume,superlist)) > threshold :
                    for k in range(2,len(superlist[0][nume])) :
                        out.append(num)
                        tt = contimeE(nume,superlist) 
                        out.append(tt)
                        out.append(superlist[0][nume][k])
                    out.append('')
                    nume += 1
                    num+=1
            
        
            else :
                out.append(mm)
                for k in range(2,len(superlist[1][numt])) :
                    out.append(superlist[1][numt][k])
                out.append('')
                numt +=1
                num += 1
                while  Hi_superlistENG(nume,superlist) > Hi_superlistTHAI(numt,superlist) and abs(Hi_superlistTHAI(numt,superlist) - Hi_superlistENG(nume,superlist)) > threshold :
                    for k in range(2,len(superlist[1][numt])) :
                        out.append(num)
                        mm = contimeT(numt,superlist)
                        out.append(mm)
                        out.append(superlist[1][numt][k])
                        out.append('')
                    numt += 1
                    num+=1
            
    if numt < len(superlist[1]) :
      #xxxx --> xxxx
        mm = contimeT(numt,superlist)  #xxxx --> xxxx

        out.append(num)
        out.append(mm)
        for k in range(2,len(superlist[1][numt])) :
            out.append(superlist[1][numt][k])
        out.append('')
    
    if nume < len(superlist[0]) :
        tt = contimeE(nume,superlist)  #xxxx --> xxxx
      #xxxx --> xxxx

        out.append(num)
        out.append(mm)
        for k in range(2,len(superlist[0][nume])) :
            out.append(superlist[0][nume][k])
        out.append('')
    

    openg.close()
    opthai.close()
    op3 = open(file_out,'w',encoding ='utf-8')

    for e in out:
        k = e
        op3.write(str(k)+'\n')
    op3.close()    
        
    
    return


#merge('test2_en.srt', 'test2_th.srt', 1000, 'ter.srt')




    #return

# ------------------------------------------
#def clean(file_in, file_out):
   # return

