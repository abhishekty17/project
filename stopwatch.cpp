#include<iostream>
#include<conio.h>
#include<windows.h>
using namespace std;
void displayTime(int hours, int minutes, int seconds) 
{
    

   system("cls");

   cout << hours << ":"
        << minutes << ":"
        << seconds << endl;
}
int main() 
{
  cout<<"Stop watch"<<endl;
  cout<<"HH:MM:SS"<<endl;
  int hour = 0;
  int min = 0;
  int sec = 0;
  cout<<"press any key to start"<<endl;
  getch();
  displayTime(hour, min, sec);
   while(!kbhit()) 
  {
    Sleep(1000);

    sec++;

    if(sec > 59) {
      min++;
      sec = 0;
    } 

    if(min > 59) {
      hour++;
      min = 0;
    }

    displayTime(hour, min, sec);
  }
  return 0;
}