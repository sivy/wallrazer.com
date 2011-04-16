---
layout: post
title: A story about a programmer (historical fiction)
---
*This was a writing exercise for [750words](http://750words.com), but inspired by some recent thinking...*

This is a story. A story about a programmer. A programmer with a manager breathing down his neck. He had to get the site updated... pronto. What was that server IP again? He had a cheat sheet around here somewhere. Where was it?

He rummaged around the desk for 2 more minutes, looking for that 3" by 3" scrap of yellow paper. What was it with him and the Stickies? He simply loved them. Too much, it would seem. Now that he needed a particular one they were falling off his monitor like drifting snow. Bits of his work life falling around him like his hopes.

He looked at the phone again. The message light was blinking. And again. Phil had left him two more messages. Really, Phil?, he thought. Like I don't know that the service hosting the images is broken and none of those images - the ones on our new slideshow-building site - are loading? Leave me alone so I can think!

He rummaged some more for the sticky note, then a glimmer of hope popped into a corner of his mind. He had started transferring stuff into the notepad app on his computer, starting with the most important ones. He had then trashed the stickies after he transferred their contents. He pushed his chair back towards the desk and pulled the keyboard back into reach, knocking more stickies and a pencil onto the floor in the process. He furiously closed apps looking for the notepad window, and found it minimized in the dock.

There it was. The note with the server details: IP address, web server username, password (yes, he knew that was a bad idea but Phil kept making him change it!), the file system path, and a cheat sheet of commands to update the site and restart the server.

He tabbed through some more windows until he found the configuration file where the alternate image hosting providers were now listed (he wished he had been more assertive when suggesting to Phil and Phil's boss that they use a couple different providers). Yes, the changes were there. He double-checked them against - yes, another sticky - and committed the changes. That was step one.

He had realized 6 months ago that they needed to have the site code in source control. It took a catastrophic disk failure for him to stop putting it off. He finally got around to signing up for an account and importing everything, and now 3 months in he breathed a sigh of relief every time he committed something into that miraculous combination of backup and time machine.

He breathed that sign now, and turned his attention to following his cheat sheet to get the site updated. He signed into the server from the terminal, typing the password in twice because most recently Phil had insisted on a 12 character, random-letters-numbers-and-punctuation password. He swore at Phil, again. The phone rang again. He could imagine Phil sitting at his desk, hammering his F5 key in an attempt to fix the site by willpower alone.

Ok, only 4 more steps. He navigated to the directory on the sticky, then the commands to download the changes from source control. He wasn't sure if it would be easier if he did this more often, or less. Phil wanted new features added to the site as quickly as possible, but Phil's boss wanted big updates with lots of features, so they tended to wait. He didn't mind so much because it was such a pain to update, and was secretly nervous that he was going to break something. Well, now something was broke. At least it hadn't been his fault.

Ok, the codebase had been updated with the new code, and the config file with the new hosting providers was in place. Done, reload in the browser. Crap, not done... oh, right, the web server. He slapped a palm over his face, then looked up the last command in the notepad app. He typed it in, hit , counted to ten, and hit reload in the browser. The page came up and then images began to pop into place, 2 or 3 at a time, as the browser his the new hosting provider.

He slumped back in his chair and let out a long breath. He liked this job, and Phil wasn't really that bad. He had a lot of great ideas, and the site had been growing quickly over the last 9 months. But going a month or more between releases (except for the emergencies) meant that he kept forgetting these details and then stressed the heck out when it came time to release something. He cracked another diet soda and wished he just had a big red button that said "fix the site".

