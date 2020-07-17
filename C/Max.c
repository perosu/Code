/*
 *2018.1.20 13.00
 *比较两个数谁大，加上了书上没有的一些功能
 **等值判断
 **多次判断
 *if和while语句有点忘了XD
 */
#include <stdio.h>
int main(void) {
  int a,b,c,d;
  while (d == 1) {
    printf("input two number\nif they equal,return -1\nint<space>int:\n");
    scanf("%d %d",&a,&b);
    c = max(a,b);
    printf("%d\ncontinue?(1:yes)",c);
    scanf("%d",&d);
    return 0;
  }
}
int max(int x,int y) {
  if (x < y) {
    return y;
  }
  else {
    if (x > y) {
      return x;
    }
    else {
    return -1;
    }
  }
}
