#include <stdio.h>
#include <string.h>

void forever() {
    // Heheheh
    int z = 0;
    for(;;) {
        printf("%d\n", z);
        z += 1;
    }
}

void oddsEvens(int max) {
    int MYCONST = 10;
    for(int i = 0; i < max; i++) {
        int j = i * MYCONST;
        if(i % 2 == 0) {
            printf("%d = Even\n", i);
        } else {
            printf("%d = Odd\n", i);
        }
    }
    printf("\n");
}

struct Person {
    char fname[50];
    char lname[50];
    char favorite_color[20];
    float age;
};

int main(void) {
    printf("[MOAL]: manifest typing example\n");
    oddsEvens(99);

    char fname[100];
    char lname[100];
    int age;

    printf("Enter your first and last name, and age: ");
    scanf("%s %s %d", fname, lname, &age);

    struct Person ella;
    strcpy(ella.fname, "Ella");
    strcpy(ella.lname, "Tabor");
    ella.age = 1.3;
    strcpy(ella.favorite_color, "gurn");

    printf("struct: %s %s %f %s", ella.fname, ella.lname, ella.age, ella.favorite_color);
    printf("\nYou entered: %s %s %d\n", fname, lname, age);

    // forever();
    return 0;
}
