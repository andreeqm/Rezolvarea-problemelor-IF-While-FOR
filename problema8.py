a=eval(input("Introduceti lungimea primei laturi a="))
b=eval(input("Introduceti lungimea a laturi a doua b="))
c=eval(input("Introduceti lungimea a laturii a treia c="))
if((a>0)and(b>0)and(c>0)) :
    if((a<b+c)and(b<a+c)and(c<b+a)) :
        print("Exista")
        if((a==b)and(b==c)and(a==c)) :
            print("triungiul este echilateral")
        if((a!=b)and(b!=c)and(c!=a)) :
            print("triunghiul este scalen")
        if(((a!=b)or(b!=c)or(c!=a))and((a==b)or(b==c)or(a==c))) :
            print("triunghil este isoscel")
    else:
        print("nu exista")