import java.util.*;
import java.math.BigInteger;
public class prime {
    public static final BigInteger  ONE  = BigInteger.ONE ;
    public static void main(String[] args) {
        BigInteger two = new BigInteger("2");
        BigInteger start_num = new BigInteger("100");
        BigInteger end_num = new BigInteger("1000");
        BigInteger temp = new BigInteger("25");
        for (BigInteger j = start_num;j.compareTo(end_num.add(ONE))<0 ;j=j.add(new BigInteger("100"))) {
        int count = 0;
        for (BigInteger i = two;i.compareTo(j.add(ONE)) < 0; i = i.add(ONE))
            if (i.isProbablePrime(9))
                count ++;
        System.out.println(j+"->"+count+"->"+(j.divide(new BigInteger("25")).subtract(new BigInteger(temp))));
        }
    }}
