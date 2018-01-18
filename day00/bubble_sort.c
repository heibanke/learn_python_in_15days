/**********************
copyRight by heibanke
***********************/

#include <stdio.h>
#define LEN 9
void bubble_sort(int nums[],int length){
    int temp;
    for(int i=1;i<length;i++){
        for(int j=0;j<length-i;j++)
        {
            if(nums[j]>nums[j+1]){
                temp=nums[j];
                nums[j]=nums[j+1];
                nums[j+1]=temp;
            }
        }
    }
}

int main(){
    int aa[LEN]={34,9,5, 23,14,7,32,2,12};
    bubble_sort(aa,LEN);
    for(int i=0;i<LEN;i++)
        printf("%d,",aa[i]);
    printf("\n");
    return 0;
}