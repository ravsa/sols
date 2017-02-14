import java.io.*;
import java.util.*;


class jam
{

    public static void main(String args[])
    {
        InputReader sc=new InputReader(System.in);
        PrintWriter pw=new PrintWriter(System.out);

        int t=sc.nextInt();

        while(t>0){

            int n=sc.nextInt();
            long count=0;
            for(int i=0;i<n;i++){
                long x=sc.nextLong();
                count+=x/100;
                x=x%100;
                count+=x/50;
                x=x%50;
                count+=x/20;
                x=x%20;
                count+=x/10;
                x=x%10;
                count+=x/5;
                x=x%5;
                count+=x/3;
                x=x%3;
                count+=x/2;
                x=x%2;
                count+=x/1;
                x=x%1;
            }
            System.out.println(count);
            t--;
        }


    }
}
class InputReader
{
    private InputStream stream;
    private byte[] buf = new byte[1024];
    private int curChar;
    private int numChars;
    private SpaceCharFilter filter;

    public InputReader(InputStream stream)
    {
        this.stream = stream;
    }

    public int read()
    {
        if (numChars==-1)
            throw new InputMismatchException();

        if (curChar >= numChars)
        {
            curChar = 0;
            try
            {
                numChars = stream.read(buf);
            }
            catch (IOException e)
            {
                throw new InputMismatchException();
            }

            if(numChars <= 0)
                return -1;
        }
        return buf[curChar++];
    }

    public String nextLine()
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String str = "";
        try
        {
            str = br.readLine();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        return str;
    }
    public int nextInt()
    {
        int c = read();

        while(isSpaceChar(c))
            c = read();

        int sgn = 1;

        if (c == '-')
        {
            sgn = -1;
            c = read();
        }

        int res = 0;
        do
        {
            if(c<'0'||c>'9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        while (!isSpaceChar(c));

        return res * sgn;
    }

    public long nextLong()
    {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-')
        {
            sgn = -1;
            c = read();
        }
        long res = 0;

        do
        {
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        while (!isSpaceChar(c));
        return res * sgn;
    }

    public double nextDouble()
    {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        int sgn = 1;
        if (c == '-')
        {
            sgn = -1;
            c = read();
        }
        double res = 0;
        while (!isSpaceChar(c) && c != '.')
        {
            if (c == 'e' || c == 'E')
                return res * Math.pow(10, nextInt());
            if (c < '0' || c > '9')
                throw new InputMismatchException();
            res *= 10;
            res += c - '0';
            c = read();
        }
        if (c == '.')
        {
            c = read();
            double m = 1;
            while (!isSpaceChar(c))
            {
                if (c == 'e' || c == 'E')
                    return res * Math.pow(10, nextInt());
                if (c < '0' || c > '9')
                    throw new InputMismatchException();
                m /= 10;
                res += (c - '0') * m;
                c = read();
            }
        }
        return res * sgn;
    }

    public String readString()
    {
        int c = read();
        while (isSpaceChar(c))
            c = read();
        StringBuilder res = new StringBuilder();
        do
        {
            res.appendCodePoint(c);
            c = read();
        }
        while (!isSpaceChar(c));

        return res.toString();
    }

    public boolean isSpaceChar(int c)
    {
        if (filter != null)
            return filter.isSpaceChar(c);
        return c == ' ' || c == '\n' || c == '\r' || c == '\t' || c == -1;
    }

    public String next()
    {
        return readString();
    }

    public interface SpaceCharFilter
    {
        public boolean isSpaceChar(int ch);
    }
}
