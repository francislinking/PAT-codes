#include <stdio.h>
#include <string.h> 
#include <stdlib.h>
  
typedef int Position;
#define NotFound -1
  
void BuildMatch( char *pattern, int *match )
{
    Position i, j;
    int m = strlen(pattern);
    match[0] = -1;
      
    for ( j=1; j<m; j++ ) {
        i = match[j-1];
        while ( (i>=0) && (pattern[i+1]!=pattern[j]) )
            i = match[i];
        if ( pattern[i+1]==pattern[j] )
             match[j] = i+1;
        else match[j] = -1;
    }
}
  
Position KMP( char *string, char *pattern )
{
    int n = strlen(string);
    int m = strlen(pattern);
    Position s, p, *match;
      
    if ( n < m ) return NotFound;
    match = (Position *)malloc(sizeof(Position) * m);
    BuildMatch(pattern, match);
    s = p = 0;
    while ( s<n && p<m ) {
        if ( string[s]==pattern[p] ) {
            s++; p++;
        }
        else if (p>0) p = match[p-1]+1;
        else s++;
    }
    return ( p==m )? (s-m) : NotFound;
}
int main() {
  char string[1000001] = {0};
  char pattern[1000001] = {0};
  scanf("%s\n", (char *)&string);
  int n;
  scanf("%d", &n);
  for(int i=0; i<n; i++) {
    scanf("%s\n", (char *)&pattern);
    Position p = KMP(string, pattern);
    if(p != NotFound) {
      if(i == n - 1) {
        printf("%s", (char *)string+p);
      } else {
        printf("%s\n", (char *)string+p);
      }
    } else {
      if(i == n - 1) {
        printf("Not Found");
      } else {
        printf("Not Found\n");
      }
    }
  }
  return 0;
}