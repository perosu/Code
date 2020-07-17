//2017.11.17晚完成代码，debug数值类型错误，函数输出选了i
//2017.11.18完成注释，造轮子，造轮子，造轮子：）
#include <iostream>
using namespace std;
int main()
{
  int i = 8;//纸的厚度，单位0.01mm以配合整型
  int time = 0;//折叠次数
  do//做循环以叠加次数和纸厚度
    {
      time += 1;
      i = 2 * i;
    }
  while (i <= 884813000);//判断条件
  if (i < 884813000)//再次判断以解决while设计缺陷，求出次数
    {
      cout << time + 1;
    }
  else
    {
      cout << time;
    }
}
