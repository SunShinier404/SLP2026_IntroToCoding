package practiceExercises.sara_practice;

import java.util.Scanner;
import java.util.Random;

public class NumberGuessingGame {
    public static void main(String[] args) {
        Random random = new Random();
        int secretNumber = random.nextInt(100) + 1;

        Scanner input = new Scanner(System.in);
       

        System.out.println("Guess a number between 1 and 100");
        int guess = input.nextInt();
        while (guess != secretNumber){
        if (guess > secretNumber){
            System.out.println("Too high! Try again.");
        }
        else if(guess < secretNumber){
            System.out.println("Too low! Try Again.");
        }
        
        System.out.println("Enter another guess: ");
        guess = input.nextInt();

        }
        System.out.println("You guessed it! Good job:)");
        input.close();
    }
    
}
