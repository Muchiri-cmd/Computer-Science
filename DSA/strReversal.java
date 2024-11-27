//Take a string and reverse it

public class strReversal {

  public String reverseString(String input){
    //base case 
    if (input.equals("")){
      return "";
    }
    //recursive call
    return reverseString(input.substring(1)) + input.charAt(0);
  }

  public static void main(String[] args) {
    strReversal str = new strReversal();
    System.out.println(str.reverseString("Hello World"));
  }
  
}
