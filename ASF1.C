#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
int i=0,j=0,x=0,y=0,p=1;
main()
{
int gd = DETECT,gm;
initgraph(&gd,&gm,"d:\software\turbo\include\graphics.h");
while(!kbhit())
{
i++;
if(i>=275)
goto first;
fillellipse(155,290-i,10,6);          /*flag tie*/
fillellipse(155,290-i,6,10);
setcolor(RED);
line(155,290-i,165,288-i);
line(155,290-i,145,292-i);
line(155,290-i,155,281-i);
line(155,290-i,158,296-i);
setcolor(RED);
line(165,290,155,290-i);
line(164,290,154,290-i);
setcolor(YELLOW);
circle(148.5,5,5);
line(150,10,150,375);
line(147,10,147,375);
setcolor(WHITE);
rectangle(125,375,175,400);
rectangle(80,400,220,425);
circle(200,280,8);        				 /* HEAD */
fillellipse(197,278,2,1.5);                              /* eye  */
fillellipse(203,278,2,1.5);				 /* EYE  */
fillellipse(200,283,4,1);				 /* LIP */
line(200,288,190,300);
line(200,288,210,300);
line(190,300,160,290);
line(210,300,200,310);
line(200,310,160,290);
line(210,300,210,340);
line(190,300,190,340);
line(210,340,190,340);
line(210,335,190,335);
line(210,340,210,400);
line(190,340,190,400);
line(190,400,200,340);
line(210,400,200,340);
delay(20000);
cleardevice();
}

first:
{
  cleardevice();
  while(!kbhit())
  {
  j++;
  if(j>=340)
  {
  j=320;
  goto second;
  }
  setcolor(YELLOW);
  circle(148.5,5,5);
  line(150,10,150,375);
  line(147,10,147,375);
  setfillstyle(SOLID_FILL,RED);
  bar(150,10,300,40);
  setfillstyle(SOLID_FILL,WHITE);
  bar(150,40,300,70);
  setfillstyle(SOLID_FILL,GREEN);
  bar(150,70,300,100);
  setfillstyle(EMPTY_FILL,GREEN);
  setcolor(BLUE);
  circle(230,55,15);
  for(i=0;i<=345;i+=15)   			/* ashoka chakra */
  {
   x=i;
   setcolor(BLUE);
   pieslice(230,55,x,y,15);
   y=x;
  }
   pieslice(230,55,345,360,15);
   setcolor(WHITE);
   rectangle(125,375,175,400);
   rectangle(100,400,200,425);
   setcolor(RED);
   line(165,290,150,90);
   line(164,290,149,90);
   setcolor(WHITE);
   rectangle(125,375,175,400);
   rectangle(80,400,220,425);
   circle(200,280,8);
   fillellipse(197,278,2,1.5);
   fillellipse(203,278,2,1.5);
   fillellipse(200,283,4,1);
   line(200,288,190,300);
   line(200,288,210,300);
   line(190,300,160,290);
   line(210,300,200,310);
   line(200,310,160,290);
   line(210,300,210,340);
   line(190,300,190,340);
   line(210,340,190,340);
   line(210,335,190,335);
   line(210,340,210,400);
   line(190,340,190,400);
   line(190,400,200,340);
   line(210,400,200,340);
   /* FLOWER */
   setcolor(WHITE);
   settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
   outtextxy(120,10+j,"   * *");
   setcolor(RED);
   settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
   outtextxy(135,30+j,"  * * *");
   setcolor(46);
   settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
   outtextxy(130,50+j," * * * *");
   setcolor(189);
   settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
   outtextxy(135,80+j,"* * * * *");
   delay(20000);
   cleardevice();
  }
  }
second:
    {
    cleardevice();
    while(!kbhit())
    {
	  setcolor(YELLOW);
	  circle(148.5,5,5);
	  line(150,10,150,375);
	  line(147,10,147,375);
	  setfillstyle(SOLID_FILL,RED);
	  bar(150,10,300,40);
	  setfillstyle(SOLID_FILL,WHITE);
	  bar(150,40,300,70);
	  setfillstyle(SOLID_FILL,GREEN);
	  bar(150,70,300,100);
	  setfillstyle(EMPTY_FILL,GREEN);
	  setcolor(BLUE);
	  circle(230,55,15);
	  for(i=0;i<=345;i+=15)   			/* ashoka chakra */
	  {
	   x=i;
	   setcolor(BLUE);
	   pieslice(230,55,x,y,15);
	   y=x;
	  }
	   pieslice(230,55,345,360,15);
	   setcolor(WHITE);
	   rectangle(125,375,175,400);
	   rectangle(100,400,200,425);
	   setcolor(RED);
	   line(165,290,150,90);
	   line(164,290,149,90);
	   setcolor(WHITE);
	   rectangle(125,375,175,400);
	   rectangle(80,400,220,425);
	   circle(200,280,8);
	   fillellipse(197,278,2,1.5);
	   fillellipse(203,278,2,1.5);
	   fillellipse(200,283,4,1);
	   line(200,288,190,300);
	   line(200,288,210,300);
	   line(190,300,160,290);
	   line(210,300,200,310);
	   line(200,310,160,290);
	   line(210,300,210,340);
	   line(190,300,190,340);
	   line(210,340,190,340);
	   line(210,335,190,335);
	   line(210,340,210,400);
	   line(190,340,190,400);
	   line(190,400,200,340);
	   line(210,400,200,340);
	   /* FLOWER */
	   setcolor(WHITE);
	   settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
	   outtextxy(85,390," *  *  * ");
	   setcolor(RED);
	   settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
	   outtextxy(135,400,"*  *  *");
	   setcolor(YELLOW);
	   settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
	   outtextxy(75,360,"*  *  *  *");
	   setcolor(978);
	   settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
	   outtextxy(100,430,"*    *   *");
	   setcolor(189);
	   settextstyle(GOTHIC_FONT,HORIZ_DIR,5);
	   outtextxy(105,370,"* * *");
	   setcolor(45);
	   settextstyle(SANS_SERIF_FONT,HORIZ_DIR,5);
	   outtextxy(135,420,"*  *");
	   setcolor(450);
	   settextstyle(TRIPLEX_FONT,HORIZ_DIR,5);
	   outtextxy(110,400,"*");
	   setcolor(89);
	   settextstyle(GOTHIC_FONT,HORIZ_DIR,5);
	   outtextxy(100,390," * * ");
	   setbkcolor(BLACK);
	   settextstyle(GOTHIC_FONT,HORIZ_DIR,4);
	   outtextxy(300,200,"VANDE MADHARAM ");
	   setbkcolor(BLACK);
	   settextstyle(GOTHIC_FONT,HORIZ_DIR,4);
	   outtextxy(300,250,"  JAIHIND  ");
	   settextstyle(TRIPLEX_FONT,HORIZ_DIR,4);
	   outtextxy(100,300,"  Created by K.Gowthaman  ");
	   delay(30000);
	   cleardevice();
  }
 }
   getch();

}
