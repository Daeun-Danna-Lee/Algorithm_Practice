#include <stdio.h>

int main() {
    int data = 0;
    int i,j;
    int k = 0;
    int tarr[10][10] = {0};
    
    printf("입력할 데이터의 개수를 적어주세요: "); //입력할 데이터의 개수를 data 에 받기
    scanf("%d", &data);
    
    while (k++ < data) {
        printf("입력할 데이터의 위치(행, 열)과 값을 입력해주세요: "); //입력할 데이터의 개수를 data 에 받기
        scanf("%d %d", &i, &j);
        scanf("%d", &tarr[i][j]);
    }

    for (int i=0; i<10; i++) {
        for (int j=0; j<10; j++) {
            printf("%d ", tarr[i][j]);
        }
        printf("\n");
    }

    return 0;
}
