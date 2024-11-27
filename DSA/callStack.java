//simulate the actions of a callstack

public class callStack {
  
  public String A(){
    return "Hello " + B();
  }

  public String B(){
    return "I am Learing " + C();
  }

  public String C(){
    return "Recursion";
  }

  public static void main(String[] args){
    callStack cs = new callStack();
    System.out.println(cs.A());
  }
  
}
