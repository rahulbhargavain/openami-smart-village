# Plugins
1. Export DokuWiki content to PDF
1. Create a DokuWiki page by importing an ODT file
1. NavBox brings the core functionality of the NavBox from Wikipedia (and MediaWiki) across to DokuWiki
1. backup
1. bureaucracy & pagemod
1. <del>gchart</del>
1. <del>Google Authentication Plugin allows to sign in to DokuWiki using OAuth 2.0</del>
1. Adds a legal (or other) notice below the login form
1. Create a DokuWiki page from a file
1. Displays a CSV file, or inline CSV data, as a table
1. Show PDF files using PDF.js
1. [https://github.com/nomadjimbob/mikioplugin/wiki](https://github.com/nomadjimbob/mikioplugin/wiki)

## Developer warning
<note warning>CSV MIME type text/csv has been enabled</note>

## Sample data
<note tip>Inline CSV</note> <csv playground:2kWy2.csv></csv>

## Datatable with include
<datatable page-length="20">

{{page>playground:sampledata}}

</datatable>

## ApexCharts
<note tip>ApexCharts: only one y-axis is supported from CSV via JSON conversion in PHP</note>

<achart url=[https://gist.github.com/karl257/6e799cc0d8a5e47ac11d97672a6890dc/raw/0a80ea7ff3b89d0f376aec0eff0d817550b32334/convertcsv.csv](https://gist.github.com/karl257/6e799cc0d8a5e47ac11d97672a6890dc/raw/0a80ea7ff3b89d0f376aec0eff0d817550b32334/convertcsv.csv) height=320px align=center> {

chart: {
    height: 350,
    type: 'line',
},
stroke: {
  width: 2,
  curve: "smooth"
},
dataLabels: {
    enabled: false
},
title: {
    text: "From web",
}


} </achart>

<achart url=:playground:2kWy2.csv height=320px align=center> {

chart: {
    height: 350,
    type: 'line',
},
yaxis: [
  {
    title: {
      text: "Production"
    },
  },
  {
    opposite: true,
    title: {
      text: "Yield"
    }
  }
],
stroke: {
  width: 2,
  curve: "smooth"
},
dataLabels: {
    enabled: true
},
xaxis: {
     type: 'datetime'
},
legend: {
    position: 'top'
},
title: {
    text: "Production (kWh)",
}
} </achart>

<achart url=:playground:2kWy2.csv height=320px align=center> {

chart: {
    height: 350,
    type: 'bar',
},
dataLabels: {
    enabled: true
},
  xaxis: {
     type: 'datetime'
},
legend: {
    position: 'top'
},
title: {
    text: "Production (kWh), Yield",
}

} </achart>

## Placeholder text
[hypothetical layout](/wiki/playground/hypothetical_layout)

[Decentralized Renewable Energy](/wiki/playground/decentralized_renewable_energy)

[Leverage](/wiki/playground/leverage)

[Standards](/wiki/playground/standards)


<div class="pdf-card">
  <span class="pdf-icon">📄</span>
  <div class="pdf-info">
    <div class="pdf-title">Techsawg.Pdf</div>
    <a href="/media/playground/techSAWG.pdf" class="pdf-btn" target="_blank">View / Download PDF Manual</a>
  </div>
</div>


