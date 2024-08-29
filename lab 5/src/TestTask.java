import java.util.Calendar;
import java.util.Timer;
import java.util.TimerTask;

public class TestTask {
    public static void main(String[] args) {
        Timer T = new Timer();
        TimerTask birthday = new TimerTask() {
            @Override
            public void run() {
                System.out.println("Happy Birthday!!!");
            }
        };

        Calendar date = Calendar.getInstance();
        date.set(2023, Calendar.AUGUST, 17, 0, 0, 0); 
        T.schedule(birthday, date.getTime());
    }
}
