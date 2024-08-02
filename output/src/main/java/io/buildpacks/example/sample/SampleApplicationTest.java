  describe('main method', () => {
    it('should call the run method of the SpringApplication class', () => {
      const springApplication = {
        run: jest.fn()
      };
      const springApplicationConstructor = jest.fn().mockReturnValue(springApplication);
      const sampleApplication = new SampleApplication(springApplicationConstructor);
      sampleApplication.main(['args']);
      expect(springApplication.run).toHaveBeenCalledWith(SampleApplication, ['args']);
    });
  });
  describe('run method', () => {
    it('should start the application', () => {
      const springApplication = {
        run: jest.fn()
      };
      const springApplicationConstructor = jest.fn().mockReturnValue(springApplication);
      const sampleApplication = new SampleApplication(springApplicationConstructor);
      sampleApplication.run(['args']);
      expect(springApplication.run).toHaveBeenCalledWith(SampleApplication, ['args']);
    });
  });