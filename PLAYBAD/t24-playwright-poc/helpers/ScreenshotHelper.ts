import { Page, TestInfo } from '@playwright/test';
import fs from 'node:fs/promises';
import path from 'node:path';

export type EvidenceStatus = 'PASSED' | 'FAILED' | 'BLOCKED' | 'SKIPPED';

export class ScreenshotHelper {
  private readonly outputDirectory = path.resolve(process.cwd(), 'screenshots');

  constructor(
    private readonly page: Page,
    private readonly testInfo: TestInfo
  ) {}

  async capture(
    testCaseId: string,
    stepNumber: number,
    description: string,
    status: EvidenceStatus
  ): Promise<string> {
    const step = stepNumber.toString().padStart(2, '0');
    const stamp = new Date().toISOString().replace(/[:.]/g, '');
    const fileName = `${this.clean(testCaseId)}_${step}_${this.clean(description)}_${status}_${stamp}.png`;
    await fs.mkdir(this.outputDirectory, { recursive: true });
    const outputPath = path.join(this.outputDirectory, fileName);
    await this.page.screenshot({ path: outputPath, fullPage: true });
    await this.testInfo.attach(fileName, { path: outputPath, contentType: 'image/png' });
    return outputPath;
  }

  private clean(value: string): string {
    return value.trim().replace(/\s+/g, '_').replace(/[^a-zA-Z0-9_-]/g, '') || 'N_A';
  }
}
