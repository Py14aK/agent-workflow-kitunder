import { defineConfig } from '@playwright/test';

const baseURL = process.env.T24_BASE_URL;

export default defineConfig({
  testDir: './tests',
  fullyParallel: false,
  workers: 1,
  timeout: 120_000,
  expect: { timeout: 20_000 },
  retries: 0,
  outputDir: './test-results',
  reporter: [
    ['list', { printSteps: true }],
    ['html', { outputFolder: './reports/html', open: 'never' }],
    ['json', { outputFile: './reports/json/results.json' }],
    ['junit', { outputFile: './reports/junit/results.xml' }]
  ],
  use: {
    baseURL,
    browserName: 'chromium',
    channel: 'msedge',
    headless: false,
    ignoreHTTPSErrors: true,
    actionTimeout: 20_000,
    navigationTimeout: 60_000,
    screenshot: 'only-on-failure',
    trace: 'retain-on-failure',
    video: 'off',
    viewport: { width: 1920, height: 1080 }
  },
  projects: [
    {
      name: 'T24-R21-SYT',
      use: { baseURL: process.env.T24_R21_URL ?? baseURL, channel: 'msedge' }
    },
    {
      name: 'T24-R26-SYT',
      use: { baseURL: process.env.T24_R26_URL ?? baseURL, channel: 'msedge' }
    }
  ]
});
