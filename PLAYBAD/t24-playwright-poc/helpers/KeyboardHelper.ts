import { Page } from '@playwright/test';

export class KeyboardHelper {
  constructor(private readonly page: Page) {}

  async pressFunctionKey(number: number): Promise<void> {
    if (!Number.isInteger(number) || number < 1 || number > 12) {
      throw new Error(`Invalid function key F${number}; expected F1-F12.`);
    }
    await this.page.keyboard.press(`F${number}`);
  }

  async pressEnter(): Promise<void> { await this.page.keyboard.press('Enter'); }
  async pressTab(): Promise<void> { await this.page.keyboard.press('Tab'); }
  async pressShiftTab(): Promise<void> { await this.page.keyboard.press('Shift+Tab'); }
  async pressEscape(): Promise<void> { await this.page.keyboard.press('Escape'); }
}
