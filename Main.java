import java.util.stream.Stream;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.IOException;
import java.nio.charset.Charset;


public class Main {
    public static void main(String[] args) {
        
try (Stream<String> stream = Files.lines(Paths.get("input.txt"),Charset.defaultCharset())) {
    stream.iterate();
 } 
catch(IOException ex){}
}}
