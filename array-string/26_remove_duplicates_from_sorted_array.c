// For details on the problem and test cases see the python version.
int removeDuplicates(int* nums, int numsSize) {
    /*
    This solution works by maintaining two pointers, a free position and a current position one.
    The free position pointer will keep track on what position a value should be written to
    the second pointer is for iterating the array, as the iteration goes on, 
    */
    int free_position = 1; // Initialize at the 2nd position of the array since the first item is always unique
    int current_position = 1; // Start checking for duplicates here onwards
    while (current_position < numsSize){  // Iterate the entire array
        if(nums[current_position] != nums[current_position-1]){  // If the current position has a value different from the one on the previous position.
            nums[free_position] = nums[r];  // This is a unique value and should be moved to the free position
            free_position += 1; // then, since the free position was used, this pointer is moved forward.
        }
        current_position += 1;  // move the iteration forward
    }
    return free_position;  // The last free position used is also the amount of unique integers.
}