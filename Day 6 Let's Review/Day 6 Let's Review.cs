using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int counter = Int32.Parse(Console.ReadLine());

        for (int i = 1; i <= counter; i++) {
            string myString = Console.ReadLine();

            for (int j = 0; j < myString.Length; j++) {
                if (j % 2 == 0) {
                    Console.Write(myString[j]);
                }
            }

            Console.Write(" ");

            for (int j = 0; j < myString.Length; j++) {
                if (j % 2 == 1) {
                    Console.Write(myString[j]);
                }
            }
            Console.WriteLine();
        }
    }
}
