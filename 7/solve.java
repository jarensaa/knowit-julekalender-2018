import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class solve {
  public static void main(String[] args) throws IOException {

    List<Integer> testInput = Arrays.asList(1, 1, 2, 3, 5, 5, 5, 3, 4, 4, 4, 4, 3, 5, 7, 6, 6, 7, 8);
    List<Integer> input = new ArrayList<>();

    try (Stream<String> lines = Files.lines(Paths.get("input-vekksort.txt"), Charset.defaultCharset())) {
      lines.forEachOrdered(line -> input.add(Integer.parseInt(line)));
    }

    if (args[0].toString().equals("bf")) {
      System.out.println("Doing brute force search");
      System.out.println(findMaxWithBruteforce(input));
      // do brute force
    } else {
      // Do binary search
    }
  }

  public static int findMaxWithBruteforce(List<Integer> input) {
    int[] lengthStore = new int[input.size()];
    long startTime = System.currentTimeMillis();
    int max = 0;

    Arrays.fill(lengthStore, 1);

    for (int i = 0; i < input.size(); i++) {
      if (i % 5000 == 0) {
        long timeused = System.currentTimeMillis() - startTime;
        startTime = System.currentTimeMillis();
        System.out.println(i + " : " + timeused);
      }
      for (int j = 0; j < i; j++) {
        if (input.get(i) >= input.get(j) && lengthStore[i] < lengthStore[j] + 1) {
          lengthStore[i] = lengthStore[j] + 1;
          max = Math.max(lengthStore[i], max);
        }
      }
    }

    return max;
  }

}