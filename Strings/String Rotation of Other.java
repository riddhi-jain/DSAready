/*Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)

Approach:
Return True if str2 is a substring of (str1+str1) */

	
class StringRotation
{
	static boolean areRotations(String str1, String str2)
	{
		// There lengths must be same and str2 must be
		// a substring of str1 concatenated with str1.
		return (str1.length() == str2.length()) &&
			((str1 + str1).indexOf(str2) != -1);
	}
	
	// Driver method
	public static void main (String[] args)
	{
		String str1 = "AACD";
		String str2 = "ACDA";

		if (areRotations(str1, str2))
			System.out.println("Strings are rotations of each other");
		else
			System.out.printf("Strings are not rotations of each other");
	}
}
