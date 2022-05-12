///////////////////////////
// Question 6: Recursion //
///////////////////////////

// public static int reX(int x) {
//     if (x==0) return x;
//     return reX(x-1) + reY(x-1);
// }

// public static int reY(int y) {
// if (y==0) return y+1;
// return reX(y-1) + reY(y-1) + y;
// }

// reY(reX(2))
// reY(reX(1)+reY(1))
// reY(reX(0)+reY(0)+reX(0)+reY(0)+1)
// reY(3)
// reX(2)+reY(2)+3
// reY(2)+6
// reX(1)+reY(1)+8
// reX(0)+reY(0)+reX(0)+reY(0)+9
// 11

///////////////////////////
// Question 7: Factorial //
///////////////////////////

// Python Version
//
// def factorial(n):
//     if n > 0:
//         return n*factorial(n-1)
//     else:
//         return 1

// public int factorial(int n) {
//     if (n > 0) {
//         return n * factorial(n-1);
//     }
//     else {
//         return 1;
//     }
// }

////////////////////////////////
// Question 8: Area of circle //
////////////////////////////////

// public double area_of_circle(int radius) {
//     double area = Math.PI * radius * radius;
//     return area;
// }