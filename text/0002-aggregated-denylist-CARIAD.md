- RFC Name: aggregated-denylist-CARIAD
- RFC PR: [https://github.com/iftas-org/rfcs/pull/](https://github.com/iftas-org/rfcs/pull/19)
- Start Date: 2023-10-31

IFTAS RFC: CARIAD
Consensus Aggregated Retractable IFTAS Allowlist Denylist

# Proposal Status

|                                                            |                        |
| ---------------------------------------------------------- | ---------------------- |
| IFTAS Workgroup Proposal                                   | Complete               |
| IFTAS Membership Comment Period                            | Complete               |
| Domain Experts / Interested Parties Comment Period         | 2023-10-07             |
| Public Request For Comment                                 | 2023-10-31             |
| Outreach to Service Providers (consent to use their lists) | 2023-10-31 (estimated) |
| Pilot Period (private testing)                             | 2023-11-14 (estimated) |
| Public Availability                                        | 2023-12-15 (estimated) |

## Target Audience

1. New service administrators (potential consumers of the list)
2. Large service providers (potential sources for the list)

## Summary

This Request for Comments describes an aggregated domain list (“CARIAD”) that IFTAS intends to curate and make available to the public online, and via the forthcoming [IFTAS FediCheck](https://docs.google.com/document/d/1aR1o1Vx34nSgqyApymTut8aVvd9PAzfUcUuNZbjrnoo/) service.

IFTAS believes the largest ActivityPub service providers, and their respective moderation teams, collectively represent a set of shared trust and safety knowledge and experience.

This policy proposal describes the process to collate, aggregate, analyse, and deliver a publicly denylist for use by new services on day one of service, reflecting the aggregate consensus of the largest service providers.

This proposal is not a comprehensive solution, nor does it meet the needs for most established communities. The proposed policy includes educational material and links to additional resources.

The proposal very specifically seeks to support a baseline starting point for new ActivityPub service providers on day one of federation.

## Motivation

New ActivityPub service providers may not fully understand the implications of open federation, and it can come as a shock to find there are federating servers that harbour malicious and inauthentic actors.

This can lead to negative consequences such as receiving large amounts of spam and abuse; being at risk of network or service abuse; negative press coverage; or being defederated themselves for not being quick enough or savvy enough to block the relevant services. In some rare instances, services have been overwhelmed with illegal media, causing trauma and service shutdown.

New service providers quickly learn there is a need to review federation policy, investigate the contentious issue of which servers to block, and where to source the relevant intelligence.

Denylist assistance is an oft-requested feature and the lack of knowledge or at-install support for denylists leads to documented cases of new administrators being overwhelmed by hate speech, trolling, network or service abuse, and spam, and are unaware of malicious instances or servers that pose a danger to their service. This highlights the need for an effective, early denylist approach to curtail the most obvious vectors for abuse and inauthentic behaviour.

As noted in The Atlantic Council Task Force for a Trustworthy Future Web report “[Scaling Trust on the Web](https://www.atlanticcouncil.org/in-depth-research-reports/report/scaling-trust/)”:

_“Federated spaces have many of the same propensities for harmful misuse by malign actors as mainstream platforms like Facebook and Twitter, while possessing few, if any, of the hard-won detection and moderation capabilities necessary to stop them. Each instance of a federated service can choose for itself what its governance approach will be. Community standards, content moderation, user reporting, and protecting against large-scale or coordinated campaigns of harassment or disinformation—even within an individual instance—require a broad array of technical, institutional, financial, and logistical competencies that federated spaces are not currently designed to support.”_

Numerous denylists exist with varying degrees of acceptance and varying scopes of intended use. However, IFTAS believes a simple, minimum necessary, day one list that reflects the broad experience of the largest proportion of Fediverse users would augment the options available to new providers.

## Guide-level explanation

CARIAD - the Consensus Aggregated Retractable IFTAS Allowlist Denylist, is a freely accessible denylist that aggregates the collective knowledge and experience of the very largest ActivityPub service providers, to produce a reference, consensus-driven denylist.

New service providers would benefit from a simple, broadly acceptable minimum necessary set of defederation recommendations. Large service providers acting as trusted sources would share their experience and collective knowledge in the pursuit of a better, safer network for all parties.

## Reference-level explanation

### CARIAD Policy Specification

The CARIAD denylist is intended to be a reflection of the defederation in the bulk of the Fediverse account coverage, and therefore source inclusion will be restricted to the largest service providers, tentatively >50,000 accounts (24 services at time of writing) or >5,000 MAU (36 services at time of writing).

_NB: at this time, we do not have consent to import these upstream lists; we will contact the eligible servers for consent if or once this proposal is in a public comment period. If we cannot obtain adequate consent, a new model will be proposed._

The following specifications are intended to reflect the operational best practices found in <https://www.rfc-editor.org/rfc/rfc6471.html>

### Intended Use

CARIAD is intended to provide the most basic, first step in ensuring the defederation of known bad actors, for new service providers.

CARIAD cannot and will not provide safety for all possible use cases. Many communities will require additional research and resources to provide more comprehensive federation management.

CARIAD is intended for new service providers seeking a minimum necessary list to manage their third-party domain federation. It is not intended to be a long term solution, and resources are available for service providers seeking to enhance their denylist to further curate the domains with which they federate.

### Source Inclusion Criteria

CARIAD will aggregate data from two sources:

1. A Do Not Interact list, comprising known sources of content deemed illegal in the preponderance of OECD nations. The DNI list currently has fewer than ten domains.
2. An aggregation of the largest ActivityPub service providers’ existing denylists

- To be eligible as a trusted source, service providers must host either 50,000 accounts, or 5,000 monthly active users.
- Any entity or individual operating more than one service that would otherwise meet inclusion, will be represented by their largest service only.
- The service provider must have been operating for at least 12 months.
- The service provider must themselves already block at least 50 domains.
- The trusted source must not themselves appear on the aggregated list.

_NB: Eligible sources will not be named or identified, nor will their metadata (“reasons”) be republished or associated with them in any way. The IFTAS CARIAD list will not disclose participation other than to observe the eligibility rules for inclusion as a trusted source. FediCheck users will be able to review unidentified, aggregate metadata in the app, but no metadata will be published to subscribed servers._

### Domain Inclusion Criteria

CARIAD will be offered in three levels, based on increasing agreement. The proposed thresholds are:\
Majority Agreement (more domains blocked or limited) - x% of the sources block or limit the domain\
Super Majority Agreement - y% of sources block or limit the domain\
Maximum Agreement (fewer domains suspended or limited) - z% of the sources block or limit the domain

_NB: proposed thresholds of 51%, 66%, 80%, and 100% agreement_

Entries will be listed with the majority recommendation, see Domain Inclusion Examples.

#### Domain Inclusion Examples

##### Example A (Decision by subset majority)

- [example.com](http://example.com/) is blocked by 14 of 20 sources, reaching super majority threshold
- The sources show 8 of 14 Suspend, 6 of 14 Silence
- [example.com](http://example.com/) is visible on majority and super majority lists, but not on maximum agreement
- [example.com](http://example.com/) is recommended for Suspend (8 of 14 majority)

##### Example B (Decision by superset majority)

- [example.com](http://example.com/) is blocked by 14 of 20 sources, reaching super majority threshold
- The sources show 8 of 14 Suspend, 6 of 14 Silence
- [example.com](http://example.com/) is visible on majority and super majority lists, but not on maximum agreement
- [example.com](http://example.com/) is recommended for Silence (8 of 20 does not meet majority)

##### Working Model

See <https://docs.google.com/spreadsheets/d/1unQXkMWLCQD8dZ13myXbhaNuGNIAC9TisoSfLdz5Kc4/> for a working model list of domains meeting inclusion criteria at various thresholds. This list is independently sourced, and is a working model only. It should _not_ be used in its current state.

_Domain Count by Threshold in Working Model:_

- 100% agreement: 25 domains
- 80% agreement: 24 domains (49 total domains >=80%)
- 75% agreement: 27 domains (76 total domains >=75%)
- 66% agreement: 44 domains (120 total domains >=66%
- 51% agreement: 63 domains (183 total domains >-51%)

### Domain Exclusion Criteria

As and when domains fail to meet inclusion, they will be delisted. The source lists will be monitored using the FediCheck database service to reaggregate the list no less than hourly. CARIAD users subscribed via FediCheck will automatically delist domains that are removed from the CARIAD database.

Trusted source domains will be safelisted by CARIAD. If a trusted source is found to be on one or more of the lists, their eligibility to serve as trusted source is rescinded.

A Web form will be made available on the CARIAD Web site to allow for delisting enquiries. While IFTAS cannot delist domains from the upstream sources, IFTAS will review delist requests and pass them on to the source domain administrators if deemed appropriate for further review.

### Listing Longevity

The list and its stratified versions will be reviewed quarterly by an IFTAS Panel to ensure the criteria are working as intended, and not causing harm to any community.

As an aggregated list, all listings are deemed temporary insofar as they are subject to the upstream sources’ inclusion criteria.

IFTAS will not itself provide expiration dates, but will seek to ensure all upstream sources are monitoring the appropriateness of their inclusion criteria. See Domain Exclusion Criteria


### Access and Availability

Access to the CARIAD denylist will be free and public. No fees will be charged for use of the list, nor for listing or delisting requests.

The CARIAD list will be made available on the IFTAS Github repository, and on the IFTAS Web site.

The CARIAD Web Site will be available at TBD and will contain all documentation, links to current lists, audit trails of additions and retractions, and a delisting enquiry Web form.

### Versioning

This policy will be versioned, and lists published subject to this policy will bear the version identifier. If this policy should be proposed to be amended in any way, IFTAS will:

- Create a beta version identifier for testing the proposed changes;
- Announce the proposed changes and a request for comments on IFTAS official accounts, in the IFTAS Github, and in regular communications, to allow a 28 day comment period;
- Upon review of comments, test the beta version in a non-production environment for 28 days;
- Upon completion of test period, close out any remaining comments and feedback, and place the new version ready for approval;
- If approved, IFTAS will announce the date of release, and make the beta version ready for production use.

While users of the associated FediCheck service will automatically reflect the latest list, public users of the list will need to review a removal file in the case that domains are delisted.

### Public Feedback

Members of the public may make enquiries about the list, or raise issues, using one of the following methods:

- Open an issue on the IFTAS Github. CARIAD will be housed at <https://github.com/iftas-org/resources/tree/main/CARIAD>
- Using the IFTAS Community Web Site CARIAD discussion forum (TBD)
- Accessing the IFTAS Denylists Working Group chat <https://matrix.to/#/#wg-denylists:matrix.iftas.org>

## Frequently Asked Questions

**What sources does the aggregation process draw from?**See Source Inclusion Criteria

**Are those sources independent?**Yes, sources must be independent and each source may only proffer one list, even if they operate multiple services (largest populated service wins).

**Do service providers share moderators or blocklist sources?**No, although ad hoc communication occurs between some/many/most providers

**How are sources combined to produce the aggregate blocklist?**Three consensus percentage thresholds are offered. The domain must appear on that percentage of the sources for it to be considered for a recommendation. Subsequently, the actions taken by the sources are counted, and a majority of actions (suspends vs. limits) decides the recommendation.

**How are sources weighted?**No weighting is applied, other than the source inclusion criteria, which precludes all but the largest providers from participating. The inference is that each moderation team’s decision is in good faith and equally valuable as a finding.

**How does the aggregator trace the provenance of its output?**Each entry is stored in a relational system that captures the source domain, the blocked domain, the severity of the block, and the datetime of the entry.

**How much of that provenance information is public?**None, as far as IFTAS is concerned. Source domains may publish their federation lists independently. IFTAS will not publish which servers are sources other than to affirm they meet the inclusion criteria.

**What happens when a CARIAD source blocks an instance because it appears on the CARIAD list?**A potential outcome of this activity is a number of domains will slowly progress to 100% agreement. This is an expected and cautiously welcomed possible outcome, monitored by frequent panel review and the publicly available list and comment process. The intent is to provide a consistent “worst of the worst” list. As such, if the sources were to review the domains listed, and investigate those domains themselves for their own review, and then add them, this should simply add greater consensus where some consensus already exists. Ongoing review will monitor this activity and ensure the lists remain fit for purpose, are not being gamed or manipulated, and are working as intended. Additionally, IFTAS participates in numerous forums where such activities are discussed, and as such IFTAS will monitor and participate in the discussions that may arise around this activity. Please note, only 25 domains currently show 100% agreement, which signals there is little to no collaboration in this space at this time.

**Is there a clean separation between work-in-progress and released denylists?**See Versioning.

**Does the aggregator perform manual review, either of the entire blocklist, or of a random sample?**An IFTAS review panel will review the lists no less than quarterly to ensure they remain fit for purpose. Ongoing monitoring of both the public feedback option and the delisting requests will occur as they arise.

**How is public feedback on the output and aggregation process itself gathered?**See Public Feedback

**What kinds of biases will sources have toward different sorts of groups?**The inclusion criteria skew to a mix of North American (US and Canadian), European, and UK service providers. This necessarily biases the list in favour of white, global north speech and prejudices, and as such should be used only by service providers who feel comfortable reflecting the aggregated views of white, global north service providers. It may be that this list is of use for a number of weeks while the service provider pursues additional research in this matter.

Additionally, the sources represent the largest service providers, who have generally favoured preserving relationships over blocking speech and content, and therefore are less likely to take action against domains that many others would consider worthy of inclusion. However, service providers of this size are also less hesitant to block a small service with few accounts, which may lead to unintended aggregation of this bias. To this end, please see Intended Use and Public Feedback

**Why are there no reasons or labels?**IFTAS is reviewing shared or common vocabularies in the Trust and Safety space, and may, in the future, undertake to label services or to publish and promote a shared vocabulary or a labelling service based on consensus or trusted flaggers. As the list is minimal in nature, and reflective of a large proportion of Fediverse accounts’ real world experience, we believe there is no need to label these services at this time. As with all denylists, they can - unfortunately - serve as a directory of the very content the service is intending to diminish, but nonetheless each domain can be reviewed by any prospective user of the list, or researched on other curated lists, hashtags, and directories of such activities.

**What is the process for review/lifecycle?**

1. IFTAS Moderator Panel review
2. IFTAS Membership review
3. Interested Party review
4. Request for Comment (Public via Github)
5. Comment review
6. 30 day test run (run the list, observe diffs, review fit for purpose)
7. Either (a) receive feedback that requires go to Step 1 Moderator Panel Review or (b) publish

Once published, the list will be monitored for domain adds, edits and deletions, public comment remains open, delisting enquiries will be reviewed, and a standing quarterly general review will occur at the Moderator Panel level.

**This list should include more/fewer domains, does not meet my personal need, does not account for x or y…**No denylist exists nor can exist that serves all possible purposes. IFTAS believes:

1. Denylisting is a necessary outcome of open federation to preserve safety and minimise harm;
2. Everyone is free to federate or defederate with anyone, at any time, for any reason - federation is a privilege, not a right;
3. While some lists already exist, many with excellent reputation and purpose, there is room for more activity using alternative methods;
4. New providers are the least served, the least aware, the least educated on the issues at hand, and this activity is specifically aimed at closing that gap;
5. Activities such as this can foster new conversation, new thought, and new activities in pursuit of better social media for all.

IFTAS is pursuing investigation into shared vocabularies, trusted flagger entities, labelling methods and options, enhancements to moderation tooling, DNSBL services, and many more resources that hopefully will be a small part of improving the general state of play with regard to shared lists, empowering service providers and their moderation teams to effectively carry out their service and mission. IFTAS in no way believes this list, or any other list, is the “right” list for everyone. However, it is hoped that this activity elevates the conversation, is inclusive of as many voices as possible, and can serve to progress the denylist and federation landscape for service providers. If this activity proves valuable and successful, IFTAS intends to continue exploring consensus methods for identifying and labelling domains and providing support to any who are engaged in creating better social media.

**Why “CARIAD”?**Cariad is the Welsh word for love. We believe helping create and preserve safety is an act of love.

## Further Reading

### Denylist Resources

CARIAD is intended to be a service provider’s first step in obtaining recommendations for limiting or defederating third-party services. It is highly recommended that service providers research additional resources to understand the threats, mitigations, and approaches to managing this activity. The following links may be of help in this regard.

#### Denylist Curators

The following curators maintain denylists as well as writing on the subject.

- <https://seirdy.one/posts/2023/05/02/fediverse-blocklists/>
- <https://writer.oliphant.social/oliphant/the-oliphant-social-blocklist>
- <https://gardenfence.github.io/>
- <https://thebad.space/> (WIP)

#### Denylist Tools

- [FediCheck](https://docs.google.com/document/d/1aR1o1Vx34nSgqyApymTut8aVvd9PAzfUcUuNZbjrnoo/) - a forthcoming denylist management tool that automates denylist additions, edits, and removals
- <https://github.com/eigenmagic/fediblockhole> - A tool for keeping a Mastodon instance blocklist synchronised with remote lists.
- <https://github.com/ineffyble/mastodon-block-tools> - a directory of denylist tools
- <https://fediseer.com/> - A crowd-sourced domain database with optional sync tool
- The hashtags #FediBlock and #FediBlockMeta can be followed to monitor on-network discussions of denylist activity

#### Server Administration Communities

Online communities are a good way to learn from experienced service providers and community managers.

- <https://matrix.to/#/#space:matrix.iftas.org> - IFTAS’ moderator community chat
- <https://matrix.to/#/#mastodon_admin:matrix.org> - Community admin chat
- <https://matrix.to/#/#mastodon_moderation:matrix.org> - Community moderation chat
- <https://matrix.to/#/#local-moderators-hub:matrix.org> - Locality-based service providers
- <https://discord.gg/jxEMxvF7> - The official Mastodon chat space

## Drawbacks

CARIAD cannot and will not provide safety for all possible use cases. Many communities will require additional research and resources to provide more comprehensive federation management. Specifically, CARIAD does not protect LGBTQ, BIPOC, BAME or other marginalised communities, and additional research will be required to better serve your membership, we recommend starting at the Further Reading section.

By definition, this list is biased to the actions and sensibilities of the moderation teams of very large service providers.

This proposal relies on the voluntary sharing of denylist data from third-party sources. They may be unwilling to share this data with IFTAS.

The CARIAD database is by definition a subset of the known inauthentic and malicious actor services that freely federate. More comprehensive lists are available, and may be more suitable for purpose.

## Rationale and alternatives

- Why is this design the best in the space of possible designs?: It is a minimum necessary list, very few other lists exist in this space, and to the best of our knowledge none have been subject to this level of peer review.
- What is the impact of not doing this?: New service providers will need to actively research their own federation decisions, with no authoritative, broadly accepted mechanism for doing so.
- Does the proposal make it easier or harder to moderate, administrate, and maintain Fediverse services?: Easier

## Prior art

E-mail is a similarly open messaging protocol, and aggregate denylists are a common threat mitigation, see <https://en.wikipedia.org/wiki/Domain_Name_System_blocklist> and <https://en.wikipedia.org/wiki/Comparison_of_DNS_blacklists>

Numerous consensus or aggregated lists exist, see Further Reading for some examples.

The following may be helpful in understanding the benefits and dangers of shared lists.

- Mansoux, A., & Roscam Abbing, R. (2020). Seven Theses on the Fediverse and the Becoming of FLOSS (pp. 124–140). Institute for Network Cultures and Transmediale. <http://urn.kb.se/resolve?urn=urn:nbn:se:mau:diva-55221>
- Zulli, D., Liu, M., & Gehl, R. (2020). Rethinking the “social” in “social media”: Insights into topology, abstraction, and scale on the Mastodon social network. New Media & Society, 22(7), 1188–1205. <https://doi.org/10.1177/1461444820912533>
- Gehl, R. W., & Zulli, D. (2022). The Digital Covenant: Non-Centralized Platform Governance on the Mastodon Social Network. Information, Communication & Society. <https://hcommons.org/deposits/item/hc:49433/>
- Rozenshtein, A. Z. (2022). Moderating the Fediverse: Content Moderation on Distributed Social Media. SSRN Electronic Journal. <https://www.journaloffreespeechlaw.org/rozenshtein2.pdf>
- Van Raemdonck, N. & Pierson, J. (2022) A conceptual framework for the mutual shaping of platform features, affordances and norms on social media Tijdschrift voor Communicatiewetenschap vol. 50 nr.4 pp.358-383 <https://cris.vub.be/ws/portalfiles/portal/92575001/TRANSLATION_Conceptual_framework_for_interaction_of_platform_features_FINAL.pdf>
- Marwick, A. E. (2021). Morally Motivated Networked Harassment as Normative Reinforcement. Social Media + Society, 7(2), 205630512110213. <https://doi.org/10.1177/20563051211021378>

## Unresolved questions

- How do we handle short-term Limits such as those that have occurred in the past to mitigate spam from a domain? How do we handle the same if it is a safelisted trusted source server?
- Should full defederation be dependent on (a) a majority of the subset of servers that action the domain or (b) a majority of all reference sources, regardless of their action?
- Some domains appear down. Do we guard against reuse of stale domains? Do we check for federation activity despite no public web presence?
- How frequently should the CARIAD database update? Assuming malware like the activitypub-troll/forkbomb type attacks (<https://github.com/mastodon/mastodon/issues/21977>), or CSAM attacks such as those that occurred on Lemmy (<https://jamie.moe/post/113630>), we probably want quick updates. What are the dangers of high frequency, especially as it may be tied to FediCheck, an automated denylist management service?
- As this list is intended to serve as a first pass baseline, what can we do to encourage service providers to graduate from this list to either actively researching their own decisions, or graduating to different lists?
- How can we best publish retractions for non-Fedicheck users (people consuming the list manually)? - likely two parts - 1. Diff file in github 2. Bot account on [mastodon.iftas.org](http://mastodon.iftas.org/) publishing retraction notices. What else makes sense?

## Future possibilities

Common vocabulary listings: IFTAS could manually review each domain and using a shared vocabulary provide standard metadata for each recommendation.\
Additional lists by size/scope: IFTAS could solicit groups of like servers to contribute to a different list, e.g. servers of size x to y, or servers for topic or community z.
