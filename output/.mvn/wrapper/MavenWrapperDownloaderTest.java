import static org.junit.Assert.fail;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.net.URL;
import java.nio.channels.Channels;
import java.nio.channels.ReadableByteChannel;
import java.util.Properties;

import org.junit.Test;

public class MavenWrapperDownloaderTest {

    @Test
    public void testMain() {
        File baseDirectory = new File("test-dir");
        baseDirectory.mkdir();
        File mavenWrapperPropertyFile = new File(baseDirectory, MavenWrapperDownloader.MAVEN_WRAPPER_PROPERTIES_PATH);
        Properties mavenWrapperProperties = new Properties();
        mavenWrapperProperties.put(MavenWrapperDownloader.PROPERTY_NAME_WRAPPER_URL, "https://example.com/maven-wrapper.jar");
        try {
            mavenWrapperPropertyFile.createNewFile();
            FileOutputStream fos = new FileOutputStream(mavenWrapperPropertyFile);
            mavenWrapperProperties.store(fos, "Test properties");
            fos.close();

            MavenWrapperDownloader.main(new String[] { baseDirectory.getAbsolutePath() });

            File mavenWrapperJarFile = new File(baseDirectory, MavenWrapperDownloader.MAVEN_WRAPPER_JAR_PATH);
            assertTrue(mavenWrapperJarFile.exists());
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }

    @Test
    public void testDownloadFileFromURL() {
        URL url = mock(URL.class);
        ReadableByteChannel readableByteChannel = mock(ReadableByteChannel.class);
        when(url.openStream()).thenReturn(Channels.newInputStream(readableByteChannel));
        File destination = new File("destination.txt");
        try {
            MavenWrapperDownloader.downloadFileFromURL("https://example.com", destination);
            FileInputStream fis = new FileInputStream(destination);
            fis.close();
        } catch (Exception e) {
            fail(e.getMessage());
        }
    }
