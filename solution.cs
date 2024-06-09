```C#
using System;

class Program
{
    static void Main(string[] args)
    {
        Console.Write("Enter a number: ");
        int number = Convert.ToInt32(Console.ReadLine());

        if (IsSumOfTwoSquares(number))
        {
            Console.WriteLine("The number can be expressed as a sum of two squares.");
        }
        else
        {
            Console.WriteLine("The number cannot be expressed as a sum of two squares.");
        }
    }

    static bool IsSumOfTwoSquares(int number)
    {
        for (int i = 0; i * i <= number; i++)
        {
            for (int j = 0; j * j <= number; j++)
            {
                if (i * i + j * j == number)
                {
                    return true;
                }
            }
        }
        return false;
    }
}
```