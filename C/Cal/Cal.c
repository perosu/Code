//2018.3.30
//简易计算器，还不完善
//ArchGu
#include <stdio.h>
#include <stdlib.h>
int main() {
  char c;
  double a, b;
  int m;
  while (1) {
    printf("Please input mode number\n1:Simple calculator\n2:Change lowercase "
           "letters\nOther:Quit\n");
    printf(">");
    scanf("%d", &m);
    if (m == 1) {
      while (1) {
        printf(">");
        scanf("%lf%c", &a, &c);
        switch (c) {
        case 'c':
          printf("%lf\n", a * 2 * 3.1415926);
          break;
        case 'd':
          printf("%lf\n", a * a * 3.1415925);
          break;
        case 't':
          printf("%lf\n",(float)5 / (float)9 * (a - (float)32));
          break;
        case 'f':
          printf("%lf\n", a * (float)9 / (float)5 + 32);
          break;
        case '+':
          scanf("%lf", &b);
          printf("%lf\n", a + b);
          break;
        case '-':
          scanf("%lf", &b);
          printf("%lf\n", a - b);
          break;
        case '*':
          scanf("%lf", &b);
          printf("%lf\n", a * b);
          break;
        case '/':
          scanf("%lf", &b);
          if (b == 0) {
            printf("Error\n");
            break;
          }
          else {
          printf("%lf\n", a + b);
          break;
          }
        case 'q':{
          break;
          break;
        }
        default:
          printf("Error\n");
          break;
        }
      }
    }
  else if (m == 2) {
    while (1) {
      printf(">");
      scanf("%c", &c);
      getchar();
      if (c >= 'A' && c <= 'Z') {
        printf("ASCII:%d\n%c\n", c, c + 32);
      } else {
        break;
      }
    }
    } else {
      system("exit\n");
    }
  }
  return 0;
}
