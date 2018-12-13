import webbrowser as wb
import pyautogui as pg
import time as t
points = 0

show = pg.prompt ("What is your favorite show?").lower()
if show == "modern family":
    wb.open ("https://www.youtube.com/watch?v=cGaoD4aPnUw")
    t.sleep (10)
    pg.alert ("That is a really good show!")
    points += 5
elif show == "friends":
    wb.open ("https://www.youtube.com/watch?v=Niu9Zmrx0p8")
    t.sleep (15)
    pg.alert ("Oh I love that show!")
    points += 8
elif show == "insatiable":
    pg.alert (" I love that show even though it gets really intense!")
    points +=  3
elif show == "full house":
    wb.open ("https://www.youtube.com/watch?v=8qp4WJiUeTc")
    t.sleep (10)
    pg.alert ("I remember that show!")
elif show == "my little pony":
    wb.open ("https://www.youtube.com/watch?v=ZcBNxuKZyN4")
    t.sleep (7)
    pg.alert ("That's what I am being for Halloween!")
    points += 15
elif show == "gossip girl":
    pg.alert ("Oh I don't watch that show but it sounds really good!")
    points += 2
else:
    pg.alert ("Your favorite show is " + show)

t.sleep (5)
    
icecreamflavor = pg.prompt ("What is your favorite ice cream flavor? ").lower()

if icecreamflavor == "vanilla":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&tbm=isch&q=vanilla+ice+cream&chips=q:vanilla+ice+cream,g_1:homemade:ttJgBillyEQ%3D&usg=AI4_-kRLYjeBZAvEBbCJIhF3cWCmwoTUhw&sa=X&ved=0ahUKEwj8j6vbubPeAhWrnuAKHdVeAcIQ4lYIKygC&biw=1347&bih=684&dpr=0.9")
    pg.alert ("Oh what a classic.")
    points += 3
elif icecreamflavor == "chocolate":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=7BPbW9rZOKayggftk6KYDw&q=chocolate+ice+cream&oq=chocolate+ice+cream&gs_l=img.3..0i67j0l4j0i67j0j0i67j0l2.37569.41982..42518...3.0..0.63.712.13......0....1..gws-wiz-img.......0i7i30.24Ql81dhyzo")
    pg.alert ("Oooo that sounds really good right now.")
    points += 2
elif icecreamflavor == "chocolate chip cookie dough":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=GBTbW8CKE8ek_Qa49qrADw&q=chocolate+chip+cookie+dough+ice+cream&oq=chocolate+chip+cookie+dough+ice+cream&gs_l=img.3..0l8j0i5i30l2.38826.48355..48921...5.0..0.64.1641.31......0....1..gws-wiz-img.......0i7i30j0i67j0i7i5i30.U035Jp6dg9g")
    pg.alert ("That is no joke my FAVORITE")
    points += 15
elif icecreamflavor == "strawberry":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=SRTbW6mYOoSb_Qb4p6eoCg&q=strawberry+ice+cream&oq=strawberry+ice+cream&gs_l=img.3..0j0i67j0l3j0i67j0l4.19552.21593..22121...0.0..0.58.532.10......0....1..gws-wiz-img.......0i7i30.qr1-jzgWNok")
    pg.alert ("Oh I like that sometimes.")
    points += 2
elif icecreamflavor == "mint-chocolate chip":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=YBTbW8qBOO-l_QaJo77QAg&q=mint+chocolate+chip+ice+cream&oq=mint+ch+ice+cream&gs_l=img.3.0.0i7i30l10.24014.26270..27442...0.0..0.82.405.7......0....1..gws-wiz-img.......0j0i67.Ym975054D40")
    pg.alert ("I need to be in the mood for it")
    points += 2
elif icecreamflavor == "triple fudge":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=fRTbW-z6B8mf_QaSw7z4DQ&q=triple+fudge+ice+cream&oq=triple+fudge+ice+cream&gs_l=img.3..0j0i7i30j0i8i30l2.19376.21718..22360...0.0..0.61.632.12......0....1..gws-wiz-img.......0i7i5i30j0i8i7i30.5HArxMt28to")
    pg.alert ("I am REALLY in the mood for that right now!")
    points += 15
else:
    pg.alert ("Your favorite ice cream flavor is " + icecreamflavor)

t.sleep (5)

color = pg.prompt ("What is your favorite color? ").lower()

if color == "pink":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=yRTbW-3WOYTv_Qb8p4DADg&q=pink+flowers&oq=pink+flowers&gs_l=img.3..0l10.4673.6039..6231...0.0..0.74.374.7......0....1..gws-wiz-img.......0i67.f0suvXoSK6c")
    pg.alert ("We are a perfect match!")
    points += 5
elif color == "blue":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=0RTbW-6mBcK0ggfWw4kw&q=blue+flowers&oq=blue+flowers&gs_l=img.3..0i67j0l7j0i67j0.19419.19999..20233...0.0..0.54.214.4......0....1..gws-wiz-img.......0i7i30j0i10i67j0i10.b7_acZkyy7E")
    pg.alert ("It's pretty but not my favorite")
    points += 3
elif color == "purple":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=5hTbW-_RBazn_Qazg5iABg&q=purple+flowers&oq=purple+flowers&gs_l=img.3..0i67j0l4j0i67j0j0i67j0j0i67.43892.49542..49763...8.0..0.59.718.14......0....1..gws-wiz-img.......0i7i30.glVSskIhCQY")
    pg.alert ("I like purple but I like pink bettter")
    points += 2
elif color == "green":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=GBXbW_uLLcG6ggf3-qLgDQ&q=green+flowers&oq=green+flowers&gs_l=img.3..0l8j0i67j0.17414.20385..20773...2.0..0.59.547.10......0....1..gws-wiz-img.......0i7i30j0i10.h1Em2vdz7tc")
    pg.alert ("Ehh sort of reminds me of puke")
    points -= 10
elif color == "orange":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=LhXbW6rWCYa-ggeqrqOQDg&q=orange+flowers&oq=or+flowers&gs_l=img.3.0.0i7i30l7j0i7i5i30l3.59290.59478..60952...0.0..0.69.121.2......0....1..gws-wiz-img.......0.PrISCdJAXLc")
    pg.alert ("I don't really like that color")
    points -= 10
elif color == "red":
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US752&biw=1347&bih=684&tbm=isch&sa=1&ei=axXbW7iDNdGp_QagsLKwDw&q=red+flowers&oq=red+flowers&gs_l=img.3..0i67j0l7j0i67j0.15982.17356..17915...0.0..0.55.213.4......0....1..gws-wiz-img.......0i7i30j0i10.5XnKXw-g2Qc")
    pg.alert ("I am ok with that because it is close to pink")
    points += 5
else:
    pg.alert ("Oh I didn't even think of that color!")

t.sleep (5)

sports = pg.prompt ("What is your favorite sport? ").lower()
           
if sports == "dance":
    wb.open ("https://www.youtube.com/watch?v=kMxjO0c5ZR4")
    pg.alert ("I do Irish Step Dancing!")
    points += 5
elif sports == "lacrosse":
    wb.open ("https://www.youtube.com/watch?v=clNEQWl9fkk")
    pg.alert ("I am really bad at it but my brother does it")
    points += 3
elif sports == "soccer":
    wb.open ("https://www.youtube.com/watch?v=JQNNcB2ciFM")
    pg.alert ("I normally trip over the ball")
    points += 2
elif sports == "tennis":
    pg.alert ("I am SOOO bad at tennis")
    points -=5
elif sports == "skiing":
    wb.open ("https://www.youtube.com/watch?v=Zs4BZASGoDw")
    pg.alert ("I have only been once and I was 3")
    points -= 2
elif sports == "hockey":
    wb.open ("https://www.youtube.com/watch?v=StmI5v-VNss")
    pg.alert ("I can skate but I am not very fast")
    points -= 4
else:
    pg.alert ("Oh I didn't even think of that sport!")

t.sleep (5)

animal = pg.prompt ("What is your favorite animal?").lower()

if animal == "dog":
    wb.open ("https://www.instagram.com/p/BBgyt-dHqDLVZyZMHH6aLHgP0uMOnWpJ0R2rvM0/?taken-by=vivdixon72")
    pg.alert ("I That's mine too!!")
    points += 5
elif animal == "cat":
    wb.open ("https://www.instagram.com/p/zprdidHqDXG6h32X6ja5y2kud4QP2HWSn40ng0/")
    pg.alert ("They are cute but can be sort of boring at times")
    points += 2
elif animal == "elephant":
    wb.open ("https://www.youtube.com/watch?v=SNggmeilXDQ")
    pg.alert ("I LOVE ELEPHANTS!")
    points += 10
elif animal == "lion":
    wb.open ("https://www.youtube.com/watch?v=PjjIQvjZ1Qc")
    pg.alert ("That is so cool!")
    points += 8
elif animal == "hamster":
    wb.open ("https://www.youtube.com/watch?v=JTWhGShZdYE")
    pg.alert ("They sort of smell a little but they can be cute")
    points -= 3
elif animal == "snake":
    wb.open ("https://www.youtube.com/watch?v=4Chgih5FqSE")
    pg.alert ("They creep me out")
    points -= 5
else:
    pg.alert ("Oh nice animal!")

t.sleep (5)

pg.alert ("you scored: " + str(points) + " on Erin's personality quiz!!")




