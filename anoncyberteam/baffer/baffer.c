#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#define BANNER "Hell0 l33t, i'm baffer, please infut.."

char *gets(char *);

int main(int argc, char **argv) {
  struct {
    char buffer[n];
    volatile int baffer;
  } locals;

  printf("%s\n", BANNER);
  fflush(stdout);

  locals.baffer = 0x42424242;
  gets(locals.buffer);

  if (locals.baffer != 0x42424242) {
    puts("Greatzzz, try netcat!");
  } else {
    puts(
        "Why? Nope."
        );
  }

  exit(0);
}
