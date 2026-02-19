
#Cristiano Ronaldo face pattern
def face_pattern():
    rows = 40
    columns = 50

    for i in range(rows):
        for j in range(columns):
            char = " "

            
            if i == 0 and (22<=j<=32):
                char = "%"
            elif i == 1 and (21<=j<=33):
                char = "%"
            
            elif i == 2 and (18 <= j <= 35):
                char = "%"
            elif i==3 and (15<j<36):
                char="%"
            elif i==4 and (17<=j<=37):
                char="@" 
            elif i==5 and (16<=j<=37 ):
                char="@"
            elif  i==6 and (13<=j<=38):
                char="@"
            elif  i==7 and (12<=j<=39):
                char="@"
            elif  i==8 and (13<=j<=38):
                char="@"
            elif  i==9 and (12<=j<=41):
                char="@"
            elif  i==10 and (13<j<=40 ):
                char="@"
            elif  i==11 and (11<=j<=16 or 34<=j<=42):
                char="@"
            elif  i==11 and (17<=j<=33):
                char="+"
            elif  i==12 and (17<=j<=35):
                char="+"
            elif  i==12 and (12<=j<=16 or 36<=j<=42):
                char="%"
            elif  i==13 and (11<=j<=15 or 38<=j<=43):   
                char="%"
            elif  i==13 and (16<=j<=37):
                char="+"
            elif  i==14 and (11<=j<=15 or 38<=j<=42):   
                char="%"
            elif  i==13 and (16<=j<=37):
                char="+"
            elif  i==14 and (16<=j<=37):
                char=":"
            elif  i==15 and (14<=j<=38):
                char="+"
            elif  i==14 and (11<=j<=15 or 38<=j<=42):   
                char="%"
            elif  i==14 and (16<=j<=37):
                char="+"
            elif  i==15 and (10<=j<=13 or 39<=j<=42):   
                char="%"
            elif  i==16 and (10<=j<=12 or 39<=j<=42):   
                char="%"
            elif  i==16 and (13<=j<=38):
                char="+"
            elif  i==17 and (12<=j<=39):
                char="+"
            elif  i==17 and (10<=j<=11 or 40<=j<=41):   
                char="%"
            elif  i==18 and (10<=j<=11 or 39<=j<=41):
                char="%" 
            elif  i==18 and (12<=j<=13 or 19<=j<=28 or 34<=j<=38):
                char=":" 
            elif  i==18 and (j==14 or j==15 or j==16 or j==17 or j==18 or j==30 or j==29 or j==28 or j==31 or j==32 or j==33):
                char="*"
            elif  i==19 and (j==15 or j==16 or j==17 or j==18 or j==30 or j==29  or j==31 or j==32 or j==33):
                char="*"
            elif  i==19 and (12<=j<=14 or 19<=j<=28 or 34<=j<=38):
                char=":" 
            elif  i==19 and (10<=j<=11 or 39<=j<=41):
                char="%"
            elif  i==20 and (12<=j<=40 ):
                char="+"
            elif  i==20 and (10<=j<=11 or 41<=j<=43):
                char="%"
            elif  i==21 and (10<=j<=12 or 41<=j<=44):
                char="%"
            elif  i==21 and (13<=j<=40 ):
                char="+"
            elif  i==22 and (11<=j<=12 or 41<=j<=44):
                char="%"
            elif  i==22 and (13<=j<=40 ):
                char="+"
            elif  i==23 and (11<=j<=12 or 41<=j<=43):
                char="%"
            elif  i==23 and (13<=j<=40 ):
                char=":"
            elif  i==24 and (11<=j<=12 or 41<=j<=43):
                char="%"
            elif  i==24 and (13<=j<=40 ):
                char="="

            elif  i==25 and (j == 11 or 40<=j<=42):
                char="%"
            elif  i==25 and (22<=j<=30 ):
                char="*"
            elif i==25 and (12<=j<=21 or 31<=j<=39):
                char="+"
            elif  i==26 and (j == 11 or 41<=j<=42):
                char="%"
            elif  i==26 and (21<=j<=31 ):
                char="*"
            elif i==26 and (12<=j<=20 or 30<=j<=40):
                char=":"
            elif  i==27 and (j == 11 or 41<=j<=42):
                char="%"
            elif  i==27 and (21<=j<=31 ):
                char="*"
            elif i==27 and (12<=j<=20 or 32<=j<=40):
                char="+"
            elif i==28 and (12<=j<=39):
                char="+"
            elif  i==28 and (j == 11 or j==40):
                char="%"
            elif  i==29 and (j == 13 or j==39):
                char="%"
            elif  i==29 and (14<=j<=38):
                char="+"
            elif  i==30 and (j==13 or j==39):
                char="%"
            elif  i==30 and (20<=j<=32):
                char="*"
            elif i==30 and (12<=j<=19 or 33<=j<=40):
                char="+"
            elif  i==31 and (j==13 or j==38):
                char="%"
            elif  i==31 and (20<=j<=32):
                char="*"
            elif  i==31 and (14<=j<=19 or 33<=j<=37):
                char="+"
            elif i==30 and (14<=j<=19 or 33<=j<=37):
                char="+"
            elif  i==32 and (j==14 or j==38):
                char="%"
            elif  i==32 and (15<=j<=37):
                char=":"
            elif  i==33 and (j==14 or j==37):
                char="%"
            elif  i==33 and (15<=j<=36):
                char="+"
            elif  i==34 and (j==14 or j==38):
                char="%"
            elif  i==34 and (15<=j<=37):
                char="="
            elif  i==35 and (j==15 or j==38):
                char="%"
            elif  i==35 and (15<=j<=37):
                char="?"
            elif  i==36 and (j==15 or j==16 or 35<=j<=38):
                char="%"
            elif  i==36 and (17<=j<=34):
                char=":"
            elif  i==37 and (j==15 or j==16 or j==35 or j==38 or j==36 or j==37):
                char="%"
            elif  i==37 and (17<=j<=34):
                char=":"
            elif  i==38 and (16<=j<=19 or 34<=j<=38):
                char="%"
            elif  i==38 and (20<=j<=33):
                char=":"
            elif  i==39 and (j==16 or 22<=j<=31 or j==41 ):
                char=":"
            elif  i==39 and (17<=j<=21 or 32<=j<=40 ):
                char="%"
            
           

            print(char, end="")
        print()   # new line after each row

face_pattern()
