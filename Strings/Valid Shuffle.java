/*check if a string is the valid shuffle of two other strings.
eg - "13sd" is valid shuffle of "2s" and "1d". */

class Main {
  static boolean shuffleCheck(String first, String second, String result) {

    // check length of result is same as
    // sum of result of first and second
    if(first.length() + second.length() != result.length()) {
      return false;
    }
    // variables to track each character of 3 strings
    int i = 0, j = 0, k = 0;

    // iterate through all characters of result
    while (k != result.length()) {

      // check if first character of result matches with first character of first string
      if (i < first.length() && first.charAt(i) == result.charAt(k))
        i++;

      // check if first character of result matches the first character of second string
      else if (j < second.length() && second.charAt(j) == result.charAt(k))
        j++;

      // if the character doesn't match
      else {
        return false;
      }

      // access next character of result
      k++;
    }

    // after accessing all characters of result
    // if either first or second has some characters left
    if(i < first.length() || j < second.length()) {
      return false;
    }

    return true;
  }

  public static void main(String[] args) {

    String first = "XY";
    String second = "12";
    String[] results = {"1XY2", "Y12X"};

    for (String result : results) {
      if (shuffleCheck(first, second, result) == true) {
        System.out.println(result + " is a valid shuffle of " + first + " and " + second);
      }
      else {
        System.out.println(result + " is not a valid shuffle of " + first + " and " + second);
      }
    }
  }
}
