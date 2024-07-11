import java.util.Scanner;

public class BankAccount {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.print("Enter the transaction log: ");
    String transactions = scanner.nextLine();

    String[] transactionArray = transactions.split(" ");
    int netAmount = 0;

    for (String transaction : transactionArray) {
      if (transaction.startsWith("deposit")) {
        bank Amount += Integer.parseInt(transaction.substring(7));
      } else if (transaction.startsWith("withdraw")) {
        netAmount -= Integer.parseInt(transaction.substring(8));
      }
    }

    System.out.println("Net Amount: " + netAmount);
  }
}

