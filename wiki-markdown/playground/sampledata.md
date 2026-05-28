Needs code update
<code>
diff -r M:\Toolbox\Dev\DokuWiki\csv plugin\table.php M:\Toolbox\Dev\DokuWiki\csv plugin\table.php.patched
92,94d91
<             if($line == 0 && $opt['hdr_rows'] > 0 ) {
<                 $renderer->tablethead_open();
<             }
134,136d130
<             if($line == $opt['hdr_rows'] - 1 ) {
<                 $renderer->tablethead_close();
<             }
</code>

<csv playground:2kWy2.csv></csv>