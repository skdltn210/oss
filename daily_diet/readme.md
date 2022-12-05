# Daily Diet
사용자의 키, 몸무게, 체지방률 등을 이용하여 기초대사량과 소비칼로리 등을 계산하여 보여주는 프로그램입니다.

## Code explannation
* 라이브러리

    ```
    from tkinter import *
    import matplotlib.pyplot as plt
    import numpy as np
    ```

* 입력버튼 1

	사용자의 성별, 나이, 키, 체중, 체지방률을 입력해 권장 단백질 섭취량과 기초대사량을 계산합니다.

	<img width="621" alt="daily_diet1" src="https://user-images.githubusercontent.com/113167709/205621896-cd73854e-25cd-40c9-a248-04cee5bce9c3.png">

	```
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
	```
* 입력버튼2

	사용자의 식단관리 목표와 활동을 계산하여 활동대사량을 계산합니다.

	<img width="620" alt="daily_diet2" src="https://user-images.githubusercontent.com/113167709/205622005-9e04a1d9-43be-492a-b587-576a08d05eb8.png">
	
	```
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
	```
* 입력버튼 3(뚱이)

	탄수화물 비율과 섭취한 음식을 계산하여 영양소별 소비칼로리와 섭취한 칼로리를 계산하여 그래프로 보여줍니다.

	<img width="620" alt="daily_diet3" src="https://user-images.githubusercontent.com/113167709/205622055-34204c41-7e1b-4b3b-8c31-c18ce6553255.png">


	<img width="597" alt="graph" src="https://user-images.githubusercontent.com/113167709/205622114-0ed7a148-ccde-4bb3-9376-9a2f05b1de1d.png">

    '''
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

    ```
## References
* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)
* [tkinter](https://076923.github.io/posts/Python-tkinter-1/)
* inbody
## License

* MIT
