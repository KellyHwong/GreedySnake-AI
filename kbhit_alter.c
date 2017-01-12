#include <stdio.h>
#include <string.h>

int main() {
    char c;
    while(1) {
        c = getchar();
        printf("%s\n", &c);
    }
    return 0;
}
