/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int p1;
    int p2;
    int a, b;

    for (int i = 0; i<numsSize; i++){
        for (int j =0; j<numsSize-1; j++){
            a = i;
            b = j+1;

            if(nums[a]+nums[b] == target && a != b){
                p1 = a;
                p2 = b;
            }
        }
    }

    int *solution = (int *)malloc(2*sizeof(int));

    solution[0]=p1;
    solution[1]=p2;

    *returnSize=2;
    return solution;
}
