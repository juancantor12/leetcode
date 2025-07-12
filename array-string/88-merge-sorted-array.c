void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
    int p = m + n - 1;
    m -= 1;
    n -= 1;
    while (n >= 0 && m >= 0) {
        if (nums2[n] > nums1[m]) {
            nums1[p] = nums2[n];
            n -= 1;
        } else {
            nums1[p] = nums1[m];
            m -= 1;
        }
        p -= 1;
    }
    while (n >= 0) {
        nums1[p] = nums2[n];
        n -= 1;
        p -= 1;
    }
}