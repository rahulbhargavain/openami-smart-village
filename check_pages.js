const fs = require('fs');
const path = require('path');

const pdfPath = path.resolve(__dirname, 'reports', 'powerafrica-2026-flyer.pdf');
const data = fs.readFileSync(pdfPath);
const dataString = data.toString('latin1');

// Match page objects in PDF
const pageCount = (dataString.match(/\/Type\s*\/Page\b/g) || []).length;
console.log('PDF Page Count:', pageCount);
if (pageCount !== 1) {
  console.error('WARNING: PDF is not exactly 1 page! It has ' + pageCount + ' pages.');
  process.exit(1);
} else {
  console.log('SUCCESS: PDF is exactly 1 page.');
}
