#Librerias
from tkinter import *  
import tkinter.font
import random
#cAqui creo una ventana
root=Tk()
root.title("Clue Naruto")
root.geometry("1050x590")
root.resizable(0,0)
cg_font = tkinter.font.Font( family="Century Gothic", size=15, weight="bold" )
#Escenarios de Naruto
academia=PhotoImage(file="Academia.png")
aldeahoja=PhotoImage(file="AldeaHoja.png")
aldealluvia=PhotoImage(file="AldeaLluvia.png")
bosque=PhotoImage(file="Bosque.png")
entrenamiento=PhotoImage(file="Entrenamiento.png")
hokages=PhotoImage(file="Hokages.png")
#Personajes /Akatsuki
deidara=PhotoImage(file="DDeidara.png")
hidan=PhotoImage(file="DHidan.png")
itachi=PhotoImage(file="DItachi.png")
kakuzu=PhotoImage(file="DKakuzu.png")
kisame=PhotoImage(file="DKisame.png")
konan=PhotoImage(file="DKonan.png")
pain=PhotoImage(file="DPain.png")
sasori=PhotoImage(file="DSasori.png")
sasuke=PhotoImage(file="DSasuke.png")
tobi=PhotoImage(file="DTobi.png")
#Dialogo
BarraDialogo=PhotoImage(file="Dialogo.png")
#Listas de todos los datos
nombres=['Deidara','Hidan','Itachi','Kakuzu','Kisame','Konan','Pain','Sasori','Sasuke','Tobi']
imagenes=[deidara,hidan,itachi,kakuzu,kisame,konan,pain,sasori,sasuke,tobi]
lugar=['Aldea de la Hoja','Aldea de la lluvia +','Bosque','Entrenamiento','Hokages']
arma=['Kunai','Shuriken','Espada','Pergamino','Sellos Explosivos']
#Asesino aleatorio
a=random.randint(0,4)
asesino=[nombres[a],lugar[random.randint(0,4)],arma[random.randint(0,4)],imagenes[a]]
#Mapa
Mapa=[] 
Conclusion=[]
AccionesCount=0
for z in range(5):
    a=random.randint(0,(len(nombres)-1))
    Mapa.append([nombres[a],lugar[random.randint(0,len(lugar)-1)],arma[random.randint(0,len(arma)-1)],imagenes[a]])
    nombres.remove(Mapa[z][0])
    lugar.remove(Mapa[z][1])
    arma.remove(Mapa[z][2])
    imagenes.remove(Mapa[z][3])
#Canvas
canvas=Canvas(root,width=1000,height=590)
canvas.pack(fill="both",expand=True)
canvas.pack()
canvas.create_image(0,0,image=academia,anchor = "nw")
canvas.create_text(120,30,text="Lugar a investigar",fill="White",font=cg_font) 
canvas.create_text(140,60,text=f"Acciones restantes: {5-AccionesCount}", fill="White",font=cg_font) 
#Aldea de la Hoja
def cambia_aldeahoja():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=aldeahoja,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Aldea de la Hoja"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Aldea de la Lluvia
def cambia_aldealluvia():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=aldealluvia,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Aldea de la Lluvia"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Bosque
def cambia_bosque():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=bosque,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Bosque"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Entrenamiento
def cambia_entrenamiento():
    canvas.pack(fill="both",expand=True)
    canvas.pack()
    canvas.create_image(0,0,image=entrenamiento,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Entrenamiento"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Hokages
def cambia_hokages():
    canvas.pack(fill="both",expand=True) 
    canvas.pack()
    canvas.create_image(0,0,image=hokages,anchor="nw")
    ocultar_botones()
    global nombre_lugar
    nombre_lugar="Hokages"
    global zmapa
    zmapa=ubicar_mapa(nombre_lugar)
    destino(nombre_lugar)
#Botones ocultos
def ocultar_botones():
    boton_aldeahoja.place_forget()
    boton_aldealluvia.place_forget()
    boton_bosque.place_forget()
    boton_entrenamiento.place_forget()
    boton_hokages.place_forget()
    global EnLugar
    global DialogCount
    EnLugar=1
    DialogCount=0
#Botones  
def mostrar_botones():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_aldeahoja.place(x=200,y=100)
    boton_aldealluvia.place(x=700,y=300)
    boton_bosque.place(x=450,y=500)
    boton_entrenamiento.place(x=100,y=500)
    boton_hokages.place(x=600,y=100)
#Opciones
def mostrar_opciones():
    boton_uno.place(x=-500,y=-280)
    boton_dos.place(x=-500,y=-320)
    boton_tres.place(x=-500,y=-360)
    boton_cuatro.place(x=500,y=400)
    boton_cinco.place(x=500,y=440)
#Lugar final

def destino(lugar):
    texto=["Deidara\n\nOk, aqui es, llegamos a "+lugar+ "\nDebe haber alguna pista por aqui \ndel asesinato de Konan.",
           "Sasori\n\nCreo que estamos solos.\n*"+Mapa[zmapa][0]+" *aparece*",
           "Deidara\n\n¿qué haremos?"]
    Imagen_texto=[deidara,sasori,deidara]
    global dialogo
    global Imagen
    if DialogCount>0 and DialogCount<len(texto):  
        canvas.itemconfig(Imagen,image=Imagen_texto[DialogCount])
        canvas.itemconfig(dialogo,text=texto[DialogCount])
        if DialogCount==2:
            boton_investigar.place(x=300,y=250)
            boton_preguntar.place(x=500,y=250)    
    elif DialogCount>=len(texto):
        boton_siguiente.place_forget()
    else:
        Imagen=canvas.create_image(220,288,image=deidara,anchor="nw")
        dialogo=canvas.create_text(330,410,fill="Black",text=texto[DialogCount],anchor="nw",font=cg_font)
#Interrogar       
def interrogar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=845,y=540)
    global AccionesCount
    global DialogCount
    global EnLugar
    global num_dialogo 
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=4
    DialogCount=0
    boton_menu.place_forget()
    num_dialogo=random.randint(0,2) 
    conversacion()
#Ver lugar
def observar():
    boton_investigar.place_forget()
    boton_preguntar.place_forget()
    boton_siguiente.place(x=845,y=540)
    global AccionesCount
    global EnLugar
    global DialogCount
    global dialogo  
    global Imagen
    canvas.delete(Imagen)
    canvas.delete(dialogo)
    AccionesCount+=1
    EnLugar=2
    DialogCount=0
    boton_menu.place_forget()
    encontrarpista()
#Conversar
def conversacion():
    global dialogo
    global Imagen
    lugar_random=random.randint(0,4)
    nombre_random=random.randint(0,4)
    if Mapa[nombre_random][0]==Mapa[zmapa][0] or Mapa[nombre_random][0]==asesino[0]:  
        nombre_random=random.randint(0,4)
    if lugar_random==zmapa:
        lugar_random=random.randint(0,4)
    dialogo1=[f"Sasori \n\nHola. {Mapa[zmapa][0]}.",
             f"{Mapa[zmapa][0]} \n\n¿Qué hacen aquí?",
             f"Hidan \n\nKonan murió y queremos saber quien lo hizo \n¿Dónde has estado hoy?",
             f"{Mapa[zmapa][0]} \n\nEstaba en {Mapa[lugar_random][1]}, creo que   \nvi a {Mapa[nombre_random][0]} en ese lugar.\nPregúntenle a el.",
             f"Sasori \n\nHmmm,vamos a ver, no perdemos nada, {Mapa[zmapa][0]}",
             f"{Mapa[zmapa][0]} \n\nNo vuelvan a buscarme."]
    image=[sasori,Mapa[zmapa][3],hidan,Mapa[zmapa][3],sasori,Mapa[zmapa][3]]
   
    dialogos=[[f"{Mapa[zmapa][0]} \n\n¿Donde está Konan?",
                 "Itachi \n\nMuerta.\n¿Donde has estado?",
                 f"{Mapa[zmapa][0]} \n\nPain estará destrozado. encuentren al maldito. \nestuve en el entrenamiento practicando \ngenjutsu.",
                 "Itachi \n\nNo creo, Konan solo va al entrenamiento de \nla academia",
                 "Deidara \n\nDéjanos en paz, creí que serías tú.",
                 f"{Mapa[zmapa][0]} \n\nNo molestes,escoria."],
            [f"Deidara \n\n¡¿Que rayos?! {Mapa[zmapa][0]}? \nven aquí ahora.",
                 f"{Mapa[zmapa][0]} \n\n¿y Konan?",
                 f"sasori \n\nEstá muerta. O descubrimos quien \nla mató o estamos muertos.¿Dónde has estado?",
                 f"{Mapa[zmapa][0]} \n\nEn una misión para capturar a un jinchuriki.\nOrdenes de arriba.",
                 "Sasori \n\nNo mientas,esa mision la teniamos nosotros \nNo estabas ahí",
                 f"{Mapa[zmapa][0]} \n\nHablen con el si es que pueden,\nno es mi problema\nEncuentren quien la mató o nos matan."],
            [f"{Mapa[zmapa][0]} \n\n¿Que quieren?",
                 f"Hidan \n\nHola! {Mapa[zmapa][0]}, buscamos al maldito que mató \na Konan,\n ¿dónde has estado?",
                 f"{Mapa[zmapa][0]} \n\nNo recuerdo ni mi desayuno de esta mañana.",
                 f"{Mapa[zmapa][0]} \n\nEstaba con {Mapa[nombre_random][0]} en la aldea de la hoja, \ny despues fuí a vigilar al bosque",
                 f"Sasori \n\nYa que, desaparécete. {Mapa[zmapa][0]}"]]
    image2 =[[Mapa[zmapa][3],itachi,Mapa[zmapa][3],itachi,deidara,Mapa[zmapa][3]],[deidara,Mapa[zmapa][3],sasori,Mapa[zmapa][3],sasori,Mapa[zmapa][3]],[Mapa[zmapa][3],hidan,Mapa[zmapa][3],Mapa[zmapa][3],sasori]]
    if asesino[0]==Mapa[zmapa][0]:
        if DialogCount>0 and DialogCount<len(dialogo1): 
            canvas.itemconfig(Imagen,image=image[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):  
            volver_menu()
        else:             
            Imagen=canvas.create_image(220,288,image=image[DialogCount],anchor="nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=dialogo1[DialogCount],anchor="nw",font=cg_font)
    else:  
        if DialogCount>0 and DialogCount<len(dialogos[num_dialogo]):  
            canvas.itemconfig(Imagen,image=image2[num_dialogo][DialogCount])
            canvas.itemconfig(dialogo,text=dialogos[num_dialogo][DialogCount])
        elif DialogCount>=len(dialogos[num_dialogo]): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(220,288,image=image2[num_dialogo][DialogCount],anchor = "nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=dialogos[num_dialogo][DialogCount],anchor="nw",font=cg_font)
#encontrar objeto importante
def encontrarcapa():  
    global dialogo
    global Imagen
    dialogo1=["Itachi \n\nEncontre la bata de Konan. \nla asesinaron aquí, hay sangre.",  
            "Hidan \n\n Idiotas",
             "Itachi \n\nPain se enterará tarde o temprano.",
             "Deidara \n\nLo encontraremos"]
    ImgTex1=[itachi,hidan,itachi,deidara]
    
    dialogo2=["Sasori \n\nHmmm, que raro, no creo \nque Konan esté aquí", 
             "Deidara \n\n Creo lo mismo",
             "Itachi \n\nNo puedo creer que esté muerta."]
    ImgTex2=[sasori,deidara,itachi]
    
    if asesino[1]==Mapa[zmapa][1]: 
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            volver_menu()
        else:            
            Imagen=canvas.create_image(220,288,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=dialogo1[DialogCount],anchor="nw",font=cg_font)
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image=ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            volver_menu()
        else:            
            Imagen=canvas.create_image(220,288,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=dialogo2[DialogCount],anchor="nw",font=cg_font)
#Pista encontrada
def encontrarpista():
    global dialogo
    global EnLugar
    global DialogCount
    global Imagen
    dialogo1=["Deidara \n\nPodemos dividirnos y encontrar más cosas.",
             "Sasori \n\nVengan a ver esto...",
             "Sasori \n\nEncontré  "+asesino[2]+", \nno tengo idea de a quien le pertenece.",
             "Hidan \n\nTenemos nuestra pieza final."]
    ImgTex1=[deidara,sasori,sasori,hidan]
    
    dialogo2=["Deidara \n\nPodemos divirdirnos y encontrar más cosas.",
             "...",
             "Itachi \n\nDudo mucho que aquí la hayan matado",
             "Sasori \n\nNo hay de otra a seguir buscando antes \nde que el nos encuentre."]
    ImgTex2=[deidara,BarraDialogo,itachi,sasori]
    
    if asesino[2]==Mapa[zmapa][2]:
        if DialogCount>0 and DialogCount<len(dialogo1):  
            canvas.itemconfig(Imagen,image=ImgTex1[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo1[DialogCount])
        elif DialogCount>=len(dialogo1):
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarcapa()
        else:             
            Imagen=canvas.create_image(220,288,image=ImgTex1[DialogCount],anchor="nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=dialogo1[DialogCount],anchor="nw",font=cg_font)
    else:  
        if DialogCount>0 and DialogCount<len(dialogo2): 
            canvas.itemconfig(Imagen,image =ImgTex2[DialogCount])
            canvas.itemconfig(dialogo,text=dialogo2[DialogCount])
        elif DialogCount>=len(dialogo2): 
            DialogCount=0
            EnLugar=3
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            encontrarcapa()
        else:             
            Imagen=canvas.create_image(220,288,image=ImgTex2[DialogCount],anchor="nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=dialogo2[DialogCount],anchor="nw",font=cg_font)
#Mapa
def ubicar_mapa(lugar): 
    for i in range(5):
        if lugar==Mapa[i][1]:
            return i       
#Return menu
def volver_menu():
    global dialogo
    global DialogCount
    global EnLugar
    EnLugar=0
    if AccionesCount==5:
        canvas.delete(dialogo)
        DialogCount=0
        EnLugar=5
        resolvermisterio()
    else:
        canvas.pack(fill="both",expand=True) 
        canvas.pack() 
        canvas.create_image(0,0,image=academia,anchor="nw") 
        mostrar_botones()
        boton_menu.place(x=945,y=540)
        canvas.create_text(120,30,text="Investigar en: ",fill="White",font=("Century Ghotic",15)) 
        canvas.create_text(140,60,text=f"Lo que falta: : {5-AccionesCount}",fill="White",font=("Century Ghotic",26)) 
#Dialogo sigue
def siguiente():
    global DialogCount
    global AnswerBien
    DialogCount+=1
    if EnLugar==1:
        destino(nombre_lugar)
    elif EnLugar==2: 
        encontrarpista()
    elif EnLugar==3: 
        encontrarcapa()
    elif EnLugar==4: 
        conversacion()
    elif EnLugar==5: 
        if DialogCount==1: 
            boton_siguiente.place_forget()
            mostrar_opciones()
        resolvermisterio()
    elif EnLugar==6: 
        Final(AnswerBien)
    elif EnLugar==7:
        root.destroy()
#Punto crítico
def resolvermisterio():
    global dialogo
    global DialogCount
    global ans
    global AnswerBien
    global EnLugar
    global Imagen
    
    DialogFinal=["Deidara \n\nGenial encontramos antes que \na Pain quien mató a Konan",
                "Deidara \n\n¿Quién es el asesino?",
                "Deidara \n\n¿Dónde mataron a Konan?",
                "Deidara \n\nArma utilizada"]
    if DialogCount>0 and DialogCount<len(DialogFinal):
        canvas.itemconfig(dialogo,text=DialogFinal[DialogCount])
        boton_uno.configure(text=Mapa[0][DialogCount-1])
        boton_dos.configure(text=Mapa[1][DialogCount-1])
        boton_tres.configure(text=Mapa[2][DialogCount-1])
        boton_cuatro.configure(text=Mapa[3][DialogCount-1])
        boton_cinco.configure(text=Mapa[4][DialogCount-1])
    elif DialogCount>=len(DialogFinal): 
        DialogCount=0
        EnLugar=6
        canvas.delete(dialogo)
        canvas.delete(Imagen)
        ans=0
        for a in 'Kunai','Shuriken','Espada','Pergamino','Sellos Explosivos':
            if asesino[2]==a:
                break
            ans+=1
        AnswerBien=True
        for i in range(3):
            if asesino[i]!=Conclusion[i]:
                AnswerBien=False
        boton_uno.place_forget()
        boton_dos.place_forget()
        boton_tres.place_forget()
        boton_cuatro.place_forget()
        boton_cinco.place_forget()
        boton_siguiente.place(x=845,y=540) 
        Final(AnswerBien)
    else:             
        canvas.create_image(0,0,image=academia,anchor="nw")
        Imagen=canvas.create_image(220,288,image=deidara,anchor="nw")
        dialogo=canvas.create_text(330,410,fill="Black",text=DialogFinal[DialogCount],anchor="nw",font=cg_font)
#Resultado
def resultado(respuesta):
    global DialogCount
    global Conclusion
    Conclusion.append(respuesta)
    DialogCount+=1  
    resolvermisterio()
#Dialogo final
def Final(r):
    global ans
    global DialogCount
    global dialogo
    global Imagen, EnLugar
    if r==True: 
        objetivos=[f"la {asesino[2]} ¿Pista? \nel Kunai es de Kazuzu \nmaldito aváro.",
                  f"el {asesino[2]} ¿Pista? \nel Shuriken le pertenece a Kisame \nidiota.",
                  f"la {asesino[2]} ¿Pista? \nLa Espada le pertenece a Sasuke \notro Uchiha.",
                  f"el {asesino[2]} ¿Pista? \nPergamino\n es de la habilidad de Tobi \nSorprendentemente sigue vivo.",
                  f"la {asesino[2]} ¿Pista? \nBueno, la Sellos Explosivos es de Pain \nY eso que estaba enamorado de Konan..."]
        
        Dialogo_Final=["Sasori \n\nQuien mató a Konan.\nFue..",
                     f"Itachi \n\n{asesino[0]} ....",
                     f"Sasori \n\n{asesino[0]} es el asesino. No lo creo...",
                     "Hidan \n\nNo tiene sentido,¡todos somos camaradas!",
                     "Deidara \n\nAl menos ya podemos descansar por hoy..",
                     "Itachi \n\n¿Porqué la mataste?",
                     f"Sasori \n\nPor {objetivos[ans]}",
                      "Itachi \n ¿Y el cuerpo?",
                      f"{asesino[0]} \n\nEncuentren lo que queda de ella",
                      "Konan \n\n¿Hey idiotas que hacen?",
                      "Deidara \n\n!!!",
                      f"Konan \n\n {asesino[0]} me pidió unas flores para una misión ",
                      "Itachi \n\nHasta sospechamos de Pain",
                      "Konan \n\nEl no me haría daño, solo mataron el tiempo en vez de buscar al resto de los jinchurikis",
                      "Deidara \n\nNo te mentiré, si me preocupé por tí.",
                       f"{asesino[0]} \n\nNo puedo creer ue se la creyeron, idiotas.",
                      "Konan \n\nNo pierdan el tiempo y vamos por el 9 colas."]
        ImgFinal=[sasori,itachi,sasori,hidan,deidara,itachi,sasori,itachi,asesino[3],
                 konan,deidara,konan,itachi,konan,deidara,asesino[3],konan]
        
        if DialogCount>0 and DialogCount<len(Dialogo_Final):  
            canvas.itemconfig(Imagen,image=ImgFinal[DialogCount])
            canvas.itemconfig(dialogo,text=Dialogo_Final[DialogCount])
        elif DialogCount>=len(Dialogo_Final): 
            DialogCount=0
            EnLugar=0
            canvas.delete(dialogo)
            canvas.delete(Imagen)
            boton_siguiente.place_forget()
            root.destroy()
        else:            
            Imagen=canvas.create_image(220,288,image=ImgFinal[DialogCount],anchor="nw")
            dialogo=canvas.create_text(330,410,fill="Black",text=Dialogo_Final[DialogCount],anchor="nw",font=cg_font)
    else:
        Imagen=canvas.create_image(220,288,image=deidara,anchor="nw")
        dialogo=canvas.create_text(330,410,fill="Black",text=f"Deidara \n\nPuedes hacerlo mejor.\nCulpable:{asesino[0]}\nLugar:{asesino[1]}\narma:{asesino[2]}",anchor="nw",font=cg_font) 
        EnLugar=7
#boton aldeahoja
boton_aldeahoja=Button(canvas,text="aldea de la hoja",width=12,command=cambia_aldeahoja)  
boton_aldeahoja.place(x=200,y=100)
#boton Aldea de la Lluvia
boton_aldealluvia=Button(canvas,text="aldea de la lluvia",width=12,command=cambia_aldealluvia)
boton_aldealluvia.place(x=700,y=300)
#boton bosque
boton_bosque=Button(canvas,text="Bosque",width=12,command=cambia_bosque)
boton_bosque.place(x=450,y=500)
#boton entrenamiento
boton_entrenamiento=Button(canvas,text="Entrenamiento",width=12,command=cambia_entrenamiento)
boton_entrenamiento.place(x=100,y=500)
#boton hokages
boton_hokages=Button(canvas,text=" Monumento",width=12,command=cambia_hokages)
boton_hokages.place(x=600,y=100)
#boton menu
boton_menu=Button(canvas,text="Menú",width=12,command=volver_menu)
boton_menu.place(x=945,y=540)
#botn siguiente
boton_siguiente=Button(canvas, text="Siguiente", width=12, command=siguiente)
boton_siguiente.place(x=845,y=540)
#boton para checar lugares
boton_preguntar=Button(canvas,text="Interrogar",width="20",command=interrogar,font=("Century Ghotic",12))
boton_investigar=Button(canvas,text="Ver lugar",width="20",command=observar,font=("Century Ghotic",12))
#botones para las respuestas del asesinato
boton_uno=Button(canvas,text="",width="28",command= lambda:resultado(Mapa[0][DialogCount-1]),font=("Century Ghotic",12))
boton_dos=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[1][DialogCount-1]),font=("Century Ghotic",12))
boton_tres=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[2][DialogCount-1]),font=("Century Ghotic",12))
boton_cuatro=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[3][DialogCount-1]),font=("Century Ghotic",12))
boton_cinco=Button(canvas,text="",width="28",command=lambda:resultado(Mapa[4][DialogCount-1]),font=("Century Ghotic",12))
root.mainloop() 