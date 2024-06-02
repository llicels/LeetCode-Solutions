#include <stdlib.h>
int isPalindrome(int x) {

    int i = 0;
    int* number = (int*)malloc(31*sizeof(int));
    int* numberP = (int*)malloc(31*sizeof(int));
    int ret = 0;

    if(x<0){
        ret = 0;
    }else if(x==0){
        ret = 1;
    }

    while(x>0){
        int mod = x % 10;
        number[i] = mod;
        x = x/10;
        i++;

    }

    int a = i-1;
    
    for(int j=0; j<i; j++){
        numberP[j] = number[a];
        a = a-1;
    }


    for(int b=0; b<i; b++){
        printf("\n %d e %d", numberP[b], number[b]);
        if(number[b] != numberP[b]){
            return 0;
        }else{
            ret = 1;
        }
    }

    return ret;

}
