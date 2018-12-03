import java.util.Stack;

public class Run {

  static int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
      97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211,
      223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
      353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
      491, 499, 503, 509, 521, 523, 541 };

  static long maxnum = Long.parseLong("4294967296");

  public static void main(String[] args) {

    int counter = 1;
    int[] primeIndexes = new int[24];
    primeIndexes[23] = 1;

    Stack<int[]> primeArraysToCheck = new Stack<>();
    primeArraysToCheck.push(primeIndexes);

    while (!primeArraysToCheck.empty()) {
      int[] primeArray = primeArraysToCheck.pop();
      if (productIsLessThanMax(primeArray)) {
        counter++;
        primeArraysToCheck.push(shiftarray(primeArray));
        incrementLastPrime(primeArray);
        primeArraysToCheck.push(primeArray);
      }
    }

    System.out.println(counter);
  }

  public static int[] shiftarray(int[] array) {
    int[] shiftedArray = new int[array.length];

    for (int i = 0; i < shiftedArray.length - 1; i++) {
      shiftedArray[i] = array[i + 1];
    }

    shiftedArray[array.length - 1] = array[array.length - 1];
    return shiftedArray;
  }

  public static void incrementLastPrime(int[] primeIndexesArray) {
    primeIndexesArray[primeIndexesArray.length - 1]++;
  }

  public static boolean productIsLessThanMax(int[] primeIndexesArray) {
    long product = 1;
    for (int primeIndex : primeIndexesArray) {
      product *= primes[primeIndex];
    }

    if (product > maxnum)
      return false;
    return true;
  }
}
