from erreurs import ErreurMaxAge,ErreurSexe,ErreurMinAge

if __name__=='__main__':
    numberMax=35
    numberMin=18
    while True:
        try:
            i_num = int(input("Entrez un age : "))
            i_sexe=input ("Entrez un sexe M ou F \n")
            if i_num< numberMin :
                 raise ErreurMinAge
            elif i_num > numberMax:
                 raise ErreurMaxAge
            elif (i_sexe !="M" ) or (i_sexe !="m" ) or (i_sexe !="F") or (i_sexe !="f"):
                raise ErreurSexe
            break
        except ErreurMinAge:
             print("vous etes trop jeune")
        except ErreurMaxAge:
            print("vous etes trop vieux")
        except ErreurSexe:
            print("merci de bien  saisir un sexe: F ou M\n")



print("félicitation! vous avez bien rempli le formulaire")