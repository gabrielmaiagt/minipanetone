let chromium;
try { ({ chromium } = require('playwright')); }
catch { ({ chromium } = require('/tmp/mini-panetone-qa/node_modules/playwright')); }
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
(async () => {
  const chromePath = process.env.CHROME_PATH || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const browser = await chromium.launch({ headless: true, ...(fs.existsSync(chromePath) ? { executablePath: chromePath } : {}) });
  const page = await browser.newPage();
  await page.goto('http://127.0.0.1:8010/app/', { waitUntil: 'networkidle' });
  const svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="#173f5b"/><g transform="translate(106 90) scale(12.5)" fill="none" stroke="#fff7e9" stroke-width="1.25" stroke-linecap="round" stroke-linejoin="round"><path d="M6 14a5 5 0 0 1-1-10 5 5 0 0 1 8-1 5 5 0 1 1 5 11v7H6v-7ZM6 17h12"/></g></svg>';
  for (const size of [192, 512]) {
    const data = await page.evaluate(async ({ svg, size }) => {
      const img = new Image(); img.src = 'data:image/svg+xml;base64,' + btoa(svg); await img.decode();
      const canvas = document.createElement('canvas'); canvas.width = size; canvas.height = size;
      canvas.getContext('2d').drawImage(img, 0, 0, size, size); return canvas.toDataURL('image/png').split(',')[1];
    }, { svg, size });
    fs.writeFileSync(path.join(root, `icon-${size}.png`), Buffer.from(data, 'base64'));
  }
  const files = ['80-receitas','biscoitos-natal','sobremesas-copinhos','guia-decoracoes','guia-embalagens','guia-vendas','tags-natal'];
  for (const file of files) {
    await page.goto(`http://127.0.0.1:8010/app/downloads/${file}.html`, { waitUntil: 'networkidle' });
    await page.evaluate(async () => { await Promise.all([...document.images].map(i => i.decode())); });
    await page.pdf({ path: path.join(root, 'downloads', `${file}.pdf`), format: 'A4', printBackground: true, preferCSSPageSize: true, displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: '<div style="width:100%;font-size:8px;text-align:center;color:#80909b;font-family:Arial">MINHA COZINHA • MINI PANETONES <span style="margin-left:20px" class="pageNumber"></span> / <span class="totalPages"></span></div>' });
    console.log(file, fs.statSync(path.join(root,'downloads',`${file}.pdf`)).size);
  }
  await browser.close();
})().catch(err => { console.error(err); process.exit(1); });
