## =Guestbook
## New Comment
<form>
action pagemod _self add_comment
fieldset "Write new comment"
textbox  "Name" /^((?!<\/nowiki>).)*$/
email "Email (optional)" /^((?!<\/nowiki>).)*$/ !
textarea "Comment" /^((?!<\/nowiki>).|\n)*$/
submit
</form>

## Comments
<pagemod add_comment output_after>
*@@meta.date.format.r@@:*
| <nowiki>@@Name@@</nowiki> |<nowiki>@@Email (optional)| @@</nowiki>| |
| --- |
| <nowiki>@@Comment@@</nowiki> |  |
</pagemod>
*Tue, 23 Jul 2024 13:30:32 +0000:*
| <nowiki>Anonymous</nowiki> |<nowiki> </nowiki>| |
| --- |
| <nowiki>Just checking</nowiki> |  |
