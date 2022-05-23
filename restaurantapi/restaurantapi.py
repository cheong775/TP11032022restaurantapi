

from flask import Flask,render_template,request,make_response,jsonify
import json
from openapi3 import OpenAPI
import yaml




app=Flask(__name__)

clientBookList={"booktable":[{"userNomPrenom":"","userEmail":"","userTele":"","nombreP":"","bookDate":"","bookTemps":"" }]}
'''
def deveniryaml(clientBookList):
    apiyaml=clientBookList
    with open("apiClient.yaml","w") as f:
        yaml.safe_dump(data=apiyaml,stream=f)
deveniryaml(clientBookList)
'''
@app.route("/",methods=["GET","POST"])

def homeindex():
    infoBook={}
    tipreussi=""
    if request.method=="POST":
        if request.form.get("soumettre")=="Book Now":
            userN=request.form.get("userName")
            userE=request.form.get("userEmail")
            userT=request.form.get("userTele")
            userbd=request.form.get("bookDate")
            userbt=request.form.get("bookTemps")
            userq = request.form.get("nombrePer")
            infoBook={"userNomPrenom":userN,"userEmail":userE,"userTele":userT,"nombreP":userq,"bookDate":userbd,"bookTemps":userbt }
            clientBookList["booktable"].append(infoBook)
            with open('bookInfo.json', 'w', encoding='UTF-8') as f:
                json.dump(clientBookList,f, ensure_ascii = False)
            with open("apiClient.yaml", "w") as f:
                yaml.safe_dump(data=clientBookList, stream=f)
            tipreussi="vous avez réservé table avec réussi "
            print(clientBookList)
            print(tipreussi)
        else:
            pass




    return render_template("accueil.html",affichage="bienvenue à nôtre restaurant")


@app.route("/<userTelephone>",methods=["GET","POST"])
def resultaBook(userTelephone):
    with open('bookInfo.json', 'r', encoding='UTF-8') as f:
        jsona = json.load(f)
    for i in list(jsona.values()):
        for j in i:
            if(userTelephone in j):
                pass
    return render_template("accueil.html",affichage="bienvenu %s" % userTelephone,infoBook=j)



@app.route("/enquerir",methods=["GET"])
def enquerir():
    if request.method=="GET":
        usertele=request.args.get("usert")
        with open('bookInfo.json', 'r', encoding='UTF-8') as f:
            jsona = json.load(f)
        for i in list(jsona.values()):
            for j in i:
                if (usertele in j):
                    pass
                else:
                    j="vous n'avez pas pris réservation"
    return render_template("accueil.html", affichage="bienvenu %s" % usertele, infoBook=j)


@app.route("/bookContinue",methods=["PUT"])
def bookContinue():
    userN = request.args.get("userName")
    userE = request.args.get("userEmail")
    userT = request.args.get("userTele")
    userbd = request.args.get("bookDate")
    userbt = request.args.get("bookTemps")
    userq = request.args.get("nombrePer")
    infoBook = {"userNomPrenom": userN, "userEmail": userE, "userTele": userT, "nombreP": userq, "bookDate": userbd,
                "bookTemps": userbt}
    clientBookList["booktable"].append(infoBook)
    return render_template("accueil.html",affichage="réservé continue")

@app.route("/annueltable",methods=["DELETE"])
def annuelT():
    userta=request.form.get("telephone")
    with open('bookInfo.json', 'r', encoding='UTF-8') as f:
        jsona = json.load(f)
    for i in list(jsona.values()):
        for j in i:
            if (userta in j):
                clientBookList=list(jsona.values()).remove(i)
                with open('bookInfo.json', 'w', encoding='UTF-8') as f:
                    json.dump(clientBookList, f, ensure_ascii=False)
            else:
                j = "vous n'avez pas pris réservation"


@app.route("/allUsers")
def users_api():
    with open('bookInfo.json', 'r', encoding='UTF-8') as f:
        jsona = json.load(f)
    allUsers = []
    for i in list(jsona.values()):
        allUsers.append(i["userNomPrenom"])


    return allUsers



@app.route("/<utilisateur>",methods=["GET","POST"])
def pageUtilisateur(utilisateur):
    return render_template("accueil.html", affichage="bienvenue à restaurant %s" % utilisateur)


@app.route("/connecter",methods=["GET","POST"])
def pageConnecter():
    return render_template("accueil.html",affichage="bienvenue à connecter")

@app.route("/inscrit",methods=["GET","POST"])
def pageInscrit():
    if request.method=="POST":
        usercompte=request.form.get("nomCompte")
        userpass=request.form.get("motPass")
        print(usercompte,userpass)
    return render_template("accueil.html",affichage="bienvenue à inscription")

if __name__=='__main__':
    app.run(debug=True)