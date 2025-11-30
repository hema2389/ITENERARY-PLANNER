module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['./jest.setup.js'],
  moduleNameMapper: {
    '^firebase/app$': '<rootDir>/src/__mocks__/firebase/app.js',
    '^firebase/auth$': '<rootDir>/src/__mocks__/firebase/auth.js',
  },
};
