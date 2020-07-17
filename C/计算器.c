/* 
 *简易计算器
 *学习switch
 *2018.1.17 20:02
 *版本1
 */
#include <stdio.h>
int main() {
  double a = 0.0;
  double b = 0.0;
  char c = 0.0;
  printf("输入一个算式\n类似1+1\n");
  scanf("%lf%c%lf", &a, &c, &b);
  switch (c) {
  case '+':
    printf("%lf", a + b);
    break;
  case '-':
    printf("%lf", a - b);
    break;
  case '/':
    printf("%lf", a / b);
    break;
  case '*':
    printf("%lf", a * b);
    break;
  default:
    printf("error");
    break;
  }
  return 0;
}
