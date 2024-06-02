#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int strStr(char* haystack, char* needle) {
    int sizen = strlen(needle);
    int sizeh = strlen(haystack);

    // If needle is empty, return 0
    if (sizen == 0) {
        return 0;
    }

    // Ensure the needle is not longer than the haystack
    if (sizen > sizeh) {
        return -1;
    }

    for (int i = 0; i <= sizeh - sizen; i++) {
        // Check if the substring matches
        int j;
        for (j = 0; j < sizen; j++) {
            if (haystack[i + j] != needle[j]) {
                break;
            }
        }
        if (j == sizen) {
            return i; // Found the match
        }
    }

    return -1; // No match found
}
