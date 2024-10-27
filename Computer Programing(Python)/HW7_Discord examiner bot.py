# HW7: Discord Examiner bot
# 6430110921 ณัฐชนน คงแก้ว
def sign_in(uid, sid, exam_info) :
    num = 0
    for e in exam_info :        
        if uid != e[0] and sid != e[1]  :
            num+= 1
        elif uid == e[0] or sid == e[1] :
            for info in exam_info:
                return info        
    if num == len(exam_info) :
        k = [uid,sid,[],[],0]
        exam_info.append(k)
        for info in exam_info:
            return info
def get_welcome_and_rules_msg():   
    x='ยินดีต้อนรับสู่การสอบกลางภาคครับนิสิต\nถ้าข้อสอบมีปัญหาตรงไหนให้แจ้งผู้คุมสอบได้เลยครับ\nกติกาการสอบ สามารถไปอ่านได้ที่mycorseville ครับ'        
    return x
def get_student_info(uid, exam_info):
    for e in exam_info :
        if e[0] == uid :
            return e  
import random
def get_question(uid, exam_info, all_questions):
    k = get_student_info(uid, exam_info)     
    if len(all_questions) == len(k[2]) :
        x = 'end'
        return x    
    if len(all_questions) > len(k[2]) :
        if k[4] == len(k[2]) :                       
            question_remain = []
            question_remain += all_questions
            for i in range(len(k[2])) :
                question_remain.remove(k[2][i])            
            x = random.choice(question_remain)
            question_remain.remove(x)            
            k[2].append(x)
            return str(x)
        if k[4] == len(k[2])-1 : 
            m = int(k[4])
            return k[2][m]
def submit_answer(uid, answer, exam_info):
    m = get_student_info(uid,exam_info)
    m[3].append(answer)    
    m[4] +=1
    return m




    





        




