#include <stdio.h>
#include <stdlib.h>

// Comparison function for integers
int compare(const void* a, const void* b) {
    int num1 = *(int*)a;
    int num2 = *(int*)b;
    
    if (num1 < num2) {
        return -1;
    } else if (num1 > num2) {
        return 1;
    } else {
        return 0;
    }
}

int main() {
    int arr[] = {5, 2, 8, 1, 9};
    int size = sizeof(arr) / sizeof(arr[0]);
    
    qsort(arr, size, sizeof(int), compare);
    
    printf("Sorted array: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    return 0;
}
