from bs4 import BeautifulSoup
import urllib2

url="http://fiikus.net/?pokedex"
webpage = urllib2.urlopen(url)
soup = BeautifulSoup(webpage)
list=[]
for anchor in soup.find_all('a'):
    try:
        k=str(anchor.string)
        if k[0]=="#":
            L=str(anchor.string).split(" ")[1:]
            list.append((" ".join(L)).lower())
    except:pass
  
print """#include<iostream>
#include<cstdio>
#include<string>

using namespace std;
"""
a=r'printf("\n");'
for I in list:
    f=open(I,"r").read()
    i=I.replace('"','').replace('(','').replace(')','').replace(' ','').replace("'",'').replace(".",'')
    print "void",i,"(){"
    for line in f.split("\n"):
        if line:
            print 'printf("',line.replace("\\","\\\\").replace('"',r'\"').replace("(",r"\(").replace(")",r"\(").replace("'",r"\'"),'");',a
    print "}"

print """void print(string s){"""
for I in list:
    i=I.replace('"','').replace('(','').replace(".",'').replace(')','').replace(' ','').replace("'",'')
    print "if (s=="+'"'+i+'"){',i+"();","""return;}"""
print """ cout<<"No suck pokemon"<<endl;"""
print "}"

print """int main(int argc, char* argv[]){
if(argc<1)
{
printf("No pokemon entered");
}
string s=argv[1];
print(s);
"""


print """return (0);
}"""

