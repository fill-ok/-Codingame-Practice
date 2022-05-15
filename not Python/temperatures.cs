// puzzle easy // https://www.codingame.com/ide/puzzle/temperature-code-golf

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Solution
{
    static void Main(string[] args)
    {
        List<int> a = new  List<int>();
        List<int> b = new  List<int>();

        int n = int.Parse(Console.ReadLine()); // the number of temperatures to analyse
        string[] inputs = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++)
        {
            int t = int.Parse(inputs[i]);// a temperature expressed as an integer ranging from -273 to 5526
            a.Add(t);
            b.Add(Math.Abs(t-0));
        }

        if (b.Count() == 0){
            Console.Write(0);
        }

        else {
            int minVal = b.Min();
            int index = b.IndexOf(minVal);

            for (int i = 0; i < a.Count(); i++){
                if (Math.Abs(a[index]) == Math.Abs(a[i]) && i!=index){
                    if (a[index] > a[i]){
                        Console.Write(a[index]);
                        System.Environment.Exit(0); 
                    } 
                    else{
                        Console.Write(a[i]);
                        System.Environment.Exit(0); 
                    }
                }
            } Console.Write(a[index]);
        } 
    }
}
