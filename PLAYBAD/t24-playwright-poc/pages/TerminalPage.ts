import { expect, Locator, Page } from '@playwright/test';

export interface TerminalSelectors {
  commandLine: string;
  terminalFrame?: string;
  targetScreenIndicator?: string;
  commandError?: string;
}

export class TerminalPage {
  constructor(
    private readonly page: Page,
    private readonly selectors: TerminalSelectors
  ) {}

  private locate(selector: string): Locator {
    return this.selectors.terminalFrame
      ? this.page.frameLocator(this.selectors.terminalFrame).locator(selector)
      : this.page.locator(selector);
  }

  private commandLine(): Locator {
    return this.locate(this.selectors.commandLine);
  }

  async enterCommand(command: string): Promise<void> {
    if (!command.trim()) throw new Error('The T24 command cannot be empty.');
    const field = this.commandLine();
    await expect(field).toBeVisible();
    await expect(field).toBeEnabled();
    await field.fill(command);
  }

  async submitCommand(): Promise<void> {
    await this.commandLine().press('Enter');
  }

  async executeCommand(command: string): Promise<void> {
    await this.enterCommand(command);
    await this.submitCommand();
  }

  async waitForTargetScreen(): Promise<void> {
    if (!this.selectors.targetScreenIndicator) {
      throw new Error('No target-screen selector has been configured.');
    }
    await expect(this.locate(this.selectors.targetScreenIndicator)).toBeVisible();
  }

  async getCommandError(): Promise<string | null> {
    if (!this.selectors.commandError) return null;
    const error = this.locate(this.selectors.commandError);
    if (!(await error.isVisible())) return null;
    return (await error.textContent())?.trim() ?? null;
  }
}
