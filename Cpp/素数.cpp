//2017.11.18完成，debug半天
//有个问题，在大的数字时会输出多个判断，最后一个是对的
//有一个问题暂时无法解决，就是完成一个输出后无法继续从头开始
#include <iostream>
using namespace std;
int main()
{
     int number;
     int i; //声明变量
     cout << "please input a int type number\n";
     cin >> number;
     //预防输入小小数而发生错误        cin >> number;   //从控制台输入数字
     if (number <= 2) //判断数字大小以进行下一步
       {
         cout << "please input a number>2";
         //输出错误
         }
     else
       {
         for (int i = 2; i < number; i++)
         // for出i
         if (number % i == 0) //判断能否被整除以分类
             {
                   cout << "no"; //输出
                   break;
                 }
         else
             {
                   cout << "yes"; //输出
                 }
           }
}
