#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 3

struct Student {
    int roll;
    char name[30];
    float marks;
};

int main(void) {
    struct Student students[MAX_STUDENTS] = {
        {1, "Asha", 82.5f},
        {2, "Ravi", 74.0f},
        {3, "Meera", 91.25f}
    };

    float total = 0;
    int best = 0;
    for (int i = 0; i < MAX_STUDENTS; i++) {
        printf("Roll %d: %-6s %.2f\n", students[i].roll, students[i].name, students[i].marks);
        total += students[i].marks;
        if (students[i].marks > students[best].marks)
            best = i;
    }
    printf("Average marks: %.2f\n", total / MAX_STUDENTS);
    printf("Topper: %s (%.2f)\n", students[best].name, students[best].marks);
    return 0;
}
