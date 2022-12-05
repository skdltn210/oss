from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

root=Tk()
root.title("Daily Diet")
root.geometry("620x720+100+0")
root.option_add("*Font","맑은고딕")
root.resizable(False,False)

image=PhotoImage(file="image.png")

def button1():
    global weight,bodyfat,age,height,protein,bmr,totalkcal,bmi
    weight=entry1.get()
    bodyfat=float(entry2.get())
    age=entry10.get()
    height=entry11.get()
    bmi=float(weight)/(float(height)/float(100))**2
    isbeginner=False
    if rv2.get()==0 :
        if bmi <= 18.5 and bodyfat <= 20:
            label27_1.configure(text="벌크업")
            isbeginner = True
        elif (bmi >= 18.5 and bmi <= 20.75) and bodyfat <= 15:
            label27_1.configure(text="벌크업 or 린매스업")
        elif (bmi >= 20.75 and bmi <= 23) and bodyfat <= 15:
            label27_1.configure(text="린매스업 or 커팅")
        elif bmi >= 23 and bodyfat <= 15:
            label27_1.configure(text="커팅")
        elif (bmi >= 18.5 and bmi <= 23) and (bodyfat >= 15 and bodyfat <= 20):
            label27_1.configure(text="린매스업 or 벌크업")
        elif bmi <= 20.75 and bodyfat >= 20:
            label27_1.configure(text="린매스업")
            isbeginner = True
        elif bmi >= 20.75 and bodyfat >= 20:
            label27_1.configure(text="다이어트")
        elif bmi >= 23 and (bodyfat >= 15 and bodyfat <= 20):
            label27_1.configure(text="다이어트 or 린매스업")
    elif rv2.get()==1 :
        if bmi <= 18.5 and bodyfat <= 28:
            label27_1.configure(text="벌크업")
            isbeginner = True
        elif (bmi >= 18.5 and bmi <= 20.75) and bodyfat <= 23:
            label27_1.configure(text="벌크업 or 린매스업")
        elif (bmi >= 20.75 and bmi <= 23) and bodyfat <= 23:
            label27_1.configure(text="린매스업 or 커팅")
        elif bmi >= 23 and bodyfat <= 23:
            label27_1.configure(text="커팅")
        elif (bmi >= 18.5 and bmi <= 23) and (bodyfat >= 23 and bodyfat <= 28):
            label27_1.configure(text="린매스업 or 벌크업")
        elif bmi <= 20.75 and bodyfat >= 28:
            label27_1.configure(text="린매스업")
            isbeginner = True
        elif bmi >= 20.75 and bodyfat >= 28:
            label27_1.configure(text="다이어트")
        elif bmi >= 23 and (bodyfat >= 23 and bodyfat <= 28):
            label27_1.configure(text="다이어트 or 린매스업")

    if isbeginner==True:
        protein = float(weight) * 2
    else :
        protein = float(weight) * 1.6

    label3_1.configure(text = f'{protein:.4}' + 'g')
    if rv2.get()==0 :
        bmr=66.47+float(weight)*13.75+5*float(height)-6.76*float(age)
        label4_1.configure(text = f'{bmr:.4f}' + 'kcal')
    elif rv2.get()==1 :
        bmr=655.1+float(weight)*9.56+float(height)*1.85-float(age)*4.68
        label4_1.configure(text=f'{bmr:.4f}' + 'kcal')
def button2():
    global totalkcal
    kcalchange=float(entry3.get())
    hour1 = float(entry4.get())
    hour2 = float(entry5.get())
    hour3 = float(entry6.get())
    hour4 = float(entry7.get())
    hour5 = float(entry8.get())
    hour6 = float(entry9.get())
    totalhour=float(hour1+hour2+hour3+hour4+hour5+hour6)
    if rv.get()==0:
        totalkcal=float(bmr)*1.4
        totalkcal=(24-totalhour)/float(24)*totalkcal\
                  +4.5*hour1/float(24)*totalkcal\
                  +6*hour2/float(24)*totalkcal\
                  +9*hour3/float(24)*totalkcal\
                  +3*hour4/float(24)*totalkcal\
                  +4.5*hour5/float(24)*totalkcal\
                  +6*hour6/float(24)*totalkcal
        totalkcal=totalkcal+kcalchange
        label17_1.configure(text =f'{totalkcal:.4f}'+ 'kcal')
    elif rv.get()==1:
        totalkcal = float(bmr) * 1.5
        totalkcal = (24 - totalhour) / float(24) * totalkcal \
                    + 4.5 * hour1 / float(24) * totalkcal \
                    + 6 * hour2 / float(24) * totalkcal \
                    + 9 * hour3 / float(24) * totalkcal \
                    + 3 * hour4 / float(24) * totalkcal \
                    + 4.5 * hour5 / float(24) * totalkcal \
                    + 6 * hour6 / float(24) * totalkcal
        totalkcal = totalkcal+kcalchange
        label17_1.configure(text=f'{totalkcal:.4f}' + 'kcal')
    elif rv.get() == 2:
        totalkcal = float(bmr) * 1.75
        totalkcal = (24 - totalhour) / float(24) * totalkcal \
                    + 4.5 * hour1 / float(24) * totalkcal \
                    + 6 * hour2 / float(24) * totalkcal \
                    + 9 * hour3 / float(24) * totalkcal \
                    + 3 * hour4 / float(24) * totalkcal \
                    + 4.5 * hour5 / float(24) * totalkcal \
                    + 6 * hour6 / float(24) * totalkcal
        totalkcal = totalkcal+kcalchange
        label17_1.configure(text=f'{totalkcal:.4f}' + 'kcal')
    elif rv.get() == 3:
        totalkcal = float(bmr) * 2
        totalkcal = (24 - totalhour) / float(24) * totalkcal \
                    + 4.5 * hour1 / float(24) * totalkcal \
                    + 6 * hour2 / float(24) * totalkcal \
                    + 9 * hour3 / float(24) * totalkcal \
                    + 3 * hour4 / float(24) * totalkcal \
                    + 4.5 * hour5 / float(24) * totalkcal \
                    + 6 * hour6 / float(24) * totalkcal
        totalkcal = totalkcal+kcalchange
        label17_1.configure(text=f'{totalkcal:.4f}' + 'kcal')
def button3():
    x = np.arange(3)
    nutrient = ['carbohydrate', 'protein', 'fat']
    carbopercent = float(entry12.get())
    carbohydratekcal = carbopercent / float(100) * float(totalkcal)
    proteinkcal = float(weight) * 1.6 * float(4)
    fatkcal = float(totalkcal) - carbohydratekcal - proteinkcal
    kcals = [carbohydratekcal, proteinkcal, fatkcal]

    ricecarbo=float(entry13.get())*float(65*4)
    riceprotein = float(entry13.get()) * float(3 * 4)

    chickenchestprotein=float(entry14.get())*float(0.23*4)
    pigneckprotein=float(entry15.get())*float(0.2*4)
    cowprotein=float(entry16.get())*float(0.2*4)
    piglegprotein=float(entry17.get())*float(0.213*4)
    proteinpowderprotein=float(entry18.get())*float(23*4)
    eggprotein=float(entry19.get())*float(7.4*4)

    chickenchestfat = float(entry14.get())*float(0.01*9)
    pigneckfat = float(entry15.get())*float(0.095*9)
    cowfat = float(entry16.get())*float(0.1*9)
    piglegfat = float(entry17.get())*float(0.033*9)
    proteinpowderfat = float(entry18.get())*float(2*9)
    eggfat=float(entry19.get())*float(4.4*9)

    eatcarbo=ricecarbo
    eatprotein=riceprotein+chickenchestprotein+piglegprotein+pigneckprotein+cowprotein+proteinpowderprotein+eggprotein
    eatfat=chickenchestfat+piglegfat+pigneckfat+cowfat+proteinpowderfat+eggfat
    eatkcals=[eatcarbo,eatprotein,eatfat]



    b1 = plt.bar(x, kcals, color=['r', 'g', 'b'], width=0.4)
    b2 = plt.bar(x+0.4,eatkcals, color=['m','y','c'],width=0.4)

    plt.xticks(x+0.2, nutrient)

    plt.title("calories per nutrient")

    plt.text(-0.1, 1.0, f'{carbohydratekcal:.0f}')
    plt.text(0.9, 1.0, f'{proteinkcal:.0f}')
    plt.text(1.9, 1.0, f'{fatkcal:.0f}')
    plt.text(0.3, 1.0, f'{eatcarbo:.0f}')
    plt.text(1.3, 1.0, f'{eatprotein:.0f}')
    plt.text(2.3, 1.0, f'{eatfat:.0f}')
    plt.xlabel('total calories = ' + f'{totalkcal:.0f}' + 'kcal')
    plt.ylabel('kcal')

    plt.show()

btn1 = Button(root, text="입력")
btn1.config(width=5,height=3)
btn1.config(command=button1)
btn1.place(x=250, y=120)

btn2 = Button(root, text="입력")
btn2.config(width=5,height=3)
btn2.config(command=button2)
btn2.place(x=250,y=630)

btn3 = Button(root, image=image)
btn3.config(command=button3)
btn3.place(x=350,y=240)
rv=IntVar()
rb1=Radiobutton(root,value=0,variable=rv)
rb2=Radiobutton(root,value=1,variable=rv)
rb3=Radiobutton(root,value=2,variable=rv)
rb4=Radiobutton(root,value=3,variable=rv)
rb1.place(x=150,y=570)
rb2.place(x=150,y=600)
rb3.place(x=150,y=630)
rb4.place(x=150,y=660)

rv2=IntVar()
rb1=Radiobutton(root,text='남성',value=0,variable=rv2)
rb2=Radiobutton(root,text='여성',value=1,variable=rv2)
rb1.place(x=0,y=0)
rb2.place(x=0,y=30)

label18 = Label(root, text='나이를 입력하세요.')
label18.place(x=0,y=60)

entry10 = Entry(root,width=10)
entry10.place(x=150,y=60)

label19 = Label(root, text='키를 입력하세요.(cm)')
label19.place(x=0,y=90)

entry11 = Entry(root,width=10)
entry11.place(x=150,y=90)

label1 = Label(root, text='체중을 입력하세요.(kg)')
label1.place(x=0,y=120)

entry1 = Entry(root,width=10)
entry1.place(x=150,y=120)

label2 = Label(root, text='체지방률을 입력하세요.(%)')
label2.place(x=0,y=150)

entry2 = Entry(root,width=10)
entry2.place(x=150,y=150)


label3 = Label(root, text='권장 단백질 섭취량 : ')
label3.place(x=0,y=180)

label3_1 = Label(root,text="")
label3_1.place(x=150, y=180)

label4 = Label(root, text='기초 대사량 : ')
label4.place(x=0,y=210)

label4_1 = Label(root,text="")
label4_1.place(x=150,y=210)

label9= Label(root, text="변경할 칼로리 입력 ")
label9.place(x=0,y=265)

entry3=Entry(root,width=10)
entry3.place(x=150,y=265)

label27=Label(root,text="추천 체중관리 : ")
label27.place(x=0,y=240)

label27_1=Label(root,text="")
label27_1.place(x=150,y=240)

label10 =Label(root, text="*린매스업 +-200 kacl")
label10.place(x=0,y=290)

label11= Label(root, text="*벌크업 +200~300 kcal")
label11.place(x=0,y=310)

label12= Label(root, text="*다이어트 -500~-700 kacl")
label12.place(x=0,y=330)

label5 = Label(root, text='빈둥빈둥')
label5.place(x=0,y=570)

label6 = Label(root, text='좌식업무')
label6.place(x=0,y=600)

label7= Label(root, text='돌아다니는 업무')
label7.place(x=0,y=630)

label8= Label(root, text='활동적인 업무')
label8.place(x=0,y=660)

label13= Label(root, text="소비 칼로리 추가                  시간(hour)")
label13.place(x=0,y=360)


label14= Label(root, text="*유산소(약)")
label14.place(x=0,y=390)

entry4 = Entry(root,width=10)
entry4.place(x=150,y=390)

label15= Label(root, text="*유산소(중)")
label15.place(x=0,y=420)

entry5 = Entry(root,width=10)
entry5.place(x=150,y=420)

label16= Label(root, text="*유산소(강)")
label16.place(x=0,y=450)

entry6 = Entry(root,width=10)
entry6.place(x=150,y=450)

label14= Label(root, text="*근력운동(약)")
label14.place(x=0,y=480)

entry7 = Entry(root,width=10)
entry7.place(x=150,y=480)

label15= Label(root, text="*근력운동(중)")
label15.place(x=0,y=510)

entry8 = Entry(root,width=10)
entry8.place(x=150,y=510)

label16= Label(root, text="*근력운동(강)")
label16.place(x=0,y=540)

entry9 = Entry(root,width=10)
entry9.place(x=150,y=540)

label17= Label(root, text="활동 대사량(섭취할 칼로리) : ")
label17.place(x=0,y=695)

label17_1 = Label(root,text="")
label17_1.place(x=150, y=695)

label18= Label(root, text="탄수화물 비율(50%~70%)")
label18.place(x=350,y=0)

entry12 = Entry(root,width=10)
entry12.place(x=500,y=0)

label20 = Label(root,text="밥(공기)")
label20.place(x=350, y=30)

entry13 = Entry(root,width=10)
entry13.place(x=500,y=30)

label21 = Label(root,text="닭가슴살(g)")
label21.place(x=350, y=60)

entry14 = Entry(root,width=10)
entry14.place(x=500,y=60)

label22 = Label(root,text="목살(g)")
label22.place(x=350, y=90)

entry15 = Entry(root,width=10)
entry15.place(x=500,y=90)

label23 = Label(root,text="소고기(g)")
label23.place(x=350, y=120)

entry16 = Entry(root,width=10)
entry16.place(x=500,y=120)

label24 = Label(root,text="뒷다리살(g)")
label24.place(x=350, y=150)

entry17 = Entry(root,width=10)
entry17.place(x=500,y=150)

label25 = Label(root,text="보충제(스쿱)")
label25.place(x=350, y=180)

entry18 = Entry(root,width=10)
entry18.place(x=500,y=180)

label26 = Label(root,text="계란")
label26.place(x=350, y=210)

entry19 = Entry(root,width=10)
entry19.place(x=500,y=210)

root.mainloop()