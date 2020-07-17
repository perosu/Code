// 被注释掉的是另一种实现方式
#include <stdio.h>
int main() {
  int a, b;
  printf("输入两个数以求平方和\n格式int<space>int:\n");
  scanf("%d %d", &a, &b);
  // printf("%d",a*a+b*b);
  return a * a + b * b;
}
