#include <stdio.h>
#include <string.h>

int main()
{
    char c[100];
    int found = 0;

    scanf("%s", c);

    for (int i = 0; c[i] != '\0'; i++)
    {
        for (int j = i + 1; c[j] != '\0'; j++)
        {
            if (c[i] == c[j] && i != j)
            {
                found = 1;
                printf("%c ", c[i]);
                break;
            }
        }
    }

    if (!found)
    {
        printf("No duplicates");
    }

    return 0;
}

