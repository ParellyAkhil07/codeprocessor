
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class SampleApplicationTests {

    @Test
    public void contextLoads() {
    }

    @Test
    public void testAdd() {
        assertEquals(3, 1 + 2);
    }

    @Test
    public void testSubtract() {
        assertEquals(1, 3 - 2);
    }

    @Test
    public void testMultiply() {
        assertEquals(6, 2 * 3);
    }

    @Test
    public void testDivide() {
        assertEquals(2, 6 / 3);
    }
