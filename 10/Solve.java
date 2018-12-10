import java.io.FileReader;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Solve {
  public static void main(String[] args) throws Exception {
    Stack<Integer> numberStore = new Stack<>();
    Queue<Character> operations = new LinkedList<>();

    Scanner inputFile = new Scanner(new FileReader("input.spp"));
    while (inputFile.hasNext()) {
      String line = inputFile.nextLine();
      for (char character : line.toCharArray()) {
        operations.add(character);
      }
    }

    while (!operations.isEmpty()) {
      char op = operations.poll();

      if (op == ' ') {
        numberStore.push(31);
      }

      if (op == ':') {
        int sum = 0;
        while (!numberStore.isEmpty()) {
          sum += numberStore.pop();
        }
        numberStore.push(sum);
      }

      if (op == '|') {
        numberStore.push(3);
      }

      if (op == '\'') {
        numberStore.push(numberStore.pop() + numberStore.pop());
      }

      if (op == '.') {
        int A = numberStore.pop();
        int B = numberStore.pop();
        numberStore.push(A - B);
        numberStore.push(B - A);
      }

      if (op == '_') {
        int A = numberStore.pop();
        numberStore.push(A * numberStore.pop());
        numberStore.push(A);
      }

      if (op == '/') {
        numberStore.pop();
      }

      if (op == 'i') {
        numberStore.push(numberStore.peek());
      }

      if (op == '\\') {
        numberStore.push(numberStore.pop() + 1);
      }

      if (op == '*') {
        numberStore.push(Math.floorDiv(numberStore.pop(), numberStore.pop()));
      }

      if (op == ']') {
        int num = numberStore.pop();
        if (num % 2 == 0)
          numberStore.push(1);
      }

      if (op == '[') {
        int num = numberStore.pop();
        if (num % 2 == 1)
          numberStore.push(1);
      }

      if (op == '~') {
        int max = Math.max(numberStore.pop(), numberStore.pop());
        numberStore.push(Math.max(max, numberStore.pop()));
      }
    }

    System.out.println(numberStore);

  }
}