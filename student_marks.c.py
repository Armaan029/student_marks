#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_SUBJECTS 5

struct Student {
    int roll;
    char name[50];
    float marks[MAX_SUBJECTS];
    float total;
    float average;
};

void input_students(struct Student students[], int *n, int *subjects) {
    int i, j;
    printf("Enter number of students: ");
    scanf("%d", n);
    printf("Enter number of subjects (max %d): ", MAX_SUBJECTS);
    scanf("%d", subjects);

    if (*subjects > MAX_SUBJECTS) {
        *subjects = MAX_SUBJECTS;
        printf("Subjects limited to %d.\n", MAX_SUBJECTS);
    }

    for (i = 0; i < *n; i++) {
        printf("\nStudent %d\n", i + 1);
        printf("Roll number: ");
        scanf("%d", &students[i].roll);
        printf("Name: ");
        scanf(" %[^\n]", students[i].name);

        students[i].total = 0;
        for (j = 0; j < *subjects; j++) {
            printf("Marks in subject %d: ", j + 1);
            scanf("%f", &students[i].marks[j]);
            students[i].total += students[i].marks[j];
        }
        students[i].average = students[i].total / (*subjects);
    }
}

void display_students(struct Student students[], int n, int subjects) {
    int i, j;
    printf("\n=== Student Marks List ===\n");
    for (i = 0; i < n; i++) {
        printf("\nRoll: %d | Name: %s\n", students[i].roll, students[i].name);
        for (j = 0; j < subjects; j++) {
            printf("  Subject %d: %.2f\n", j + 1, students[i].marks[j]);
        }
        printf("  Total: %.2f | Average: %.2f\n", students[i].total, students[i].average);
    }
}

void sort_by_total(struct Student students[], int n) {
    int i, j;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            if (students[j].total < students[j + 1].total) {
                struct Student temp = students[j];
                students[j] = students[j + 1];
                students[j + 1] = temp;
            }
        }
    }
}

void display_rank_list(struct Student students[], int n) {
    int i;
    printf("\n=== Rank List (by Total Marks) ===\n");
    for (i = 0; i < n; i++) {
        printf("%d. %s (Roll: %d) - Total: %.2f, Average: %.2f\n",
               i + 1, students[i].name, students[i].roll,
               students[i].total, students[i].average);
    }
}

int main() {
    struct Student students[MAX_STUDENTS];
    int n, subjects;

    input_students(students, &n, &subjects);
    display_students(students, n, subjects);

    sort_by_total(students, n);
    display_rank_list(students, n);

    return 0;
}
