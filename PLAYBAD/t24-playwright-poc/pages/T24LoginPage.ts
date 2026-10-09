import { expect, Locator, Page } from '@playwright/test';

export interface T24LoginSelectors {
  username: string;
  password: string;
  submitButton?: string;
  successfulLoginIndicator: string;
  loginError?: string;
  loginFrame?: string;
}

export class T24LoginPage {
  constructor(
    private readonly page: Page,
    private readonly selectors: T24LoginSelectors
  ) {}

  private locate(selector: string): Locator {
    return this.selectors.loginFrame
      ? this.page.frameLocator(this.selectors.loginFrame).locator(selector)
      : this.page.locator(selector);
  }

  async open(): Promise<void> {
    await this.page.goto('/');
  }

  async enterUsername(username: string): Promise<void> {
    const field = this.locate(this.selectors.username);
    await expect(field).toBeVisible();
    await expect(field).toBeEnabled();
    await field.fill(username);
  }

  async enterPassword(password: string): Promise<void> {
    const field = this.locate(this.selectors.password);
    await expect(field).toBeVisible();
    await expect(field).toBeEnabled();
    await field.fill(password);
  }

  async submitLogin(): Promise<void> {
    if (this.selectors.submitButton) {
      const button = this.locate(this.selectors.submitButton);
      await expect(button).toBeVisible();
      await expect(button).toBeEnabled();
      await button.click();
      return;
    }
    await this.locate(this.selectors.password).press('Enter');
  }

  async login(username: string, password: string): Promise<void> {
    await this.enterUsername(username);
    await this.enterPassword(password);
    await this.submitLogin();
  }

  async verifyLoginSucceeded(): Promise<void> {
    await expect(this.locate(this.selectors.successfulLoginIndicator)).toBeVisible();
  }

  async getLoginError(): Promise<string | null> {
    if (!this.selectors.loginError) return null;
    const error = this.locate(this.selectors.loginError);
    if (!(await error.isVisible())) return null;
    return (await error.textContent())?.trim() ?? null;
  }
}
