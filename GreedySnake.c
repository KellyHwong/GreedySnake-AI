#include<stdio.h>
//#include<windows.h>
#include<stdlib.h>
#include<time.h> 
//#include<conio.h>
#define up 119
#define down 115
#define left 97
#define right 100//�������ҷֱ���wsad������

void play();
char replay();
//�Գ�������̨���ڵĳ�����80(��Χ0~79)
//���ľ������,�Զ���Ϊ40(0~39),�պ����ڵ�����Ļ������
void dot(int x,int y,char z);
void draw();
void change();
void move();

void die();
int life=1;

void border();//���߽�
int bdx=0;
int bdy=0;
char bdc='0';

int speed=100;//��Ϸ�ٶ����ã�speedָ���ʱ�䣬�������������ߵ��ٶ�

int randomx();int randomy();
void food();//����ʳ��
int foodx;int foody;char foodc=38;
void eat();

int length=6;//��һ��ʼ��6�ڣ����һ����a[length-1]��b[length-1]
int a[100]={6,5,4,3,2,1},b[100]={1,1,1,1,1,1};//�ߵĳ��Ȳ�Ҫ����100= =
char c[100]={64,35,35,35,35,35};//��������ܸ���
int directx=1,directy=0;//����ҲҪ��ʼ�����ߵ��ƶ���directx��directy���У���غ������̲���

int tempx,tempy;char space=' ';
char key;
char rp='y';//rp����replay����д��������־�Ƿ�����

void main()
{
  while(rp=='y') //��ѭ��Ϊ���������
   {
	border();//�߽�ĳ�ʼ��
	draw();//�����ߣ����г�ʼ��
    food();//ʳ��ĳ�ʼ��
    play();//����Ϸ���̴���ɺ���,���������play������
	rp=replay();
   }
}
void play()//play������һ��ѭ��
{
        while(life!=0)//���ѭ������������Ϸlife==0��Ϸ����
        {
	            
		  if(!kbhit())//��û�а�����ʱ��
          {
	       tempx=a[length-1];tempy=b[length-1];
	       change();//��������ֵ
	       die();//�ж�����
		   eat();//�ж��߳�û��ʳ��
		   if(life!=0)move(); //��û���Ż�move
	      }
          else//���˼���ʱ��
          {
            key=getch();
	       //if(key!=left&&key!=right&&key!=up&&key!=down)
	        switch(key)
	        {case left:directx=-1;directy=0;break;//�����ƶ�directx=-1;directy=0;
	         case right:directx=1;directy=0;break;//�����ƶ�directx=1;directy=0;
             case up:directx=0;directy=-1;break;//�����ƶ�directx=0;directy=-1;
      	     case down:directx=0;directy=1;break; }  //�����ƶ�directx=0;directy=1;
           }
		 
	     }
}
void food()
{ 
   int i,check=1;
   do               
   {check=1;
	foodx=randomx();
    foody=randomy();
    for(i=0;i<length;i++)//�ж�ʳ���Ƿ������������ˣ�����ǣ�check=0������������ʳ��
		if(foodx==a[i]&&foody==b[i]){check=0;break;}//һֱ�Ƚϵ��ߵ����һ�ڼ�a[length-1]��b[length-1]
   }while(check=0);//����������غ��˼�check=0��Ҫ�������ã�check=1������ѭ��
   dot(foodx,foody,foodc);//û�д�������ʾʳ��
}
int randomx() //��������1��78��������ֵ
{ 
 int j;
 srand((int)time(0)); 
 j=(rand()%78)+1; //rand()����0��RAND_MAX֮��������ֵ
 return j;                      //RAND_MAX������stdlib.h����ֵΪ2147483647��
} 
int randomy() //��������1��38��������ֵ
{ 
 int j;
 srand((int)time(0)); 
 j=(rand()%38)+1; //rand()����0��RAND_MAX֮��������ֵ
 return j;                      //RAND_MAX������stdlib.h����ֵΪ2147483647��
} 
char replay()
{  
   char kb;
   a[0]=6;a[1]=5;a[2]=4;a[3]=3;a[4]=2;a[5]=1;
   b[0]=1;b[1]=1;b[2]=1;b[3]=1;b[4]=1;b[5]=1;
   c[0]=64;c[1]=35;c[2]=35;c[3]=35;c[4]=35;c[5]=35;//����
   system("CLS");//������֮������
   printf("GAME OVER!\n");
   printf("Do you want play agian?\n");
   printf("Please press y for yes,n for no.\n");
   kb=getch();
   while(kb!='y'&&kb!='n'){printf("Please press y for yes,n for no.\n");kb=getch();}//�᲻�������������������ģ�fuckԽ��Խ���ӣ�
   return kb;
}
void change()
{
 int i;
 for(i=length-1;i>0;i--)//��i=length-1����ԭ����i=5
 {
  a[i]=a[i-1];//��һ�ڵ�λ�þ���ǰһ��ԭ����λ��
  b[i]=b[i-1];
 }
 a[0]+=directx;b[0]+=directy;//�ߵ��ƶ���directx��directy���У���غ������̲���
}
void draw()
{
 int i;
 for(i=0;i<length;i++)//��length����6
  dot(a[i],b[i],c[i]);
}
void dot(int x,int y,char z)//����������Ϊ(x,y)��,����״z��ӡ
{
 HANDLE hout;
 COORD coord={x,y};
 hout=GetStdHandle(STD_OUTPUT_HANDLE);
 SetConsoleCursorPosition(hout,coord);//������ƶ�������(a,b)��
 printf("%c",z);                 //�����ߵ�Ԫ��
}
void move()
{
 dot(a[0],b[0],c[0]);
 dot(a[1],b[1],c[1]);
 dot(tempx,tempy,space);Sleep(speed);	
}
void die()
{
 int i;
 for(i=1;i<length;i++)
 {
	 if(a[0]==a[i]&&b[0]==b[i]){life=0;break;}
 }
 //��ײ���Լ������������߽�Ҳ����
 if(a[0]==0||a[0]==79||b[0]==0||b[0]==39)life=0;
}
void border()
{
 for(bdx=0;bdx<80;bdx++)
	 dot(bdx,bdy,bdc);
 bdy=39;
 for(bdx=0;bdx<80;bdx++)
	 dot(bdx,bdy,bdc);//���Ż��߽�
 bdx=0;
 for(bdy=0;bdy<40;bdy++)
	 dot(bdx,bdy,bdc);
 bdx=79;
 for(bdy=0;bdy<40;bdy++)
	 dot(bdx,bdy,bdc);//���Ż��߽�
}
void eat()
{
	if(a[0]==foodx&&b[0]==foody)//����Ե�ʳ��
	{
	  a[length]=a[length-1];b[length]=b[length-1];c[length]=c[length-1];//�Ե�ʳ����β�ͼӳ�
	  length+=1;//��������Ϊ1
	  food();//ʳ��û���˾�Ҫ��������ʳ��
	}
}