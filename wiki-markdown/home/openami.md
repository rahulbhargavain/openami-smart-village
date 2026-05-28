# Open AMI
### Open-Source Advanced-Metering-Infrastructure to enable minigrids for electricity access.
`Note: This page is actively under construction and will be updated frequently. Last update: Akash Borde, 28 October 2025`
## Background:
* [Power Africa Conference Presentation](https://docs.google.com/presentation/d/1b1Bl63I-evfd20MW6XxDe0IIse-0Nm85/edit?usp=sharing&ouid=112191662511889552544&rtpof=true&sd=true)
* [Linux Foundation Conference Presentation](https://docs.google.com/presentation/d/1b1Bl63I-evfd20MW6XxDe0IIse-0Nm85/edit#slide=id.g28b247f5353_0_91)

## Ongoing:
* There is a weekly meeting actively discussing and shaping this project. This takes places from 630-730am US Pacific Time on Wednesdays.
* Contact Product Manager for more details: Akash Borde at borde.akash[at]gmail.com

## Weekly Meeting Notes:
`(I am struggling to figure out why the formatting breaks so badly, will work on figuring this format out… -Akash)`

There are two embedded editors, a WYSIWYG editor that is the default that applies its own markup and a DokuWiki Editor that requires tags for all markup. Pages can also be created from Word Docx or ODT uploads that plugins convert to Wikipages. I got Google Gemini 2.5 Pro to re-format to Wiki format. Please review and check that nothing was omitted.

## 29 Oct 2025
1)
 [5 minutes] Logistics: Akash, (+Adam, Rajan, if available).
 Proposed to move meeting 30 minutes later - no objections from people on call
 2)
 [15 minutes] Current Problem Statement: Akash, Jude, Rahul
 Summarizing the problem as we understand it and having the team review it. Documenting this as the top item on the wiki. Short-term problems, long-term problems, and major pain points.
 Jude proposal: (link):
 Solution
 The proposed solution is to establish an OpenAMI Association, a multi-stakeholder initiative that will develop, test, and promote a universal communications and interoperability standard for smart metering systems in Africa.
1. Should allow remote monitoring
1. Should allow controls (remote start/stop)
 Rahul:
1. HES is customized from the OEM by utilities, it's not proprietary
 ○ EU has strict guidelines on open and proprietary
1. Size of group is too small, need backing from large institutions (e.g. World Bank)
 ○ Jude: Disagree - this is a very large problem. STS was created for the same reason
 ○ We can promote this standard to the OEMs. AMDA and World Bank are coming to us
 ○ StemaCo - willing to give us keys (showed interest)
1. Plan for getting OEMs to participate
 ○ Drive demand - if the meters don't have OpenAMI certification, the minigrids won't buy
 ○ Use AMDA and WorldBank for leverage
1. Rahul: Getting keys shouldn't be hard - manufacturers have not said no yet
 ○ Concerned about getting large enough to drive adoption. STS was created by large multinationals
1. Create a reference that the minigrid developers adopt
1. Don:
 ○ Could we reach out to OEM's about Jude's idea and get feedback about this concept? Or are we saying if we create something that is certified by World Bank and AMDA they will be forced to accept our certified standard?
 3)
 [10 minutes] Update on vendor relations: Rahul, Rajan, Jude, Michel
1. 
 Any updates from Donsun, Sparkmeter, EarthSpark
 Leeks has started saying that Donsun is still active (inaccurate)
 Donsun has split into two - China and Rest-of-Worl
1. 
 Asks from StemacoVP, who presented at Thursday ISV Bi-Weekly call
 Willing to help out
 ISV has a commercial relationship with them already.
 StemaCo is moving away from Donsun
 Any progress opening up DLMS Cosem yet?
 Glenn to follow up with this person - Warren Scott White → will contact Sam (tech lead) at Stemaco
1. 
 How is AMDA doing? Are they tracking this project?
1. 
 Inhemeter: Inhemeter has requested some documents, NDA, MoU to continue working with them. Do we want to continue this at this time? Michel started drafting docs if so.
1. 
 Not a no, but we need a better strategy
1. 
 OEMs don't want to work with our group b/c we are too small
1. 
 Work through GVE?
 ○ They are also very small and use legacy meters only
1. 
 Challenge is if we use INHE-5000 now, Inhemeter will not support the next version
 Glenn:
1. Would be great if we can create a DCU that supports DLMS Cosem and non-DLMS protocols that is compatible with edge meters
1. Getting backing from Stemaco for OpenAMI would be great
1. Can we get ISV to support the creation of OpenAMI consortium?
 4)
 [15 minutes] Engineering development: Rahul, Glenn, Akash, Jude, Adam
 People with source code - Adam, Vivien, Rahul, Glenn - can you walk us through what's been read, what's pending, etc?
 Akash - no updates on MeshEMS still :(. Would it be useful for Cameroon lab? Energy IoT open source has requested it for January.
 Is there funding for hardware manufacturing?
 Jude - OpenAMI and other standards. Do we want to get into STS and try to replicate it for Metering/Vending?
 5)
 [10 minutes] All: Assignments for next week / planning ahead
 Glenn - talk to the contact at StemaCo (Sam) → will discuss opening up DLMS protocol
 Don - we need to update our document for OpenAMI
 Continue discussion on "ISV AMI Subcomittee" whatsapp group
 Glenn may come to Cameroon early January


### October 22nd, 2025:
Follow-ups

* Rahul weekly meeting? Meeting delayed, follow-up email to team sent today. — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:10*
* Stemaco and Donsun relationship? Donsun is splitting into two, with Synergy serving the global market, particularly African STS compliant hardware and a much more competitive (in terms of entrenchment and margins) Chinese domestic market. It is believed that the African market will continue to be served by Leets+Synergy. — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:12*
* Vivian hardware access?
* Sparkmeter source code access?
* EnAccess made introductions and the Emerging Markets codebase on gitlab is accessible to Glenn and Rahul, aside from EnAccess. Though, while there is no clarity on licensing and ownership, it is generally unadvisable to use the code. — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:14*

Logistics - Akash will make a new email series, including Jude. Agendas will be sent 24 hrs in advance over email.

* Whatsapp: - OpenAMI Coms Integration → Inhemeter
* Pending with Inhe who are expected to furnish REIc with a NDA and contract before sharing any doucmentation, let alone code stubs for querying meters from the DCU (only 5000 series, no legacy support). Meanwhile, SteamaCo is committing to provide legacy support including code. — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:15*
* Tech Comm and OpenAMI → used for presentations
* ISV AMI Subcommittee
* Arila is not on Whatsapp
* Ask Rajan if he wants the weekly emails

1) Any updates from the crowd – Donsun, Sparkmeter, EarthSpark current state Rahul + Daniel - SparkMeter has been "handed over" to EarthSpark after SparkMeter collapsed. Allison is the president of EarthSpark. She makes the call if/when SparkMeter becomes Open-Sourced. Vivien is the guy leading the open-source effort. Sparkmeter's operating costs are artificially very high. Sparkmeter wraps the cailin's hardware in their own protocol (SparkMeter replace the radios with their own and run custom firmware without STS; so legacy meters cannot be orchestrated by new DCUs and no one can participate on their private neighbourhood networks without matching radios and protocols). — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:17*  Worldbank M300 → project from World Bank for electricity reach 300Mill new people in africa

Things we need

* How we're doing vending
* Correct timestamps
* Information about the grid

Proposed solution: take the telemetry from the field, add an additional service (?) and have access to the data via the server infrastructure

4 organizational members: IEEE, EnAccess, NESL, Arila

Rahul proposal:

* Daniel in convinced that telemetry should not go to MicoPowerManager (MPM) directly. We need middleware like Grid Fabric's backend (GFX) from Linux Foundation. The Frontend will still be MPM conceptually with a plugin that fetches required data more at a meter-level and associate billing and customer data in MPM. Meanwhile, grid-scale telemetry (distribution by phase of three-phase distribution from inverters) data can be analyzed by custom front-ends to a stable and mature Grid Fabric backend (that is heavy and requires servers and will not fit on DCUs). — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:20*
* Open AMI server, standardize schema (glenn has started this), called Grid Fabric. Linux foundation project. Not the Hyphae project.
* This project takes the logs from the DCU
* Glenn has defined a XML schema that is tuples, timestamp and readings for each meter. This can be optimized and adopted if compliant with IEEE 2030.5 — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:21*
* MicroPowerManager needs a plugin to ingest this data.
* There is an ingestion plugin by the Linux Foundation but we may need middleware to log the telemtery and then pull aggregations to MPM — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:22*
* Grid Fabric supports 2 protocols, both can be run on DCU
* DLMS →
* MQTT →
* Vendors are offering the keys to these protocols, not hacking the solutions
* Donsun, StemaCo, Inhemeter (not explicitly yet)
* This is on the table with support from SteamaCo — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:23*
* Donsun - has offered access to DCU (serial console / Telnet). Busybox linux environment. They have spare CPU cycles we can run other processes in.
* The guy who offered the keys is now gone though, and said Donsun is bankrupt
* Leets is not gone and Donsun's successor is not bankrupt, as per Warren of SteamaCo. HES support expected from SteamaCo — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:23*
* We weren't talking to Donsun directly though.
* Let's not talk to OEMs directly, go through SteamaCo — *[Rahul Bhargava](mailto:rahul.bhargava.in@ieee.org) 2025/10/28 14:24*
* "Leets" from Donsun
* Jude has Nigeran Donsun hardware
* StemaCo - service provider
* Donsun is one of 6 chinese OEMs that StemaCo will support
* If we go through StemaCo

– EnAccess - any updates/questions/agenda topics? – Sparkmeter source code access? — Rahul/Enaccess currently have it – Akash-plan/idea to hack the SparkMeter from Sun Gate Solar Rahul has access to code base, but it's "a mess"

Jude:

* We thought we had commitments to get keys to access hardware.
* Inhemeter is now asking for a contract
* Sparkmeter - stuck asking Alison (EarthSpark) trying to get opensource access 1 month later
* There may be some Google Drive with limited access to see source
* We Cannot use anything from this drive, legally, without Open-Sourcing it
* Rahul - we have pretty good reference of the architecture, but legally we cannot use it till Alison approves.
* TAM (AMDA): 1M meters, $20/meter = $20M TAM
* Seems unlikely we'll get access for free
* Donsun - collapsed mid-conversation
* StemaCo - we will probably hit the same wall
* As of today, we have no keys to any hardware. Only open hardware is our own board.

2) Clarification of problem statements, both short-term and long-term. – Short term will include exit of major metering vendors – Long term will include discussion of software and hardware solutions – We can use the Cairo OpenAMI slide deck ([link](https://docs.google.com/presentation/d/1b1Bl63I-evfd20MW6XxDe0IIse-0Nm85/edit?usp=sharing&ouid=112191662511889552544&rtpof=true&sd=true)) to start the discussion.

* Don - are we trying to hack existing systems or use the OpenAMI as our own standard?
* Last meeting, we found all the OEMs are having the same vulnerability. Don't want to support legacy products of theirs.

Question: Should we have this be a software-only solution? – Jude, Akash

3) Hardware discussion – Utility and desires for the MeshEMS gateway – Arila, Jude, Glenn, Akash, Rahul – What if we made our own hardware?

* 2 major players have already failed
* Rajan is skeptical
* Vivian - thumbs up. Not for the meters, but maybe for the DCU.
* Jude - yes let's talk about this
* Lots of donor money available
* Roadblocks - local developers/infrastructure
* Stemaco, Sparkmeter → were all whitelabeling a few OEMs. Did not make their own hardware (both metering and DCU).
* Sparkmeter - was whitelabeling their own meters, but making their own DCUs.
* Jude's idea:
* AMDA developers have 3 priorities:
* Vending
* Monitoring ability
* Ability to do operations (on/off control)
* Vending:
* Solved by STS/OpenPay Go
* So long as you have the CIU (customer intefface) at the meter level, and the token generation software, you can vend irrespective of the (?)
* Monitoring and Operations
* This is not yet solved. What if we take this as a standard?
* Like STS, we build a comms standard that can be deployed by the OEMs for people that want to go beyond vending.
* Maybe this requires an open-source DCU to go with it
* Building software that can go on DCUs that lets the data seen in multiple places
* Similar to an STS certification, this could be a selling point for new developers to use OEMS that are "OpenAMI" compliant

OpenPay Go and STS - similar For talking to the edge meter (supports STS, version 2)

* You'd need a key that talks to the STS

4) Blockers / goals for setting up Yaounde lab with Glenn's VPN hardware – Glenn, Jude, Endurance

5) ISV Funding and Project Plan Revisions – Don, Rajan, Jude

* Adam- how can we live stream any existing data from villages?

#### October 15th, 2025:
0) Recap of Oct 8th meeting for folks traveling back from Power Africa (Arila or Daniel)? (5-10 mins)

* Nothing major to discuss

1) Akash/Jude: Power Africa Recap (5-10 mins) a. Presentation recap

* Discussed with minigrid developers
* Sun Moksha - Indian minigrid company that is building smart metering. 3 priorities
* Vending - ability to make sales
* Manage the energy / assets
* Monitoring - what sparkmeter can provide
* Sun Moksha agrees on scarcity of metering suppliers / availability
* They have a prototype working on this that has solved their problem
* Make their own controller that talks between the meters (modbus) and server (wifi mesh), which then talks to the cloud
* They are open to share IP with the IEEE community; they've invested a lot of $ and don't have too much incentive to provide
* Not open-sourcing, but some sort of license that gives other vendors
* They built their own proprietary hardware (with ESP32 equivalent) that they could sell

b. Discussion recap / feedback session

* Jude: This looks like another locked solution, we would have the risk of being stuck on them
* Arila: Is there any openness from the open-source perspective from SunMoksha?
* Jude: This was developed for India, they had a sponsored project from India. Was a larger for minigrid developers in India previously, but currently isn't such a big market
* Arila: Is there an open solution available on the cloud side?
* Akash:
* Mou Riiny - interested in OpenAMI, frustrated with Sparkmeter
* Shared a sparkmeter to debug (malfunctional)
* Sparkmeter
* Vivien/Jude might have access to their repos
* What's the goal with this one?
* Just a test bed for now
* Akash to share
* Jude may have functional sparkmeters
* Nova / Edge Meter
* Has some spares

c. Akash - will try to make a slide on this

2) Jude: Client/customer's wishlist (5-10 mins) a. Jude's thoughts on the current status of the project b. Include pivots of the direction he would like to take this

3) Inhemeter call - Jude/Michel/Akash (5 mins) a. Recap of call with Sanji from inhemeter They want a signed document before providing documentation Awaiting on the confidential agreement from Inhemeter <→ Michel F is working on this b. "Cannot support the Inhe-4000 you got from nigeria" Latest model available is the Inhemeter-5000 c. "Please give us your specs for a new order" Donsun - sales person is no longer at Donsun Donsun is now bankrupt (!) Purchased sample meters through StemaCo

Rahul - Sparkmeter Sparkmeter has custom radios, not modbus 485 Need to be on their custom neighborhood network Rahul has access to the codebase and developers → can share answers to the queries Dominant architecture in Africa Radios are working on a certain set of frequencies, these are pretty locked Seems very hard to jailbreak existing sparkmeters based on this Recommends avoid committing to jailbreaking this Maybe easier to do if we are already in contact/customers with them

Arila: Was under the impression that there is Modbus Donsun Splitting into 2 One for Africa One for rest of world? Could expect code stubs for AMI potentially Rahul → older conversations

4) Formal roles within volunteer team - Jude a. Product Manager b. Project Manager c. Administrators d. Other roles?

5) Auditing/Changing of project timeline - Akash in place of Don (cannot make it)

6) Techincal debug and setup of REI-Cameroon Lab - Glenn/Endurance/Rahul a. Summarizing status of remote access b. Setup of new hardware / VPN from Glenn

Looking forward:

* So many meter vendors going bankrupt or not helpful
* How do we salvage existing meters/hardware in the field from these bankruptcies?
* Specific to REI-Cameroon,
* Jude has Sparkmeter and Stemaco (using Donsun)
* Sparkmeter has also moved to stop usage of older hardware
* Currently has ~800 sparkmeters
* Other hardware is at risk too
* Rahul:
* Would be great if we can support legacy systems. Some vendors (Sparkmeter for example) are not open to being supported
* While providing this legacy support, we basically create the support/framework for OpenAMI
* Vivien:
* Sparkmeter has not yet committed to becoming open, but needs help (has a lot of tickets, backlog, etc).

Sparkmeter

* Allison is the person we need to convince
* Rajan has talked, Vivien has talked to them, Jude has also talked to them, AMDA has also talked to them
* M300 has given them $ to stay alive, we have about 3-6 months of funding there

What do we as OpenAMI focus on in the next 3-6 months?

* Rahul: Support on legacy solutions
* Jude: Re-formulate the implementation plan
* Seems like everyone will be legacy soon
* Go back to drawing board
* Open-Source Hardware?
* Arila:
* Open-source meter for EnAccess
* Yes - but not available for use though
* For next week:
* Come with proposals for OpenAMI
* Akash - hardware gateway prototype
* No progress to report
* Is anyone blocked by this yet?
* Could be useful for some hardware prototyping
* Glenn's hardware
* Endurance hasn't been able

Follow-ups - Rahul weekly meeting?

* Stemaco and Donsun relationship?
* Vivian hardware access?
* Sparkmeter source code access?

