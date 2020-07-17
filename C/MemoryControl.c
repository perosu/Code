#include <stdio.h>
int main() {
  char ch[1];
  int i = 0;
  while (ch[0] != '\n') {
    scanf("%c",&ch[0]);
    if (ch[0] != ' ')
      i += 1;
  }
  printf("%d",i-1);
  return 0; // Exit
}