import java.util.*;

class aws {
    public static int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    public static int lcm(int a, int b) {
        return (a * b) / gcd(a, b);
    }

    public static int countValidPairs(int[] arr) {
        int n = arr.length;
        int count = 0;
        Set<Integer> arrSet = new HashSet<>();
        for (int num : arr) {
            arrSet.add(num);
        }

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int hcf = gcd(arr[i], arr[j]);
                int lcmVal = lcm(arr[i], arr[j]);
                int product = hcf * lcmVal;

                if (arrSet.contains(product)) {
                    count++;
                }
            }
        }

        return count;
    }

    public static void main(String[] args) {
        int[] A = {1, 2, 3, 4, 5};
        int result = countValidPairs(A);
        System.out.println(result);  // Output: 10
    }
}