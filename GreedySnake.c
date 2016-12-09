#include<stdio.h>
//#include<windows.h>
#include<stdlib.h>
#include<time.h> 
//#include<conio.h>
#define up 119
#define down 115
#define left 97
#define right 100//上下左右分别用wsad键控制

void play();
char replay();
//试出来控制台窗口的长度是80(范围0~79)
//宽度木有限制,自定义为40(0~39),刚好能在电脑屏幕上容下
void dot(int x,int y,char z);
void draw();
void change();
void move();

void die();
int life=1;

void border();//画边界
int bdx=0;
int bdy=0;
char bdc='0';

int speed=100;//游戏速度设置，speed指间隔时间，可以用来控制蛇的速度

int randomx();int randomy();
void food();//设置食物
int foodx;int foody;char foodc=38;
void eat();

int length=6;//蛇一开始有6节，最后一节是a[length-1]和b[length-1]
int a[100]={6,5,4,3,2,1},b[100]={1,1,1,1,1,1};//蛇的长度不要超过100= =
char c[100]={64,35,35,35,35,35};//用数组可能更好
int directx=1,directy=0;//方向也要初始化！蛇的移动靠directx，directy进行，这关乎到键盘操作

int tempx,tempy;char space=' ';
char key;
char rp='y';//rp就是replay的缩写，用来标志是否重玩

void main()
{
  while(rp=='y') //外循环为重玩而设置
   {
	border();//边界的初始化
	draw();//画出蛇，进行初始化
    food();//食物的初始化
    play();//将游戏过程打包成函数,蛇死亡后从play中跳出
	rp=replay();
   }
}
void play()//play函数是一个循环
{
        while(life!=0)//这个循环用来进行游戏life==0游戏结束
        {
	            
		  if(!kbhit())//当没有按键的时候
          {
	       tempx=a[length-1];tempy=b[length-1];
	       change();//交换坐标值
	       die();//判断死亡
		   eat();//判断蛇吃没吃食物
		   if(life!=0)move(); //蛇没死才会move
	      }
          else//按了键的时候
          {
            key=getch();
	       //if(key!=left&&key!=right&&key!=up&&key!=down)
	        switch(key)
	        {case left:directx=-1;directy=0;break;//向左移动directx=-1;directy=0;
	         case right:directx=1;directy=0;break;//向右移动directx=1;directy=0;
             case up:directx=0;directy=-1;break;//向上移动directx=0;directy=-1;
      	     case down:directx=0;directy=1;break; }  //向下移动directx=0;directy=1;
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
    for(i=0;i<length;i++)//判断食物是否落在蛇身上了，如果是，check=0，并重新设置食物
		if(foodx==a[i]&&foody==b[i]){check=0;break;}//一直比较到蛇的最后一节即a[length-1]和b[length-1]
   }while(check=0);//如果和身体重合了即check=0就要重新设置，check=1就跳出循环
   dot(foodx,foody,foodc);//没有错误再显示食物
}
int randomx() //产生介于1到78间的随机数值
{ 
 int j;
 srand((int)time(0)); 
 j=(rand()%78)+1; //rand()返回0至RAND_MAX之间的随机数值
 return j;                      //RAND_MAX定义在stdlib.h，其值为2147483647。
} 
int randomy() //产生介于1到38间的随机数值
{ 
 int j;
 srand((int)time(0)); 
 j=(rand()%38)+1; //rand()返回0至RAND_MAX之间的随机数值
 return j;                      //RAND_MAX定义在stdlib.h，其值为2147483647。
} 
char replay()
{  
   char kb;
   a[0]=6;a[1]=5;a[2]=4;a[3]=3;a[4]=2;a[5]=1;
   b[0]=1;b[1]=1;b[2]=1;b[3]=1;b[4]=1;b[5]=1;
   c[0]=64;c[1]=35;c[2]=35;c[3]=35;c[4]=35;c[5]=35;//重置
   system("CLS");//蛇死亡之后清屏
   printf("GAME OVER!\n");
   printf("Do you want play agian?\n");
   printf("Please press y for yes,n for no.\n");
   kb=getch();
   while(kb!='y'&&kb!='n'){printf("Please press y for yes,n for no.\n");kb=getch();}//会不会有人无聊输入其他的？fuck越搞越复杂！
   return kb;
}
void change()
{
 int i;
 for(i=length-1;i>0;i--)//用i=length-1代替原来的i=5
 {
  a[i]=a[i-1];//后一节的位置就是前一节原来的位置
  b[i]=b[i-1];
 }
 a[0]+=directx;b[0]+=directy;//蛇的移动靠directx，directy进行，这关乎到键盘操作
}
void draw()
{
 int i;
 for(i=0;i<length;i++)//用length代替6
  dot(a[i],b[i],c[i]);
}
void dot(int x,int y,char z)//函数在坐标为(x,y)处,以形状z打印
{
 HANDLE hout;
 COORD coord={x,y};
 hout=GetStdHandle(STD_OUTPUT_HANDLE);
 SetConsoleCursorPosition(hout,coord);//将光标移动到坐标(a,b)处
 printf("%c",z);                 //画出蛇的元素
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
 //蛇撞到自己会死，碰到边界也会死
 if(a[0]==0||a[0]==79||b[0]==0||b[0]==39)life=0;
}
void border()
{
 for(bdx=0;bdx<80;bdx++)
	 dot(bdx,bdy,bdc);
 bdy=39;
 for(bdx=0;bdx<80;bdx++)
	 dot(bdx,bdy,bdc);//横着画边界
 bdx=0;
 for(bdy=0;bdy<40;bdy++)
	 dot(bdx,bdy,bdc);
 bdx=79;
 for(bdy=0;bdy<40;bdy++)
	 dot(bdx,bdy,bdc);//竖着画边界
}
void eat()
{
	if(a[0]==foodx&&b[0]==foody)//如果吃掉食物
	{
	  a[length]=a[length-1];b[length]=b[length-1];c[length]=c[length-1];//吃到食物蛇尾巴加长
	  length+=1;//长度增量为1
	  food();//食物没有了就要重新设置食物
	}
}