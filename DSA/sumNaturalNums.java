//find sum of first natural numbers upto arg number
public class sumNaturalNums {
  public static int sum(int number){
    if (number <=1 ) return number;

    return number + sum(number - 1);
  }

  public static void main (String[] args){
    System.out.println(sumNaturalNums.sum(10));
    System.out.println(sumNaturalNums.sum(20));
  }
}
