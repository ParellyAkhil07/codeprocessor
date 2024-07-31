java
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.fail;
import org.junit.Test;
import java.io.File;

public class MavenWrapperDownloaderTest {

    @Test
    public void testMain() {
        // Test the main method with valid arguments
        String[] args = { "my_base_directory" };
        MavenWrapperDownloader.main(args);
        File baseDirectory = new File("my_base_directory");
        File mavenWrapperPropertyFile = new File(baseDirectory, MavenWrapperDownloader.MAVEN_WRAPPER_PROPERTIES_PATH);
        File mavenWrapperJarFile = new File(baseDirectory, MavenWrapperDownloader.MAVEN_WRAPPER_JAR_PATH);
        assertTrue("Base directory should exist", baseDirectory.exists());
        assertTrue("Maven wrapper properties file should exist", mavenWrapperPropertyFile.exists());
        assertTrue("Maven wrapper JAR file should exist", mavenWrapperJarFile.exists());

        // Test the main method with invalid arguments
        args = new String[] {};
        try {
            MavenWrapperDownloader.main(args);
            fail("Expected an exception to be thrown");
        } catch (Exception e) {
            assertEquals("Expected exception message", "Invalid arguments", e.getMessage());
        }
    }

    @Test
    public void testDownloadFileFromURL() {
        // Test the downloadFileFromURL method with valid arguments
        String urlString = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.4.2/maven-wrapper-0.4.2.jar";
        File destination = new File("maven-wrapper.jar");
        try {
            MavenWrapperDownloader.downloadFileFromURL(urlString, destination);
            assertTrue("Destination file should exist", destination.exists());
        } catch (Exception e) {
            fail("Unexpected exception: " + e.getMessage());
        }

        // Test the downloadFileFromURL method with invalid arguments
        urlString = "https://invalid_url.com";
        destination = new File("invalid_destination.jar");
        try {
            MavenWrapperDownloader.downloadFileFromURL(urlString, destination);
            fail("Expected an exception to be thrown");
        } catch (Exception e) {
            assertEquals("Expected exception message", "Unable to download file from URL: " + urlString, e.getMessage());
        }
    }
}