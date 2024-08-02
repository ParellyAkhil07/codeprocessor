import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.fail;
import org.junit.Test;

public class MavenWrapperDownloaderTest {

    @Test
    public void testDownloadFileFromURL() {
        String url = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.2/maven-wrapper-0.4.2.jar";
        File destination = new File("maven-wrapper.jar");
        try {
            MavenWrapperDownloader.downloadFileFromURL(url, destination);
            assertTrue(destination.exists());
            assertTrue(destination.length() > 0);
        } catch (Exception e) {
            fail("Download failed: " + e.getMessage());
        }
    }

    @Test
    public void testDownloadFileFromInvalidURL() {
        String url = "https://invalid.url/maven-wrapper.jar";
        File destination = new File("maven-wrapper.jar");
        try {
            MavenWrapperDownloader.downloadFileFromURL(url, destination);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            assertTrue(e.getMessage().contains("Failed to connect"));
        }
    }

    @Test
    public void testDownloadFileFromURLInterrupted() {
        String url = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.2/maven-wrapper-0.4.2.jar";
        File destination = new File("maven-wrapper.jar");
        try {
            MavenWrapperDownloader.downloadFileFromURL(url, destination);
            fail("Expected exception not thrown");
        } catch (Exception e) {
            assertTrue(e.getMessage().contains("Download cancelled"));
        }
    }
