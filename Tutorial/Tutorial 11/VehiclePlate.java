import java.util.*;

public class VehiclePlate {
 
   public static void main(String[] args) {

      Scanner stdIn = new Scanner(System.in);

      System.out.print("Vehicle Plate (excluding the checksum alphabet at the end): ");
      String plate = stdIn.nextLine();
      plate = plate.toUpperCase();
      String prefix =  plate.replaceAll("[0123456789]", "");
      int suffix = Integer.parseInt(plate.replaceAll("[a-zA-Z]",""));
      char checkSum = generateCheckSum (prefix, suffix);

      System.out.println("Vehicle Plate is: " + prefix + " " + suffix + " " + checkSum);

   } // end main

   /*********************************************************
      
   **********************************************************/
   public static char generateCheckSum(String prefix, int suffix) {

   }// end generateCheckSum

}// end class 