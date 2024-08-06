public void testMain() throws Exception {
    File baseDirectory = new File("path/to/base/directory");
    File mavenWrapperPropertiesFile = new File(baseDirectory, MavenWrapperDownloader.MAVEN_WRAPPER_PROPERTIES_PATH);
    if (!mavenWrapperPropertiesFile.exists()) {
        mavenWrapperPropertiesFile.createNewFile();
    }
    File mavenWrapperJarFile = new File(baseDirectory, MavenWrapperDownloader.MAVEN_WRAPPER_JAR_PATH);
    if (!mavenWrapperJarFile.exists()) {
        mavenWrapperJarFile.createNewFile();
    }
    MavenWrapperDownloader.main(new String[] {baseDirectory.getAbsolutePath()});
    assertTrue(mavenWrapperJarFile.exists());