#include <stdio.h>
#include <stdlib.h>

// 1. DATA STRUCTURE DEFINITIONS
// i. for node definition: include a capacity + type
// ii. to make the graph connections as we go
// iii. also have a "visited" component just in case
// iv. ENUM for each of the to-put stuff
// can use this!
typedef enum {
    SINGLE_HORIZONTAL = '-',
    SINGLE_VERTICAL = '|',
    DOUBLE_HORIZONTAL = '=',
    DOUBLE_VERTICAL = '"',
    TRIPLE_HORIZONTAL = 'E',
    TRIPLE_VERTICAL = '#'
} BridgeType;

// for a, b, and c. ah
// typedef enum {
//     A = 10;
//     B = 11;
//     C = 12;
// } BiggerNum;

// 2. FUNCTIONS: can split it to different files -> 
// i. one for adjacency list related stuff; 
// ii. the other for DFS backtracking
// iii. print graph function on here
// void printResult(graph) {
    // print(graph) if there is a solution
    // print (normal graph) if there is no solution ?? or just put NO SOLUTION
// }

// 3. GET INPUT
int main(void) {
    // BLACKBOX

    // get input in char**
    // create empty adjacency list 

    // put it through the graph to make an adjancecy graph

    // then, find the HASHI puzzle thing

    // print out the graph
    // printResult(graph);


    // TODO: REMOVE LOL
    char take[] = "a1.2.";
    printf("Before: %s\n", take);
    for (int i = 0; i < 6; i++) {
        if (i % 2 == 0) {
            take[i] = SINGLE_HORIZONTAL;
        }
    }

    printf("After: %s\n", take);

    return 0;
}