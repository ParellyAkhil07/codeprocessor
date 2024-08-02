import org.junit.runner.RunWith;
import org.mockito.junit.MockitoJUnitRunner;

import java.io.File;
import java.net.URL;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

@RunWith(MockitoJUnitRunner.class)
public class MavenWrapperDownloaderTest {

    @Test
    public void testDownloadFileFromURL() throws Exception {
        byte[] mockBytes = {1, 2, 3, 4, 5};
        URL mockUrl = mock(URL.class);
        when(mockUrl.openStream()).thenReturn(new java.io.ByteArrayInputStream(mockBytes));
        File tempFile = File.createTempFile("mock-file", ".jar");
        MavenWrapperDownloader.downloadFileFromURL(mockUrl.toString(), tempFile);
        byte[] downloadedBytes = java.nio.file.Files.readAllBytes(tempFile.toPath());
        assertArrayEquals(mockBytes, downloadedBytes);
        tempFile.delete();
    }

    @Test
    public void testMain() throws Exception {
        File tempDir = File.createTempFile("maven-wrapper-test", "");
        tempDir.delete();
        tempDir.mkdir();
        File propertiesFile = new File(tempDir, MavenWrapperDownloader.MAVEN_WRAPPER_PROPERTIES_PATH);
        propertiesFile.getParentFile().mkdirs();
        propertiesFile.createNewFile();
        String wrapperUrl = "https://example.com/mock-wrapper.jar";
        String propertiesContent = MavenWrapperDownloader.PROPERTY_NAME_WRAPPER_URL + "=" + wrapperUrl;
        java.nio.file.Files.write(propertiesFile.toPath(), propertiesContent.getBytes());
        String[] args = {tempDir.getAbsolutePath()};
        MavenWrapperDownloader.main(args);
        File outputFile = new File(tempDir, MavenWrapperDownloader.MAVEN_WRAPPER_JAR_PATH);
        assertTrue(outputFile.exists());
        tempDir.delete();
    }
