# HOWTO
A user-friendly guide to adding and editing content on the IEEE Smart Village DokuWiki.


<div class="pdf-card">
  <span class="pdf-icon">📄</span>
  <div class="pdf-info">
    <div class="pdf-title">Howto.Pdf|?Page-Width</div>
    <a href="/media/playground/howto.pdf|?page-width" class="pdf-btn" target="_blank">View / Download PDF Manual</a>
  </div>
</div>


### Getting Started: Creating a New Page
**Search for your page title**: The easiest way to create a new page is to first search for the title you have in mind. If the page doesn't exist, you can create it.

**Use the search bar**: Type your desired page title into the search bar and press Enter.

**Create the page**: If the page doesn't exist, you'll see a "This topic does not exist yet" message. Click the "Create this page" button to open the editor.

### Editing an Existing Page
To edit a page you are currently viewing, look for an "Edit this page" button or link. This will open the page in the editor, allowing you to make changes.

### Basic Formatting
DokuWiki uses a simple markup language to format text. Here are some of the most common formatting options.

**Bold and Italic**:

For **bold** text, wrap it in double asterisks: `%%**text**%%`

For *italic* text, wrap it in double slashes: `%%*text*%%`

For **underlined** text, wrap it in double underscores: `%%<u>text</u>%%`

**Headlines**: Use the equals sign = to create headlines. More equals signs create smaller headlines.
<code>
# Large Heading
## Medium Heading
### Small Heading
</code>

**Lists**:

**Unordered Lists**: To create a bulleted list, indent your text with two spaces and use an asterisk * for each item.

**Ordered Lists**: To create a numbered list, indent your text with two spaces and use a hyphen - for each item.

### Creating Links
**Internal Links**: To link to another page within the wiki, use double square brackets.

`%%[Page Name](/wiki/page_name)%%` will create a link to "page_name".

`%%[link text](/wiki/page_name)%%` will create a link to "page_name" with the text "link text".

**External Links**: To link to an external website, simply paste the full URL.

`%%http://www.example.com%%` will create a link to that URL.

`%%[link text](http://www.example.com)%%` will create a link with custom text.

### Adding Images
**Upload the image**: Click the "Media Manager" button to upload your image file.

**Embed the image**: To embed an image into a page, use double curly braces.

`%%<img src="/media/image.jpg" class="wiki-image" alt="Embedded Image">%%`

### Saving Your Work
Once you are finished editing, you will see a "Save" button. Click this to save your changes. It's a good practice to also use the "Preview" button to see how your changes will look before saving.

Here is a guide on how to embed PDFs and import content from Microsoft Word files into your DokuWiki pages.

### Embedding PDF Files
While DokuWiki doesn't natively display PDFs directly on the page, you can link to them. A common way to embed a PDF is by using the pdfjs plugin, which displays the PDF in a viewer within the wiki page.

**Upload the PDF**: First, use the "Media Manager" to upload your PDF file to the wiki.

**Embed the File**: To embed the uploaded PDF, insert the following syntax into your page, replacing your_file.pdf with the name of your uploaded file: `%%
<div class="pdf-card">
  <span class="pdf-icon">📄</span>
  <div class="pdf-info">
    <div class="pdf-title">Your File.Pdf</div>
    <a href="/media/your_file.pdf" class="pdf-btn" target="_blank">View / Download PDF Manual</a>
  </div>
</div>
%%`

This will display the PDF with a default width of 100% and a height of 300px.

**Customizing the Viewer Size**

You can customize the height and width of the PDF viewer.

To set only the height (e.g., to 500 pixels): `%%
<div class="pdf-card">
  <span class="pdf-icon">📄</span>
  <div class="pdf-info">
    <div class="pdf-title">Your File.Pdf|500</div>
    <a href="/media/your_file.pdf|500" class="pdf-btn" target="_blank">View / Download PDF Manual</a>
  </div>
</div>
%%`

To set both width and height (e.g., 800 pixels wide by 600 pixels high): `%%
<div class="pdf-card">
  <span class="pdf-icon">📄</span>
  <div class="pdf-info">
    <div class="pdf-title">Your File.Pdf|800,600</div>
    <a href="/media/your_file.pdf|800,600" class="pdf-btn" target="_blank">View / Download PDF Manual</a>
  </div>
</div>
%%`

### Adding Content from Microsoft Word
When dealing with content from .docx files, especially troublesome ones, you can use the "Paste from Word" feature available in the CKEditor.

**Using the "Paste from Word" Button**

**Copy from Word**: Select and copy the content from your Microsoft Word document.

**Click in the Editor**: In the DokuWiki editor, you must first click inside the text window where you want the content to go.

**Paste from Word**: Locate the "Paste from Word" button on the far right of the CKEditor toolbar and click it. This will open a dialog box.

**Paste and Insert**: Paste your content into the text window of the dialog box and click "OK."

**Limitations and Tips**

Be aware of the following limitations when pasting from Word:

**Basic Lists Only**: The tool currently has basic support for lists.

Only one list can be inserted at a time.

Nested (multi-level) lists are not supported.

**Cleaning Complex Lists**: For complex lists, it is best to paste them directly into the main CKEditor window first. Then, select the pasted list with your mouse and open the "Paste from Word" dialog. The list will load into the text window, and clicking "OK" will clean up the formatting for DokuWiki.

**Precise Selections**: For both lists and tables, try to make your selection as exact as possible in the Word document before copying.
