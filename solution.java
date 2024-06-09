Here is a Java console application that solves the problem:

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a number:");
        int number = scanner.nextInt();
        System.out.println(isSumOfTwoSquares(number));
    }

    private static boolean isSumOfTwoSquares(int number) {
        if (number < 0) {
            return false;
        }
        for (int i = 0; i * i <= number; i++) {
            for (int j = i; j * j <= number; j++) {
                if (i * i + j * j == number) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

This program asks the user to input a number and then checks if it can be expressed as a sum of two squares. It does this by iterating through all possible pairs of numbers whose squares could sum to the input number. If it finds such a pair, it returns true. If it doesn't find such a pair after checking all possibilities, it returns false.