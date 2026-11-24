"""Page text for the ShiftMate website. Written for business owners and their staff."""
EMAIL = "sabeehdayyanofficial@gmail.com"
UPDATED = "24 November 2026"
M = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

PRIVACY = f"""
<h1>Privacy policy</h1>
<p class="muted">Last updated {UPDATED}</p>
<p>This policy explains what personal information the ShiftMate app and website collect, why, and what you can do about it.
ShiftMate is provided by <strong>Sabeeh Dayyan</strong> ("we", "us"). You can contact us about privacy at {M}.</p>

<h2>Who is responsible for your information</h2>
<p>ShiftMate is used by businesses ("employers") to run rotas, time clocks and team updates for their staff.</p>
<ul>
<li><strong>Your employer</strong> decides what work information is recorded about you in their workplace, such as your shifts,
timesheets, leave and pay rates. For that information your employer is the <em>controller</em> and we process it on their behalf.
Questions about it are best sent to your employer first.</li>
<li><strong>We</strong> are the controller for your ShiftMate account itself (your login and profile), for the business owner's
account and subscription, and for keeping the service secure.</li>
</ul>

<h2>What we collect</h2>
<table>
<tr><th>Information</th><th>Why</th></tr>
<tr><td>Name, email address and password (stored only as a secure hash by our sign-in provider)</td><td>To create your account and let you sign in</td></tr>
<tr><td>Phone number and job title (optional)</td><td>So your team can reach you; you choose whether coworkers see your number</td></tr>
<tr><td>Workplace information: locations, jobs, shifts, swaps, availability, leave requests and balances, timesheets, tasks, posts, comments and documents</td><td>To provide the service your employer uses</td></tr>
<tr><td>Precise location, <strong>only at the moment you clock in, start or end a break, or clock out</strong></td><td>So your employer can see whether you were at work when you clocked in. ShiftMate never tracks your location in the background.</td></tr>
<tr><td>Photos you choose to take when clocking in, and photos or videos you add to posts</td><td>To show them to the people your employer allows</td></tr>
<tr><td>Pay rates and pay rules entered by your employer</td><td>To estimate labour costs. Only owners, admins and managers with pay permission can see them; team members never can.</td></tr>
<tr><td>A device token for notifications</td><td>To send you alerts about your shifts and your team</td></tr>
<tr><td>Business details for owners: business name, country and VAT number (optional)</td><td>To set up the workplace, its currency and its plan</td></tr>
<tr><td>Basic technical logs (for example, when a request failed)</td><td>To keep the service working and secure</td></tr>
</table>
<p>We do not sell your information, use it for advertising, or use it to make automated decisions about your pay or job.
ShiftMate does not use face recognition or any biometric matching.</p>

<h2>Legal bases</h2>
<p>We process account and service information to perform our contract with the business that uses ShiftMate, and to provide the service you
signed up for. We keep the service secure and prevent misuse (for example, one free trial per business) because we have a legitimate interest in doing so.
Location is collected only when you choose to clock in or out, and your phone asks for your permission first.</p>

<h2>Who we share it with</h2>
<ul>
<li><strong>People in your workplace</strong>, according to their role. For example, managers see the rota and timesheets for their locations;
coworkers see published shifts and posts.</li>
<li><strong>Google (Firebase and Google Cloud)</strong>, which hosts ShiftMate's database, files, sign-in and notifications for us. Our database
and files are stored in London. Google may process some information in other countries under its data processing terms and standard contractual clauses.</li>
<li><strong>A payment provider</strong>, once paid plans are available, to handle payments for business owners. We never store card details.</li>
<li>Authorities, if the law requires it.</li>
</ul>

<h2>How long we keep it</h2>
<ul>
<li>Your account information is kept while your account exists.</li>
<li>When you delete your account, your login, profile, phone number, availability, clock-in photos and notifications are deleted straight away.
Records your employer needs for payroll and legal reasons, such as past timesheets and pay history, stay with your employer and show you as "Deleted user".</li>
<li>When a workplace's plan ends, its information is kept for at least 30 days so the owner can renew, then deleted on request or when we close inactive workplaces.</li>
<li>When an owner deletes their workplace, everything in it is deleted.</li>
<li>To stop the free trial being claimed again and again, we keep a one-way scrambled code made from the owner's email and business name. It can't be turned back into either.</li>
</ul>

<h2>Your rights</h2>
<p>You can ask to access, correct, delete or receive a copy of your information, to object to or restrict how we use it, and to withdraw any consent.
Email {M}. For information your employer controls, we will pass your request to them or help them answer it. You can
<a href="delete-account.html">delete your account</a> at any time in the app.</p>
<p>If you are unhappy with how we handle your information, you can complain to the data protection authority where you live or work.
In the United Kingdom that is the Information Commissioner's Office (ico.org.uk).</p>

<h2>Security</h2>
<p>Information is encrypted in transit and at rest. Each workplace's data is kept separate, and access follows each person's role, enforced on our servers.
Every view of pay information is logged.</p>

<h2>Children</h2>
<p>ShiftMate is for businesses and their staff. It is not intended for anyone under 16.</p>

<h2>Changes</h2>
<p>We will update this page when this policy changes and, for significant changes, tell business owners in the app or by email.</p>
"""

TERMS = f"""
<h1>Terms of service</h1>
<p class="muted">Last updated {UPDATED}</p>
<p>These terms apply to your use of ShiftMate, provided by <strong>Sabeeh Dayyan</strong> ("we", "us"). By creating an account you agree to them.
If you create a workplace for a business, you confirm you can accept these terms for that business.</p>

<h2>The service</h2>
<p>ShiftMate helps businesses plan rotas, record working time, manage leave and keep their team informed. Some features estimate labour cost
and flag possible working-time issues. <strong>These are estimates and guidance based on the information you enter, not legal, tax or payroll advice.</strong>
You remain responsible for paying your staff correctly and for complying with employment and working-time law.</p>

<h2>Accounts</h2>
<ul>
<li>Keep your password safe and tell us if you think someone else has used your account.</li>
<li>Business owners decide who joins their workplace and what each person can do.</li>
<li>You can delete your account at any time from Profile and privacy in the app.</li>
</ul>

<h2>Free trial and plans</h2>
<ul>
<li>New workplaces get a <strong>30-day free trial</strong> with every feature. No card is needed. Each business can have one free trial.</li>
<li>After the trial, a paid plan is needed to keep making changes. Prices are shown on our <a href="pricing.html">pricing page</a> and exclude VAT or sales tax.</li>
<li>If a workplace has no active plan, everyone can still sign in, view and export their information, but changes are paused.
Staff can still clock in and out for 7 days so nobody is caught out mid-shift.</li>
<li>Paid plans renew until cancelled. You can cancel at any time; the plan stays active until the end of the period already paid for.</li>
</ul>

<h2>Acceptable use</h2>
<p>Don't use ShiftMate to break the law, to harass anyone, to upload content you have no right to share, to try to reach other workplaces' information,
or to disrupt the service. We may suspend accounts that do.</p>

<h2>Your content</h2>
<p>You and your business own what you put into ShiftMate. You give us permission to store and process it only to provide the service.
Our <a href="privacy.html">privacy policy</a> explains how we handle personal information.</p>

<h2>Availability</h2>
<p>We work to keep ShiftMate available and secure, but we can't promise it will always be uninterrupted or error-free. We may change or improve features over time.</p>

<h2>Liability</h2>
<p>Nothing in these terms limits liability that can't be limited by law. Otherwise, we are not liable for indirect or consequential loss, loss of profit,
or losses caused by information you entered. Our total liability to a business in any 12 months is limited to the amount it paid us in that period.</p>

<h2>Ending</h2>
<p>You can stop using ShiftMate at any time. We may end or suspend access if these terms are seriously broken, or with reasonable notice if we stop the service.</p>

<h2>Changes and law</h2>
<p>We may update these terms and will tell business owners about significant changes. These terms are governed by the laws of England and Wales.</p>

<h2>Contact</h2>
<p>{M}</p>
"""

DELETE = f"""
<h1>Delete your ShiftMate account</h1>
<p>You can delete your account yourself in the app at any time:</p>
<ol>
<li>Open ShiftMate and go to <strong>More → Profile and privacy</strong>.</li>
<li>Tap <strong>Delete my account</strong> and enter your password to confirm.</li>
</ol>
<p>If you can't sign in, email {M} from the address you use for ShiftMate with the subject "Delete my account".
We will confirm it's you and delete the account within 30 days.</p>

<h2>What is deleted</h2>
<ul>
<li>Your login, name, email address, phone number and profile</li>
<li>Your availability, clock-in photos and notifications</li>
<li>Your upcoming shifts are taken off you so your manager can fill them</li>
</ul>
<h2>What your employer keeps</h2>
<p>Records your employer needs for payroll and legal reasons, such as past timesheets, past shifts and pay history, stay with the workplace and
show you as "Deleted user".</p>
<h2>Workplace owners</h2>
<p>If you own a workplace and other people still use it, hand ownership to someone else first (Team → their profile).
If you're the only member, deleting your account deletes the workplace and everything in it.</p>
"""

INDEX = f"""
<img src="img/banner.jpg" alt="ShiftMate screens: manager dashboard, weekly rota, time clock and timesheet approval" style="width:100%;border-radius:16px">
<div class="grid" style="margin-top:20px">
<div class="card"><h3 style="margin-top:0">Rotas in minutes</h3><p>Plan the week, publish with one tap, and let staff pick up open shifts or swap with a coworker.</p></div>
<div class="card"><h3 style="margin-top:0">A time clock that checks location</h3><p>Staff clock in on their phone. ShiftMate checks they're at work, only at that moment.</p></div>
<div class="card"><h3 style="margin-top:0">Timesheets ready for payroll</h3><p>See late starts and missing clock-outs, correct with a note, approve in bulk and export.</p></div>
<div class="card"><h3 style="margin-top:0">Leave and availability</h3><p>Requests, balances and approvals in one place, with conflicts flagged on the rota.</p></div>
<div class="card"><h3 style="margin-top:0">Team updates</h3><p>News with photos and video, documents to read and confirm, and tasks for each shift.</p></div>
<div class="card"><h3 style="margin-top:0">Pay rates, kept private</h3><p>Rates per job and per person, visible only to the people you choose. Every view is logged.</p></div>
</div>
<p style="margin-top:24px"><a class="btn" href="https://play.google.com/store/apps/details?id=com.shiftmate.app">Get it on Google Play</a></p>
<p class="muted">30-day free trial with every feature. No card needed.</p>
"""

PRICING = f"""
<h1>Simple pricing</h1>
<p>Start with a <strong>30-day free trial</strong> of every feature. No card needed. After that, pay only for the people who actually work:
you're charged per <em>active user</em> each month, meaning anyone who had a published shift or clocked in.</p>
<div class="grid">
<div class="card"><h2 style="margin-top:0">Basic</h2>
<p class="price">£2.79 <span class="muted" style="font-size:16px;font-weight:400">per active user / month</span></p>
<p class="muted">$3.49 · €3.29</p>
<ul><li>Rota, open shifts and swaps</li><li>Time clock with location check</li><li>Timesheets and payroll export</li><li>Leave and availability</li><li>News, documents and tasks</li><li>Multiple locations</li></ul></div>
<div class="card"><h2 style="margin-top:0">Pro</h2>
<p class="price">£4.79 <span class="muted" style="font-size:16px;font-weight:400">per active user / month</span></p>
<p class="muted">$5.99 · €5.49</p>
<ul><li>Everything in Basic</li><li>Pay rates per job and per person</li><li>Pay rules and labour cost settings</li>
<li class="muted">Coming soon: labour cost on the rota, budgets, compliance warnings and reports</li></ul></div>
</div>
<table>
<tr><th></th><th>GBP</th><th>USD</th><th>EUR</th></tr>
<tr><td>Minimum per business, per month</td><td>£9</td><td>$12</td><td>€11</td></tr>
<tr><td>Yearly billing</td><td colspan="3">Pay for 10 months, get 12</td></tr>
</table>
<p class="muted">Prices exclude VAT or sales tax. Paid plans open before the first free trials end; we'll email workplace owners when
you can choose one. Until you do, nothing is charged.</p>
"""

SUPPORT = f"""
<h1>Support</h1>
<p>Email {M} and we'll get back to you, usually within one working day.</p>
<h2>Common questions</h2>
<h3>How do I add my team?</h3>
<p>In the app, go to <strong>Team → Invite</strong>, create an invite code and share it. Staff download ShiftMate, sign up and enter the code.</p>
<h3>Why does ShiftMate ask for my location?</h3>
<p>Only to check you're at work when you clock in or out, if your employer has set a clock-in pin. It never tracks you in the background.</p>
<h3>I forgot my password.</h3>
<p>On the sign-in screen tap <strong>Forgot password?</strong> and we'll email you a reset link.</p>
<h3>I'm not getting notifications.</h3>
<p>Check notifications are allowed for ShiftMate in your phone's settings, and look at <strong>More → Notification settings</strong> for muted alerts or quiet hours.</p>
<h3>What happens when the free trial ends?</h3>
<p>Everyone can still sign in and see everything, but changes pause until the owner chooses a plan. Staff can still clock in and out for 7 days.</p>
<h3>How do I delete my account?</h3>
<p>See <a href="delete-account.html">Delete your account</a>.</p>
"""

PAGES = [
    ("index.html", "ShiftMate: rotas, time clock and team updates", INDEX,
     ("Rotas, time clock and team updates in one place", "ShiftMate keeps shift-based teams like cafés, restaurants and shops organised, so everyone knows where they need to be.")),
    ("pricing.html", "Pricing · ShiftMate", PRICING),
    ("support.html", "Support · ShiftMate", SUPPORT),
    ("privacy.html", "Privacy policy · ShiftMate", PRIVACY),
    ("terms.html", "Terms of service · ShiftMate", TERMS),
    ("delete-account.html", "Delete your account · ShiftMate", DELETE),
]
