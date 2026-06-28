const puppeteer = require('puppeteer');
const path = require('path');
const fs = require('fs');

process.on('unhandledRejection', (reason) => {
  console.warn('Note: Asynchronous promise rejection (ignored):', reason);
});
process.on('uncaughtException', (err) => {
  console.warn('Note: Asynchronous exception (ignored):', err.message);
});

(async () => {
  const execPath = 'C:\\Users\\rhlbh\\.cache\\puppeteer\\chrome\\win64-150.0.7871.24\\chrome-win64\\chrome.exe';
  const htmlPath = path.resolve(__dirname, 'reports', 'openami-amda-pitch-print.html');
  const pdfPath  = path.resolve(__dirname, 'reports', 'openami-amda-pitch.pdf');

  console.log('Launching browser at:', execPath);
  const browser = await puppeteer.launch({
    executablePath: execPath,
    headless: 'new',
    userDataDir: path.resolve(__dirname, '.chrome-profile'),
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--disable-gpu',
      '--no-first-run',
      '--run-all-compositor-stages-before-draw',
      '--disable-features=VizDisplayCompositor'
    ]
  });

  console.log('Browser launched. Opening page...');
  const page = await browser.newPage();

  const fileUrl = 'file:///' + htmlPath.replace(/\\/g, '/');
  console.log('Navigating to:', fileUrl);
  await page.goto(fileUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });

  // Wait for fonts/layout
  await new Promise(r => setTimeout(r, 2000));

  console.log('Generating PDF...');
  await page.pdf({
    path: pdfPath,
    format: 'A4',
    printBackground: true,
    margin: { top: '0mm', right: '0mm', bottom: '0mm', left: '0mm' }
  });

  try {
    await browser.close();
  } catch (err) {
    console.warn('Note: Browser closed with cleanup warning:', err.message);
  }

  const stats = fs.statSync(pdfPath);
  console.log('PDF saved to:', pdfPath);
  console.log('File size:', Math.round(stats.size / 1024) + ' KB');
})().catch(err => {
  console.error('FAILED:', err.message);
  process.exit(1);
});
