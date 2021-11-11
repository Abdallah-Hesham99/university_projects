#include<iostream>
#include<math.h>
#include<string.h>
using namespace std;
int main()
{ string std1; int X; string t; int epower; string et; string Lt; int y,z,shifting;
cout<<"Please enter the the trigonometric function to be transformed using Laplace trsnsform :"<<endl;
getline(cin,std1);

cout<<"Please enter the angle, press enter, then enter the variable t :"<<endl;

 cin>>X>>t;
 
 cout<<"if it's shifted, enter the value of the shifting, else enter zero :"<<endl;
 cin>>shifting;
 
 
 cout<<"if the function is multiplied by the unit step function, enter the value of alpha. else, enter zero"<<endl;
 cin>>y;
 cout<<endl;
 
  cout<<"if the function is multiplied by an exponential function, enter the power, press enter, then enter the variable t. if not, enter zero :"<<endl;
 cin>>epower;
 if (epower!=0)
 {cin>>et;
 }
 cout<<"if it's shifted, enter the value of the shifting, else enter zero :"<<endl;
 cin>>z;

y=-y;
if (y==shifting&&y==z)
{

 
 

 cout<<"Laplace transform for your function is :"<<endl;
if (y==0) 
{

 if (std1=="cos"||std1=="cosine"&&epower!=0)
 {cout<<"s"<<"/"<<"(s"<<-epower<<")^2"<<"+"<<pow(X,2)<<endl;}
 else if (std1=="cos"||std1=="cosine"&&epower==0)
 {cout<<"s"<<"/"<<"s"<<"^2"<<"+"<<pow(X,2)<<endl;}
 else if (std1=="sin"||std1=="sine"&&epower!=0)
 {cout<<X<<"/"<<"(s"<<-epower<<")^2"<<"+"<<pow(X,2)<<endl;
 }
 else {cout<<X<<"/"<<"s"<<"^2"<<"+"<<pow(X,2)<<endl;
 }}
 //for the unit step shifting 
 else if (y!=0)
 {if (std1=="cos"||std1=="cosine"&&epower!=0)
 {cout<<"e^("<<y<<"s)*s"<<"/"<<"(s"<<-epower<<")^2"<<"+"<<pow(X,2)<<endl;}
 else if (std1=="cos"||std1=="cosine"&&epower==0)
 {cout<<"e^("<<y<<"s)*s"<<"/"<<"s"<<"^2"<<"+"<<pow(X,2)<<endl;}
 else if (std1=="sin"||std1=="sine"&&epower!=0)
 {cout<<"e^("<<y<<"s)*"<<X<<"/"<<"(s"<<-epower<<")^2"<<"+"<<pow(X,2)<<endl;
 }
 else {cout<<"e^("<<y<<"s)*"<<X<<"/"<<"s"<<"^2"<<"+"<<pow(X,2)<<endl;
 }
  }
}
  else
  cout<<"error, the variable t must be shifted by the value of alpha ";

 
 }
 	
 

 

	
	
	
	
	
	
	
	
	
	
	

