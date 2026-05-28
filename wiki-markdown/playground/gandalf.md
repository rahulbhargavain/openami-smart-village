### John's playground space
[Docuwiki](/wiki/docuwiki)

# Wiki contribution guide
The following standards should help keeping the wiki consistent, easy to understand for newbies, and easy to edit for casual contributors. There can be exceptions in some cases where it makes sense, but there should be a good reason for that.

{{section>meta:infobox:registration_disabled&noheader&nofooter&noeditbutton}}

## Mantras
- **Articles must be easy to read and easy to edit, simpler is better. ** Articles should be formatted only using basic features found in the editor GUI, plus the code tag and table construct where necessary.<br>
Why? More advanced formatting would give this wiki a more "professional" look, but it will also be harder to read and edit for casual users and contributors. More advanced layouts with tabs and buttons are more compact but are usually more confusing than a simpler layout with just a single list of actions and links where readers scroll through and click. Also a simple non-interactive layout allows easy printing. For example, look at this tutorial [Factory install: First-time installation on a device](/wiki/docs/guide-quick-start/factory_installation).

- **Avoid duplicating information within this wiki** : Information on the same topic shall appear in the wiki only ***once***  . If it is needed somewhere else, we refer to it with a link!<br>
For example if you are writing a tutorial and one of the step is "configure USB storage" you should link to [Using storage devices](/wiki/docs/guide-user/storage/usb-drives). DO NOT write down (or copy-paste) the same procedures in your new tutorial!<br>
<br>
- **Avoid duplicating upstream documentation** : consider contributing the more generic parts of the documentation to ***upstream***  , and just link to that in your article. This wiki exists for OpenWrt-related documentation, for example [Start](/wiki/docs/guide-user/network/ipv4/start). Some example upstream wikis: i.e. [Linux WiFi drivers wiki](https://wireless.wiki.kernel.org/), [OpenVPN Wiki](https://community.openvpn.net/openvpn/wiki) etc. Not all employ wikis, and not all accept contributions from third parties. If upstream contributions are impossible, then it's fine to have that info in the OpenWrt wiki.<br>
<br>
- **Versioning information**: the information in the articles should be valid for the ***current stable release***  . Information that applies **only** to older or snapshot releases (either deprecated or very new features) should be marked as such.<br>
<br>
- **Articles should be easy to find** most people will search for information with the search engine of their choice, or with the wiki's own internal search. Use short, descriptive titles and introductions that contain the right keywords to be found. You can try to search for your article with your favorite search engine (after a few days you posted the article, because search engines need time to update their indexes). If you won't find your own content, others probably won't as well!<br>
E.g. **installing.opkg.packages.in.mount.point.other.than.root** is a long title that could be replaced with something like *opkg – Installation Destinations*, but the latter will not be as easily be found as the first one when someone does not browse the wiki, but uses a search engine instead.<br>
<br>
- **Articles should explain why they exist, what is their goal**. Please add an "introduction" paragraph or two where you explain what is the feature you are configuring, and what needs can be satisfied by following the instructions. It does not need to be very verbose. For example, the first paragraph here: [Using the Image Generator (Image Builder)](/wiki/docs/guide-user/additional-software/imagebuilder)<br>
<br>
- **Articles should contain VERIFIABLE information, speculation should be clearly labeled as such**. Really, this is very important in any wiki. Cite sources for statements that aren't common knowledge, or write enough information to allow easy google searching for sources. For example: [USB 3.0 and WiFi problems](/wiki/docs/guide-user/network/wifi/usb3.0-wifi-issues)<br>
<br>
- **All tutorials you write must be tested personally or must have a warning** stating that testing was not possible when writing them (and to remove the warning when someone successfully tested it).<br>
<br>
- **One topic per article**. Articles should be focused on a single, focused topic, for example "**installing and configuring Adblock**". General articles that span many different topics, for example "**filtering web traffic**" (where you talk of Adblock, proxy servers, and maybe Tor and VPNs) should be split up.<br>
<br>
- **Large tutorials should be split up**. Large tutorials where each step is long should be split up in separate articles, each covering a part of the steps. This is even more important if the tutorial contains conditional or optional steps (for example: "do step **A**, then you can do either step **B** or **C**, then do **D**"). For example [Factory install: First-time installation on a device](/wiki/docs/guide-quick-start/factory_installation) or this ["Hello, world!" for OpenWrt](/wiki/docs/guide-developer/helloworld/start)<br>
<br>
- **Articles should be accessible from within the wiki** Please make sure your article has a link in one of the main Categories pages (links below) if it is some kind of tutorial. Some articles may not need this if they are part of a multi-article tutorial, but again make sure ALL articles can be reached either from the main Categories pages or from the other pages of its multi-article tutorial. Very popular articles will also be linked from within other tutorials, as explained in the **Avoid duplicating information within this wiki** mantra above. For a handy list of pages linking to the current page, click on the "**chain**" icon you find on the right tool panel (it's under the **clock** icon).
## Structure
To give the Wiki a better structure, we employ `namespaces` and `categories` (and `tags`):

* **Namespaces** are highest. In each of these upper namespaces, there shall be a maximum of 3 (three) sublevels. * *[about](/wiki/about/home)* about the OpenWrt project in general * *[TOH](/wiki/toh/home)*documentation about supported devices, called "Table of Hardware". * *[Packages](/wiki/packages/home)*documentation about available packages * *[Downloads](/wiki/downloads/home)*landing page to download firmware for your device * *[Documentation](/wiki/docs/home)*main documentation page * *[Wiki](/wiki/wiki/home)*pages about wiki functionality and wiki contribution rules * *[FAQ](/wiki/faq/home)*is the place for FAQ lists * *[Inbox](/wiki/inbox/start)*place pages here you are working on and which are not mature enough yet * *[Playground](/wiki/playground/playground)*is for trying out [wiki syntax](/wiki/wiki/syntax) or similar shortlived actions

* **Categories** provide the first level of the namespaces. They distinguish different kinds of **docs**: * *[Quick Start](/wiki/docs/guide-quick-start/start)*quick start tutorials, used for first installation and setup, or similar. * *[User Guide](/wiki/docs/guide-user/home)*most of the documentation for users goes here * *[Developer Guide](/wiki/docs/guide-developer/home)*developer documentation

* **Tags** are different. While the structure is exclusive, you can place an article only in one subcategory, tags are more flexible. More of them can be placed simultaneously in one article, and thus allow for a more flexible categorizing. To reproduce this with the structure we could write symbolic articles, which are placed in different subcategories and redirect to one article. But let's not do that. Tags will prove most useful, when you want to search for routers with certain features. * [Tags](/wiki/meta/tags) Overview To ease navigation, we use a [sidebar](/wiki/sidebar/home)

