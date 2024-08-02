import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class MavenWrapperDownloaderTest {
    @Test
    public void testDownloadFileFromURL() throws Exception {
        String urlString = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.2/maven-wrapper-0.4.2.jar";
        File tempFile = File.createTempFile("maven-wrapper", ".jar");
        MavenWrapperDownloader.downloadFileFromURL(urlString, tempFile);
        assertEquals(true, tempFile.exists());
        tempFile.delete();
    }