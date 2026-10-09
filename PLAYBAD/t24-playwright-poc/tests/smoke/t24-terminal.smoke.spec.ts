import { expect, test } from '@playwright/test';
import { T24LoginPage, T24LoginSelectors } from '../../pages/T24LoginPage';
import { TerminalPage, TerminalSelectors } from '../../pages/TerminalPage';
import { ScreenshotHelper } from '../../helpers/ScreenshotHelper';

const testCaseId = 'T24-SMOKE-001';

// TODO: Replace every TODO selector with a proven selector from the working KHN test.
const loginSelectors: T24LoginSelectors = {
  username: 'TODO_USERNAME_SELECTOR',
  password: 'TODO_PASSWORD_SELECTOR',
  submitButton: 'TODO_LOGIN_BUTTON_SELECTOR',
  successfulLoginIndicator: 'TODO_SUCCESSFUL_LOGIN_INDICATOR'
  // loginFrame: 'TODO_LOGIN_FRAME_SELECTOR',
  // loginError: 'TODO_LOGIN_ERROR_SELECTOR'
};

const terminalSelectors: TerminalSelectors = {
  commandLine: 'TODO_COMMAND_LINE_SELECTOR',
  targetScreenIndicator: 'TODO_TARGET_SCREEN_INDICATOR'
  // terminalFrame: 'TODO_TERMINAL_FRAME_SELECTOR',
  // commandError: 'TODO_COMMAND_ERROR_SELECTOR'
};

test('logs in and executes a safe enquiry command', async ({ page }, testInfo) => {
  const username = process.env.T24_INPUT_USERNAME;
  const password = process.env.T24_INPUT_PASSWORD;
  const command = process.env.T24_SMOKE_COMMAND ?? 'ENQ TXN.ENTRY';

  if (!username || !password) {
    throw new Error('Configure T24_INPUT_USERNAME and T24_INPUT_PASSWORD locally.');
  }

  const login = new T24LoginPage(page, loginSelectors);
  const terminal = new TerminalPage(page, terminalSelectors);
  const evidence = new ScreenshotHelper(page, testInfo);

  await test.step('Open T24', async () => {
    await login.open();
    await evidence.capture(testCaseId, 1, 'T24Opened', 'PASSED');
  });

  await test.step('Log in', async () => {
    await login.login(username, password);
    await login.verifyLoginSucceeded();
    expect(await login.getLoginError()).toBeNull();
    await evidence.capture(testCaseId, 2, 'Login', 'PASSED');
  });

  await test.step('Execute terminal command', async () => {
    await terminal.executeCommand(command);
    await terminal.waitForTargetScreen();
    expect(await terminal.getCommandError()).toBeNull();
    await evidence.capture(testCaseId, 3, 'CommandExecution', 'PASSED');
  });
});
