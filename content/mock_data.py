"""
content/mock_data.py — Threadline Centralized Mock Data

This module is the single source of truth for all article and category data
in V1. Views call helper functions defined here. Templates receive the same
dict structure that MongoDB documents will produce in Phase 2, so swapping
to MongoDB later requires only updating these helper functions — no views or
templates need to change.

Data structure mirrors the planned MongoDB collections defined in the spec:
  Articles, Categories, Users
"""

# ---------------------------------------------------------------------------
# CATEGORIES
# ---------------------------------------------------------------------------

CATEGORIES = [
    {
        'id': 'cat_001',
        'name': 'Sports',
        'slug': 'sports',
        'description': 'Stories, analysis and updates from the world of sports.',
    },
    {
        'id': 'cat_002',
        'name': 'Technology',
        'slug': 'technology',
        'description': 'The latest breakthroughs, trends and ideas shaping our digital future.',
    },
    {
        'id': 'cat_003',
        'name': 'News',
        'slug': 'news',
        'description': 'In-depth coverage of global events, politics and world affairs.',
    },
    {
        'id': 'cat_004',
        'name': 'Entertainment',
        'slug': 'entertainment',
        'description': 'Film, music, television and the culture that moves us.',
    },
]


# ---------------------------------------------------------------------------
# ARTICLES  (12 fictional demo articles — 3 per category)
# Images use picsum.photos seeded by slug for deterministic, stable previews.
# ---------------------------------------------------------------------------

ARTICLES = [

    # ===== SPORTS ==========================================================

    {
        'id': 1,
        'title': 'India Clinches Dramatic Series Victory',
        'slug': 'india-series-victory',
        'excerpt': (
            'A thrilling final match brought the series to an unforgettable conclusion, '
            'as India chased down 287 runs in the last over.'
        ),
        'content': """
<p>In what commentators are calling the most dramatic finish to a bilateral cricket series
in over a decade, the Indian national team pulled off a stunning last-over chase to
clinch the five-match series 3&ndash;2 against a formidable opposition on their home turf.</p>

<p>Needing 19 runs off the final over, stand-in captain Rohit Sharma and the emerging
talent Shubman Gill combined for an extraordinary partnership that left the packed stadium
in stunned silence before erupting in celebration. It was Gill&rsquo;s composure under
pressure that drew the most admiration &mdash; the young batsman smashed three consecutive
sixes off the penultimate deliveries to bring the equation down to a manageable finale.</p>

<h2>A Series Defined by Momentum Shifts</h2>

<p>The series had see-sawed dramatically across its five matches. India won the first two
games convincingly, only to lose the third and fourth to a revitalised bowling unit. The
fifth and deciding match saw both sides playing as if the world depended on it &mdash;
because, for their fans, it did.</p>

<blockquote>&ldquo;This is why we play cricket,&rdquo; Sharma said at the post-match
presentation. &ldquo;You cannot write a script like this.&rdquo;</blockquote>

<p>The victory was built on strong contributions throughout the lineup. The opening stand
of 87 runs gave India the platform they needed, while the middle-order collapse that
threatened to derail the chase only served to heighten the drama. When the last over
began, most observers had written off India&rsquo;s chances. The rest is history.</p>

<p>India&rsquo;s bowling unit, led by the veteran pacer who took four wickets for 38 runs,
was equally crucial in restricting the opposition to a chaseable total. The series victory
hands India a significant boost in the ICC rankings, moving them to second place in the
ODI standings.</p>
""",
        'category': 'sports',
        'author': 'Arjun Mehta',
        'image': 'https://picsum.photos/seed/india-series-victory/800/500',
        'status': 'published',
        'created_at': 'July 29, 2026',
        'featured': True,
    },

    {
        'id': 2,
        'title': 'Juventus Signs Record-Breaking Midfielder in Summer Window',
        'slug': 'juventus-signs-midfielder',
        'excerpt': (
            "The Italian giants shatter their transfer record to secure one of Europe's "
            'most coveted midfield talents ahead of the new season.'
        ),
        'content': """
<p>Juventus Football Club confirmed on Tuesday the signing of 24-year-old central
midfielder Luca Ferrara from Portuguese club Benfica for a club-record fee reported to
be in the region of &euro;95 million. The deal, which includes a further &euro;15 million
in potential add-ons, makes Ferrara the most expensive player in Juventus history.</p>

<p>Ferrara, who scored 18 goals and contributed 22 assists across all competitions last
season, emerged as one of the standout players in European football this term. His ability
to dictate tempo from deep while also arriving late into the box made him the subject of
intense interest from clubs across England, Spain and Italy.</p>

<h2>A Statement of Intent</h2>

<p>The acquisition signals Juventus&rsquo;s renewed ambition to challenge for Champions
League honours after a three-year absence from the knockout rounds. Club director
Alessandro Mauro spoke candidly at the signing ceremony held at the club&rsquo;s
Continassa training ground.</p>

<blockquote>&ldquo;Luca is exactly the kind of player who changes games,&rdquo; Mauro
said. &ldquo;We have been planning this signing for eighteen months, and we are delighted
to welcome him to the Juventus family.&rdquo;</blockquote>

<p>Ferrara himself expressed his delight at joining one of football&rsquo;s most storied
institutions. &ldquo;When Juventus come calling, you do not hesitate,&rdquo; he told
reporters. &ldquo;This club has a history unlike any other in Italian football. I want to
help bring the Champions League back to Turin.&rdquo;</p>

<p>The midfielder is expected to be presented to fans at the Allianz Stadium later this
week before joining the squad for pre-season training in Austria.</p>
""",
        'category': 'sports',
        'author': 'Marco Ricci',
        'image': 'https://picsum.photos/seed/juventus-signs-midfielder/800/500',
        'status': 'published',
        'created_at': 'July 27, 2026',
        'featured': False,
    },

    {
        'id': 3,
        'title': 'Elena Vasquez Stuns Wimbledon with Flawless Performance',
        'slug': 'vasquez-wimbledon-triumph',
        'excerpt': (
            'The unseeded Spaniard defeated three top-ten players in succession '
            'to reach her first Grand Slam final at the All England Club.'
        ),
        'content': """
<p>Nobody had Elena Vasquez down as a Wimbledon finalist at the start of the fortnight.
Seeded twenty-second and competing on grass for only the second time in her professional
career, the 26-year-old from Seville has transformed the tournament with a brand of
attacking tennis that has left opponents, commentators and fans utterly speechless.</p>

<p>Her semi-final victory over world number three Ananya Singh was widely described as
one of the finest grass-court performances seen at the All England Club in the Open Era.
Vasquez won 6&ndash;3, 6&ndash;2 in just 68 minutes, dictating every rally with a
groundstroke combination that Singh simply could not handle.</p>

<h2>From Red Clay to Green Grass</h2>

<p>Vasquez has built her reputation as a clay-court specialist over six years on the tour.
Her decision to overhaul her serve-and-volley game over the winter paid dividends almost
immediately, but few anticipated that the transformation would deliver results at this
level, this quickly.</p>

<blockquote>&ldquo;I changed everything,&rdquo; Vasquez said after her semi-final victory.
&ldquo;My grip, my serve motion, how I approach the net. It was frightening at first.
Now it feels natural.&rdquo;</blockquote>

<p>She will face defending champion Petra Lindqvist of Sweden in Saturday&rsquo;s final.
Lindqvist has been in ominous form herself, conceding just one set during the fortnight.
However, given Vasquez&rsquo;s trajectory this week, few are willing to bet against
another shock result on Centre Court.</p>
""",
        'category': 'sports',
        'author': 'Claire Donovan',
        'image': 'https://picsum.photos/seed/vasquez-wimbledon-triumph/800/500',
        'status': 'draft',
        'created_at': 'July 25, 2026',
        'featured': False,
    },

    # ===== TECHNOLOGY ======================================================

    {
        'id': 4,
        'title': "DeepMind's New Model Solves Protein Folding at Unprecedented Scale",
        'slug': 'deepmind-protein-folding',
        'excerpt': (
            'Researchers unveil AlphaFold 4, capable of mapping entire cellular protein '
            'interaction networks in minutes rather than months.'
        ),
        'content': """
<p>Google DeepMind has announced the release of AlphaFold 4, the latest iteration of its
groundbreaking protein structure prediction system. The new model, described in a paper
published simultaneously in <em>Nature</em> and across the DeepMind research blog,
represents a dramatic leap in capability &mdash; predicting not just individual protein
structures, but the full interaction maps of proteins within living cells.</p>

<p>The implications for pharmaceutical research, disease understanding and drug development
are profound. Processes that previously required months of laboratory work and supercomputer
time can now be completed in minutes on standard research hardware.</p>

<h2>From Structure to Interaction</h2>

<p>AlphaFold 3, released in 2024, had already demonstrated the ability to predict how
proteins bind to DNA, RNA and small molecules. AlphaFold 4 goes further still, modelling
entire protein-protein interaction networks at the scale of full organelles &mdash; the
compartments inside living cells.</p>

<blockquote>&ldquo;We are essentially giving researchers a map of the cellular interior
they have never had access to before,&rdquo; said Dr Priya Nair, one of the lead
researchers on the project. &ldquo;The question is no longer whether we can predict
structure. It&rsquo;s how quickly we can act on what we know.&rdquo;</blockquote>

<p>The model was trained on a dataset of over 200 million experimentally determined
structures, combined with synthetic data generated through a novel self-supervised
learning approach developed in-house at DeepMind.</p>

<p>The scientific community has responded with considerable excitement, though some
researchers caution that computational predictions still require experimental validation
before clinical applications can be pursued. DeepMind has made AlphaFold 4 available
free of charge to academic researchers through its existing research portal.</p>
""",
        'category': 'technology',
        'author': 'Priya Nair',
        'image': 'https://picsum.photos/seed/deepmind-protein-folding/800/500',
        'status': 'published',
        'created_at': 'July 28, 2026',
        'featured': False,
    },

    {
        'id': 5,
        'title': 'The Race to Build a Quantum Internet Has a New Frontrunner',
        'slug': 'quantum-internet-race',
        'excerpt': (
            'A consortium of European universities has demonstrated stable quantum '
            'entanglement across a 500-kilometre fibre link, setting a new world record.'
        ),
        'content': """
<p>Scientists at the Quantum Internet Alliance &mdash; a consortium of research
institutions spanning the Netherlands, Germany and Denmark &mdash; have achieved a
milestone that physicists have been working toward for two decades: the stable
transmission of entangled photon pairs across a 500-kilometre optical fibre network with
a fidelity rate exceeding 99.8 percent.</p>

<p>The result, confirmed by independent replication experiments at three separate
laboratories, pushes the boundaries of what quantum communication technology can achieve
at real-world distances. Previous records had topped out at around 250 kilometres before
quantum decoherence rendered the signal unusable.</p>

<h2>Why It Matters</h2>

<p>A functional quantum internet would offer communication channels that are, by the laws
of physics, impossible to intercept without detection. Unlike classical encryption, which
relies on mathematical problems that could theoretically be broken by a sufficiently
powerful computer, quantum cryptography guarantees security through the fundamental
principles of quantum mechanics.</p>

<blockquote>&ldquo;If an eavesdropper tries to observe a quantum-encrypted message, they
alter the quantum state and immediately reveal themselves,&rdquo; explained Professor
Hendrik Voss, Director of the Delft Quantum Lab. &ldquo;This isn&rsquo;t a feature of
the software. It&rsquo;s a law of nature.&rdquo;</blockquote>

<p>The research team achieved the breakthrough by developing a new class of quantum
repeaters &mdash; devices that can refresh and forward quantum signals without measuring
them, thereby preserving the entanglement. Three such repeaters were deployed along the
fibre network connecting Amsterdam, Hamburg and Copenhagen.</p>

<p>Commercial applications remain years away, but the technical demonstration has prompted
immediate interest from governments, central banks and intelligence agencies across Europe
and North America.</p>
""",
        'category': 'technology',
        'author': 'Elsa Brenner',
        'image': 'https://picsum.photos/seed/quantum-internet-race/800/500',
        'status': 'published',
        'created_at': 'July 26, 2026',
        'featured': False,
    },

    {
        'id': 6,
        'title': "Inside the Cyberattack That Shut Down a Nation's Power Grid",
        'slug': 'power-grid-cyberattack',
        'excerpt': (
            'A sophisticated state-sponsored intrusion exposed critical vulnerabilities '
            'in aging industrial control systems and sparked an international security review.'
        ),
        'content': """
<p>For eleven hours earlier this year, a fictional Eastern European nation experienced a
rolling series of cascading power failures that left major cities without electricity,
grounded commercial flights and disrupted hospital operations across four regions. What
initially appeared to be an infrastructure fault was quickly identified by cybersecurity
investigators as a deliberate, coordinated cyberattack targeting industrial control
systems deep within the national power grid.</p>

<p>The attackers, believed to be a state-sponsored group with access to sophisticated
tools and months of prior reconnaissance, used a combination of spear-phishing emails and
a previously undiscovered zero-day software vulnerability to gain access to operational
technology networks that control physical infrastructure.</p>

<h2>The Anatomy of a Grid Attack</h2>

<p>What made this incident particularly alarming to security researchers was its level of
operational sophistication. The attackers did not merely disrupt power flow &mdash; they
systematically staged their access over several months, mapping the grid&rsquo;s topology
and identifying optimal points of failure before executing their campaign.</p>

<blockquote>&ldquo;This wasn&rsquo;t smash-and-grab. This was a precision operation
planned over a long timeline,&rdquo; said Marcus Webb, lead analyst at cybersecurity firm
Sentinel Arc. &ldquo;The attackers understood the target environment better than some of
the operators running it.&rdquo;</blockquote>

<p>The incident has prompted an urgent review of industrial control system security
standards across Europe, with the EU proposing mandatory cybersecurity audits for all
critical infrastructure operators by the end of 2027. Similar debates have resurfaced in
Washington, where Congressional hearings on grid security have resumed after a two-year
pause.</p>
""",
        'category': 'technology',
        'author': 'Daniel Kowalski',
        'image': 'https://picsum.photos/seed/power-grid-cyberattack/800/500',
        'status': 'draft',
        'created_at': 'July 23, 2026',
        'featured': False,
    },

    # ===== NEWS ============================================================

    {
        'id': 7,
        'title': 'World Leaders Agree on Landmark Climate Financing Deal',
        'slug': 'landmark-climate-deal',
        'excerpt': (
            'The Nairobi Accord commits forty-seven nations to a $2.4 trillion climate '
            'finance package, the largest in history.'
        ),
        'content': """
<p>After five days of intensive negotiations in Nairobi, representatives from forty-seven
nations emerged on Friday evening to announce the Nairobi Accord &mdash; a landmark
climate financing agreement that commits signatory countries to mobilising $2.4 trillion
for renewable energy transition, climate adaptation and loss-and-damage compensation over
the next fifteen years.</p>

<p>The agreement, brokered under the auspices of the United Nations Framework Convention
on Climate Change, breaks new ground in several areas. For the first time, middle-income
nations are included as both contributors and recipients in a structured framework,
addressing a long-standing criticism that previous climate finance deals benefited only
the least-developed countries while ignoring the vast middle tier of the global economy.</p>

<h2>A Breakthrough on Loss and Damage</h2>

<p>Perhaps the most significant element of the Accord is its formal mechanism for
loss-and-damage payments &mdash; financial transfers from historically high-emitting
nations to those suffering the worst consequences of climate change without having
significantly contributed to it. The mechanism, which had been blocked in previous
negotiations by major emitters, was finally agreed following a late-night session that
reportedly lasted until dawn.</p>

<blockquote>&ldquo;History will judge this moment as the turning point,&rdquo; said UN
Secretary-General Amara Diallo. &ldquo;The question of who pays for the climate crisis
has been answered, at least in principle. Now we must make certain that principle becomes
practice.&rdquo;</blockquote>

<p>Environmental groups broadly welcomed the agreement while cautioning that implementation
would be critical. Several NGOs noted that previous climate finance commitments had fallen
short of their targets, and called for robust independent monitoring mechanisms to be
written into the Accord&rsquo;s implementation framework.</p>
""",
        'category': 'news',
        'author': 'Sarah Kimani',
        'image': 'https://picsum.photos/seed/landmark-climate-deal/800/500',
        'status': 'published',
        'created_at': 'July 28, 2026',
        'featured': False,
    },

    {
        'id': 8,
        'title': 'Global Economy Shows Unexpected Signs of Resilience',
        'slug': 'global-economy-resilience',
        'excerpt': (
            'Revised IMF projections suggest stronger-than-expected growth across '
            'emerging markets, confounding earlier predictions of a prolonged slowdown.'
        ),
        'content': """
<p>The International Monetary Fund released revised growth projections on Thursday
suggesting the global economy is performing meaningfully better than forecast six months
ago, driven by robust consumer spending in South and Southeast Asia, a recovery in Chinese
manufacturing output and resilient labour markets across much of the European Union.</p>

<p>The Fund&rsquo;s updated World Economic Outlook projects global GDP growth of 3.4
percent for 2026, up from the 2.9 percent predicted in its January report. The revision
represents a significant upward shift that has caught several leading economists by
surprise.</p>

<h2>Emerging Markets Lead the Recovery</h2>

<p>The most striking aspect of the revised projections is the outperformance of emerging
and developing economies, which are collectively forecast to grow at 5.1 percent &mdash;
the fastest rate for a non-pandemic rebound year since 2010. India leads the group with
projected growth of 7.8 percent, followed by Vietnam at 6.9 percent and Indonesia at
5.7 percent.</p>

<blockquote>&ldquo;The narrative of a global slowdown has proved to be premature,&rdquo;
said IMF Chief Economist Dr. Miriam Fontaine at a press briefing in Washington. &ldquo;We
are seeing genuine structural strength in parts of the world that were written off by
investors twelve months ago.&rdquo;</blockquote>

<p>The projections are not without caveats. The IMF flagged ongoing risks including
persistent inflation in services sectors, geopolitical tensions affecting energy markets,
and the potential for financial contagion from elevated debt levels in several
middle-income countries. The Fund maintained its call for careful, data-dependent monetary
policy from central banks worldwide.</p>
""",
        'category': 'news',
        'author': 'James Okafor',
        'image': 'https://picsum.photos/seed/global-economy-resilience/800/500',
        'status': 'published',
        'created_at': 'July 26, 2026',
        'featured': False,
    },

    {
        'id': 9,
        'title': 'UN Summit Calls for Urgent Action on Refugee Crisis',
        'slug': 'un-refugee-summit',
        'excerpt': (
            'With global displacement at a record 117 million, world leaders gathered '
            'in Geneva to chart a new course for international protection frameworks.'
        ),
        'content': """
<p>A special session of the United Nations General Assembly convened in Geneva this week
to address what the UNHCR has described as the largest forced displacement crisis in
recorded history. With 117 million people currently displaced from their homes by conflict,
persecution and climate-related events, the international protection system faces a strain
that existing frameworks were never designed to handle.</p>

<p>The two-day summit, attended by heads of state or senior ministers from sixty-eight
countries, aimed to build consensus around a new Comprehensive Protection Framework &mdash;
a proposed set of binding commitments that would update and expand the legal protections
afforded by the 1951 Refugee Convention.</p>

<h2>Divisions Remain</h2>

<p>Despite the stated urgency of the gathering, significant divisions between participating
nations quickly became apparent. A bloc of European governments, several of which have
implemented increasingly restrictive immigration policies in recent years, resisted language
in the draft framework that would formally recognise climate displacement as a grounds for
refugee status &mdash; a change the UNHCR has been lobbying for since 2023.</p>

<blockquote>&ldquo;We cannot continue to apply a seventy-five-year-old legal instrument to
a twenty-first century crisis,&rdquo; said UNHCR Director-General Ama Koffi-Asante.
&ldquo;The world has changed. Our protection systems must change with it.&rdquo;</blockquote>

<p>The summit concluded with a political declaration that, while lacking the binding force
of a treaty, reaffirmed member states&rsquo; commitments to the existing Convention and
established a working group tasked with drafting a formal protocol on climate displacement
for consideration at the next General Assembly session.</p>
""",
        'category': 'news',
        'author': 'Fatima Al-Hassan',
        'image': 'https://picsum.photos/seed/un-refugee-summit/800/500',
        'status': 'draft',
        'created_at': 'July 24, 2026',
        'featured': False,
    },

    # ===== ENTERTAINMENT ===================================================

    {
        'id': 10,
        'title': 'Cannes 2026: The Films That Redefined a Generation',
        'slug': 'cannes-2026-films',
        'excerpt': (
            "This year's festival brought an extraordinary cohort of debut and sophomore "
            'features that challenged the very definition of what cinema can be.'
        ),
        'content': """
<p>The 79th Cannes Film Festival closed its doors on Saturday evening with a ceremony
that felt less like an awards show and more like a collective exhale &mdash; the
industry&rsquo;s acknowledgement that something genuinely significant had just occurred.
Over twelve days on the French Riviera, an exceptional selection of films challenged
comfortable assumptions, broke formal conventions and reminded a generation of filmgoers
why cinema remains the art form&rsquo;s most visceral and communal experience.</p>

<p>The Palme d&rsquo;Or was awarded to Iranian director Leila Moghimi&rsquo;s debut
feature <em>The Salt Road</em>, a three-and-a-half-hour meditation on grief, migration
and memory that left the Grand Th&eacute;&acirc;tre Lumi&egrave;re in stunned silence
before a ten-minute standing ovation. The film follows three generations of a family
across forty years, told entirely without dialogue in the traditional sense.</p>

<h2>A Decade's Worth of Debuts</h2>

<p>What made Cannes 2026 particularly remarkable was the quality concentrated in the
parallel sections. The Directors&rsquo; Fortnight and Un Certain Regard programmes
delivered debut features from filmmakers in Brazil, South Korea, Nigeria and Norway that,
in normal years, would have been contenders for the main Competition.</p>

<blockquote>&ldquo;I have attended Cannes for twenty-two years,&rdquo; said veteran
critic Elena Rousseau of <em>Cahiers du Cin&eacute;ma</em>. &ldquo;This is perhaps the
richest selection of debuts I have witnessed in a single festival. Something is happening
in world cinema right now.&rdquo;</blockquote>

<p>The festival also confirmed the arrival of streaming as a genuine creative force at
the highest level of cinematic ambition. Three of the competition films were produced by
streaming platforms, yet all three insisted on theatrical debuts &mdash; a sign that the
industry&rsquo;s long-running tensions around exhibition windows may finally be resolving
into something more nuanced.</p>
""",
        'category': 'entertainment',
        'author': 'Isabelle Laurent',
        'image': 'https://picsum.photos/seed/cannes-2026-films/800/500',
        'status': 'published',
        'created_at': 'July 27, 2026',
        'featured': False,
    },

    {
        'id': 11,
        'title': "Priya Kapoor's Album 'Monsoon' Shatters Streaming Records",
        'slug': 'monsoon-album-records',
        'excerpt': (
            "The Mumbai-born singer's third studio album became the fastest South Asian "
            'album to reach 500 million streams, forcing the industry to rethink its '
            'global market assumptions.'
        ),
        'content': """
<p>Priya Kapoor&rsquo;s third studio album <em>Monsoon</em> crossed 500 million streams
across major platforms in just eleven days following its release, establishing a new
benchmark for South Asian artists in the global music market and prompting a reassessment
of how major labels approach international talent development.</p>

<p>The album, produced entirely in Mumbai and co-written by Kapoor with longtime
collaborator Rishabh Shah, blends Hindi lyrical traditions with contemporary electronic
production in a way that has resonated powerfully with listeners well beyond the South
Asian diaspora. Chart positions in Germany, Brazil and Japan signal a genuine crossover
rather than a diaspora-driven phenomenon.</p>

<h2>The Sound of Monsoon</h2>

<p>Musically, <em>Monsoon</em> is an extraordinarily confident record. Where Kapoor&rsquo;s
debut was characterised by cautious genre fusion, and her second album by an ill-advised
attempt to appeal directly to Western pop sensibilities, this third effort sounds like an
artist who has stopped asking for permission. The production is dense and immersive, the
vocals confident and varied, and the arrangements &mdash; which weave sitar, tabla and
ambient electronic textures into a genuinely coherent sonic world &mdash; are unlike
anything currently being made at this scale.</p>

<blockquote>&ldquo;I made this album for myself first,&rdquo; Kapoor said in a widely
shared interview this week. &ldquo;I spent two years on it. I wasn&rsquo;t thinking about
markets or playlists. I was thinking about what a monsoon actually sounds like inside your
chest.&rdquo;</blockquote>

<p>The critical response has been uniformly ecstatic. <em>Pitchfork</em> awarded the
album a rare 9.2, calling it &ldquo;a landmark work of global pop ambition,&rdquo; while
<em>Rolling Stone</em> included it in its midyear list of the twenty most important albums
of the decade so far.</p>
""",
        'category': 'entertainment',
        'author': 'Rahul Sharma',
        'image': 'https://picsum.photos/seed/monsoon-album-records/800/500',
        'status': 'published',
        'created_at': 'July 25, 2026',
        'featured': False,
    },

    {
        'id': 12,
        'title': "How 'The Meridian' Became the Show Television Needed",
        'slug': 'the-meridian-tv-show',
        'excerpt': (
            'The critically acclaimed drama series challenged the streaming model, '
            'returned television to the weekly release format, and proved that patience '
            'still has a place in the medium.'
        ),
        'content': """
<p>When the streaming platform Vela announced it would release its prestige drama
<em>The Meridian</em> in weekly instalments rather than dropping all episodes
simultaneously, industry observers predicted disaster. In an era defined by the
binge-watch, a show asking audiences to wait &mdash; actually wait &mdash; for the next
chapter seemed not just anachronistic but commercially reckless.</p>

<p>Eighteen months later, <em>The Meridian</em> stands as the most-discussed television
series in years, its weekly release schedule not merely a scheduling quirk but an integral
part of its cultural impact. The show&rsquo;s creator, Josephine Tremblay, has been
credited with engineering a return to communal television viewing at a moment when most
observers had declared it dead.</p>

<h2>What Makes It Work</h2>

<p><em>The Meridian</em> tells the story of a small coastal community reckoning with the
slow disappearance of its shoreline &mdash; a climate drama framed as a detective story,
a family saga and, in its final act, something approaching myth. The writing is
extraordinarily precise. Every line of dialogue carries weight. Every scene earns its
place. It is the rare television drama that seems to have been made by people who genuinely
care about what happens between commercial breaks &mdash; even when there are no commercial
breaks.</p>

<blockquote>&ldquo;I was very deliberate about the pacing,&rdquo; Tremblay told an
audience at the Television Critics Association press tour. &ldquo;I wanted people to have
to live with it. To think about it during the week. To argue with their friends about what
it meant. That&rsquo;s what television used to do. That&rsquo;s what it can do
again.&rdquo;</blockquote>

<p>The second season is already in production, with Tremblay reportedly expanding the
story&rsquo;s geographical scope while retaining its intimate emotional register. Whether
<em>The Meridian</em> represents a lasting shift in how prestige drama is made and
consumed, or a beautiful exception to entrenched industry logic, will be answered in the
years to come.</p>
""",
        'category': 'entertainment',
        'author': 'Nadia Foster',
        'image': 'https://picsum.photos/seed/the-meridian-tv-show/800/500',
        'status': 'draft',
        'created_at': 'July 22, 2026',
        'featured': False,
    },
]


# ---------------------------------------------------------------------------
# HELPER FUNCTIONS
# In Phase 2, replace these function bodies with MongoDB queries.
# The function signatures and return shapes must remain identical so that
# views.py and templates require zero changes.
# ---------------------------------------------------------------------------

def get_all_articles():
    """Return all articles."""
    return ARTICLES


def get_articles_by_category(category_slug):
    """Return articles filtered by category slug."""
    return [a for a in ARTICLES if a['category'] == category_slug]


def get_article_by_slug(slug):
    """Return a single article by slug, or None if not found."""
    for a in ARTICLES:
        if a['slug'] == slug:
            return a
    return None


def get_article_by_id(pk):
    """Return a single article by integer pk, or None if not found."""
    for a in ARTICLES:
        if a['id'] == pk:
            return a
    return None


def get_featured_article():
    """Return the first article marked as featured, falling back to the first article."""
    for a in ARTICLES:
        if a.get('featured'):
            return a
    return ARTICLES[0] if ARTICLES else None


def get_trending_articles(n=3):
    """Return n trending articles (published, non-featured)."""
    featured = get_featured_article()
    candidates = [
        a for a in ARTICLES
        if a['status'] == 'published' and a.get('id') != (featured or {}).get('id')
    ]
    return candidates[:n]


def get_latest_articles(n=8):
    """Return n most recent articles."""
    return ARTICLES[:n]


def get_category_preview(category_slug, n=3):
    """Return n articles for a category preview (used on the homepage)."""
    return get_articles_by_category(category_slug)[:n]


def get_related_articles(article, n=3):
    """Return n related articles from the same category, excluding the current article."""
    same_cat = [
        a for a in ARTICLES
        if a['category'] == article['category'] and a['slug'] != article['slug']
    ]
    if len(same_cat) < n:
        # Top up from other categories if needed
        others = [
            a for a in ARTICLES
            if a['category'] != article['category'] and a['slug'] != article['slug']
        ]
        same_cat = same_cat + others
    return same_cat[:n]


def search_articles(query):
    """Case-insensitive search across title, category and excerpt."""
    if not query:
        return []
    q = query.lower()
    return [
        a for a in ARTICLES
        if q in a['title'].lower()
        or q in a['category'].lower()
        or q in a['excerpt'].lower()
    ]


def get_categories():
    """Return all categories."""
    return CATEGORIES


def get_category_by_slug(slug):
    """Return a category dict by slug, or None if not found."""
    for c in CATEGORIES:
        if c['slug'] == slug:
            return c
    return None


def get_category_article_counts():
    """Return a dict mapping category slug to article count."""
    return {c['slug']: len(get_articles_by_category(c['slug'])) for c in CATEGORIES}
