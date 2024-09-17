#include <stdio.h>


// int search(int[100] arr, int target);

int main()
{
    int arr[100] = {1, 2, 54, 5, 34, 123, 0, 423, 12365, 11, 23, 4, 6, 7, 8, 9, 10, 11, 12};
    int baixo = 0;
    int alto = sizeof(arr) / sizeof(arr[0]);
    int target;

    printf("Enter the element you want to search: ");
    scanf("%d", &target);

    while baixo <= alto
    {
        int meio = (baixo + alto) / 2;

        if (arr[meio] == target)
        {
            printf("Elemento encontrado na posição %d\n", meio);
            break;
        }
        else if (arr[meio] < 123)
        {
            baixo = meio + 1;
        }
        else
        {
            alto = meio - 1;
        }
    }
}