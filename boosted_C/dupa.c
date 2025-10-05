#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr = (int *)malloc(1);
    printf("%d\n", *ptr);
    return 0;
}