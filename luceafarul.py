import pygame
import time
from pygame import mixer
score=0
pygame.init()
pygame.font.init()
mixer.init()
music_path=r"C:\\Users\\user\\Desktop\\Autumn-Scene(chosic.com).mp3"
mixer.music.load(music_path)
mixer.music.play(-1)
icon=pygame.image.load(r"C:\\Users\\user\\Desktop\\luceafarul.ico")
font_question=pygame.font.Font("freesansbold.ttf",25)
font_variant=pygame.font.Font("freesansbold.ttf",18)
font_big=pygame.font.Font("freesansbold.ttf",30)
black=(0,0,0)
yellow=(50,200,0)
blue=(0,0,255)
red=(255,0,0)
background_color=(255,255,255) #white
window=pygame.display.set_mode()
window.fill(background_color)
pygame.display.set_caption("Luceafarul - unealta de bac")
pygame.display.set_icon(icon)
width=window.get_size()[0]
height=window.get_size()[1]
def question(text,lis,selector):
    window.fill(background_color)
    pygame.draw.rect(window,black,[selector[0]-405,selector[1]-20,1200,40],2)
    question_text=font_question.render(text,True,black,background_color)
    rect=question_text.get_rect()
    rect.center=(width//2,200)
    A=lis[0]
    B=lis[1]
    C=lis[2]
    D=lis[3]
    corect=lis[4]
    textA=font_variant.render(A,True,black,background_color)
    textB=font_variant.render(B,True,black,background_color)
    textC=font_variant.render(C,True,black,background_color)
    textD=font_variant.render(D,True,black,background_color)
    rectA=textA.get_rect()
    rectB=textB.get_rect()
    rectC=textC.get_rect()
    rectD=textD.get_rect()
    rectA.center=(410,310)
    rectB.center=(410,410)
    rectC.center=(410,510)
    rectD.center=(410,610)
    window.blit(question_text,rect)
    window.blit(textA,rectA)
    window.blit(textB,rectB)
    window.blit(textC,rectC)
    window.blit(textD,rectD)
    if corect==A:
        return [410,310]
    elif corect==B:
        return [410,410]
    elif corect==C:
        return [410,510]
    else:
        return [410,610]
#question1-A1
question1='1.Din ce basm romanesc este inspirat poemul "Luceafarul :"'
A1="A.Fata in gradina de aur"
B1="B.Baiatul care vorbea cu florile"
C1="C.Balaurul cel cu 7 capete"
D1="D.Broasca Testoasa cea fermecata"
corect1=A1
#question2-C2
question2="2.Austriacul care a cules basmul se numeste:"
A2="A.Heinrich Jasomirgott"
B2="B.Friedrich der Katholische"
C2="C.Richard Kunisch"
D2="D.Jacob Paul Maximilian"
corect2=C2
#question3-A3
question3='3.Cum se numeste poemul prin care Eminescu valorifica basmul "Fata in gradina de aur" :'
A3="A.Fata in gradina de aur"
B3="B.Luceafarul"
C3="C.Soarele, vantul si gerul"
D3="D.Fluierul"
corect3=A3
#question4-D4
question4="4.Tema Luceafarului este :"
A4="A.Frica de Moarte"
B4="B.Tristetea autorului in fata adevarului universal"
C4="C.Singuratatea si durerea de fi neinteles"
D4="D.Romantica:problematica geniului in raport cu lumea,iubirea si cunoasterea"
corect4=D4
#question5-B5
question5='5."Luceafarul" a fost publicat in:'
A5="A.aprilie 1885 în Almanahul societății studențești România Jună din Bucuresti"
B5="B.aprilie 1883 în Almanahul societății studențești România Jună din Viena"
C5="C.ianuarie 1883 în Almanahul societății studențești România Bună din Velenta"
D5="D.aprilie 1883 în Almanahul societății studențești România Jună din Militari, Bucuresti"
corect5=B5
#question6
question6="6.Entitatile din Luceafarul sunt:"
A6="A.Hyperion,Catalin,Catalina,Demiurgul"
B6="B.Hyperion,Aurelia,Aurel,Demiurgul"
C6="C.Hyperion,Florina,Florin,Demiurgul"
D6="D.Zmeul,Catalin,Mina,Demiurgul"
corect6=A6
#question7
question7='7.Titlul operei denumeste:'
A7="A.Luna"
B7="B.Planeta marte"
C7="C.Soarele in timp de eclipsa"
D7="D.Planeta Venus,cel mai stralucitor corp ceresc observat de pe pamant noaptea."
corect7=D7
#question8
question8='8.Tablourile poemulul "Luceafarul" se desfasoara pe:'
A8="A.Planul terestru"
B8="B.Planul Celest"
C8="C.Sub pamant si in ceruri"
D8="D.Atat pe planul terestru cat si pe cel celest"
corect8=D8
#question9
question9="9.Romantismul este :"
A9="A.Un reprezentant al fanteziei,al libertatii de expresie,al cultului naturii si al lirismului"
B9="B.Un reprezentant al regulilor bine definite si al formalizarii in literatura"
C9="C.Un sinonim pentru clasicism"
D9="D.O stare de spirit"
corect9=A9
#question10
question10='10."Luceafarul" se incadreaza in curentul:'
A10="A.Realism"
B10="B.Clasicism"
C10="C.Romantism"
D10="D.Electric"
corect10=C10
questions={question1:[A1,B1,C1,D1,corect1],question2:[A2,B2,C2,D2,corect2],question3:[A3,B3,C3,D3,corect3],question4:[A4,B4,C4,D4,corect4],question5:[A5,B5,C5,D5,corect5],question6:[A6,B6,C6,D6,corect6],question7:[A7,B7,C7,D7,corect7],question8:[A8,B8,C8,D8,corect8],question9:[A9,B9,C9,D9,corect9],question10:[A10,B10,C10,D10,corect10]}
questions_keys=questions.keys()
questions_keys=list(questions_keys)
question_index=0
running=True
selector_index=0
selectors=[[410,310],[410,410],[410,510],[410,610]]
while running:
    selector=selectors[selector_index]
    q=question(questions_keys[question_index],questions[questions_keys[question_index]],selector)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.quit:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if selector_index!=3:
                    selector_index+=1
            elif event.key==pygame.K_UP:
                if selector_index!=0:
                    selector_index-=1
            elif event.key==pygame.K_RETURN:
                window.fill(background_color)
                if selector==q:
                    score+=1
                    text=font_big.render("Corect!",True,black,blue)
                    text_rect=text.get_rect()
                    text_rect.center=(width//2,height//2)
                    window.blit(text,text_rect)
                else:
                    text=font_big.render("Incorect!",True,black,red)
                    text_rect=text.get_rect()
                    text_rect.center=(width//2,height//2)
                    window.blit(text,text_rect)
                pygame.display.flip()
                time.sleep(0.8)
                question_index+=1
                selector_index=0
                if question_index==10:
                    running=False
                    window.fill(background_color)
                    score=font_big.render(f"Raspunsuri corecte:{score}",True,black,yellow)
                    score_rect=score.get_rect()
                    score_rect.center=(width//2,height//2)
                    window.blit(score,score_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    window.fill(background_color)
                    barem=font_big.render("Barem:",True,black,yellow)
                    barem_rect=barem.get_rect()
                    barem_rect.center=(width//2,height//2)
                    window.blit(barem,barem_rect)
                    pygame.display.flip()
                    time.sleep(3)
                    for i in range(10):
                        window.fill(background_color)
                        question=font_question.render(questions_keys[i],True,black)
                        question_rect=question.get_rect()
                        question_rect.center=(width//2,height//2)
                        window.blit(question,question_rect)
                        answer=font_variant.render(questions[questions_keys[i]][4],True,black)
                        answer_rect=answer.get_rect()
                        answer_rect.center=(410,height//2+100)
                        window.blit(answer,answer_rect)
                        pygame.display.flip()
                        time.sleep(4)
                    window.fill(background_color)
                    dev=font_big.render("Contact me: kingambitrap@gmail.com",True,red,black)
                    dev_rect=dev.get_rect()
                    dev_rect.center=(width//2,height//2)
                    window.blit(dev,dev_rect)
                    pygame.display.flip()
                    time.sleep(5)




