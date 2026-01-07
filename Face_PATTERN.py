#Simone Biles face pattern
def face_pattern():
    rows = 35
    columns = 40

    for i in range(rows):
        for j in range(columns):
            char = " "

            
            if i == 0 and (15<=j<=25):
                char = "%"
            elif i == 1 and (j == 15 or j == 16 or j == 24 or j == 25 or j == 14 or j == 26 or j == 17 or j == 23 or j == 18 or j == 22 or j == 19 or j == 21):
                char = "@"
            elif i == 2 and (13 <= j <= 18 or 22 <= j <= 28):
                char = "@"
            elif i == 2 and (19 <= j <= 21):
                char = "@"
            elif i==1 and (j==20):
                char="@"
            elif i==3 and (j==12 or j==29):
                char="@"
            elif i==3 and (12<j<29):
                char="%"
            elif i==4 and (10<j<31):
                char="@" 
            elif i==5 and (11<=j<=13 or 17<=j<=23 or 27<=j<=30):
                char="@"
            elif  i==6 and (11<j<30):
                char="@"
            elif  i==7 and (11<j<30):
                char="@"
            elif  i==8 and (12<j<29):
                char="@"
            elif  i==9 and (13<j<28):
                char="@"
            elif  i==10 and (14<j<=18 or 23<=j<=26):
                char="@"
            elif  i==11 and (15<j<26):
                char="@"
            elif  i==12 and (16<j<26):
                char="@"
            elif  i==13 and (17<j<25):
                char="@"
            elif  i==14 and (14<j<28):
                char="%"   
            elif  i==15 and (9<j<34):
                char="@"
            elif  i==16 and (6<j<36):
                char="@"
            elif  i==17 and (4<j<38):
                char="@"
            elif i== 5 and (14<=j<=16 or  24<=j<=26):
                char="."
            elif  i==10 and (19<=j<=22):
                char="."
            elif  i==18 and (2<j<40):
                char="%"
            elif  i==19 and (2<j<40):
                char="@"
            elif  i==20 and (2<j<40):
                char="#"
            elif  i==14 and (11<=j<=14 or 28<=j<=32):
                char="." 
            elif  i==13 and (15<=j<=17 or 25<=j<=27):
                char="."
            elif i==6 and (j==11 or j==10 or j==30 or j==31):
                char="%"
            elif i==5 and ( j==10 or  j==31):
                char="%"
            elif  i==7 and (j==11 or j==30):
                char="%"
            
            print(char, end="")
        print()   # new line after each row

face_pattern()
