# Include Mastodon.Social Blocklist At Install
- RFC Name: 0001-include-ms-blocklist 
- RFC PR: iftas-org/rfcs#0001
- Start Date: 2023-05-24

## Target Audience

[target-audience]: #target-audience

* IFTAS-WG-Blocklists
* Mastodon development team
* Mastodon server operators
* Mastodon community managers

## Summary

[summary]: #summary

Include the most current version of the mastodon.social federation domain blocklist in the core installation files, such that a newly-created Mastodon service begins operations with the same federation domain blocklist as the reference mastodon.social Web site

(A copy of the blocklist is maintained at https://codeberg.org/oliphant/blocklists/src/branch/main/blocklists/mastodon.social.csv including some domains that have been obfuscated and are unimportable through routine means)

## Motivation

[motivation]: #motivation

Numerous hobbyists and newcomers to Mastodon service provision are unaware of the full extent of the large number of Mastodon servers with which they will immediately federate content once installation is complete. A known number of these servers are created and maintained expressly for the purpose of allowing inauthentic activity, leading to documented cases of newly-created servers being overwhelmed with hate speech, trolling, brigading and spam.

The mastodon.social Web site, operated by the Mastodon development team, maintains a federation domain blocklist for its members, and it therefore reflects the overall mission and sensibility of the Mastodon project.

Including the mastodon.social federation domain blocklist as part of a routine Mastodon installation will prevent a large proportion of unwanted federation by newcomer service providers well before they have the opportunity to learn of the need for blocklist management.

Blocklists are an oft-requested feature e.g. https://github.com/mastodon/mastodon/discussions/18143, https://www.reddit.com/r/Mastodon/comments/mvebvj/ive_set_up_a_new_instance_can_i_get_a_list_of/, https://github.com/mastodon/mastodon/issues/21666 

## Guide-level explanation

[guide-level-explanation]: #guide-level-explanation

Upon installation, Mastodon freely federates with any and all compatible software. As of the date of this RFC, Mastodon includes a function to selectively block certain domains from federating. However, this blocklist is unpopulated, and it is incumbent upin the service provider to first learn that a blocklist is necessary, then research sources for blocklist recommendations, then enter the blocks using the Web-based interface unless the service provider is sufficiently versed in operatin gcomplex blocklist management software.

While there are numerous options for importing blocklists, IFTAS believes the creators of federating software have a duty of care to their users "out of the box".

Mastodon is created by Mastodon gGmbH, a German non-profit. This entity also operates mastodon.social - a community service that employs a blocklist managed and maintained by Mastodon gGmbH.

This change would ensure that all new installations of Mastodon begin operations with a copy of the Mastodon gGmbH federation domain blocklist, freely editable by any service provider to better reflect their specific requirements.

This would have the effect of defederating third-party service providers who have a demonstrated negative impact on the Fediverse and its reputation. This protects new service providers and users of the Mastodon software, and reduces harm.

While IFTAS believes more robust and varied approaches to federation domain blocklist management are required, this change represents a good faith first effort in reducing harm on the Fediverse.

## Reference-level explanation

[reference-level-explanation]: #reference-level-explanation

There are no interactions with other features. No impact is anticipated.

## Drawbacks

[drawbacks]: #drawbacks

Some service providers wish to federate with known bad actors. Generally, this reflects either a desire to monitor or participate with operators of servers appearing on the mastodon.social blocklist. These providers are free to remove any blocks they do not wish to maintain.

Some portions of the community believe that blocking any service that has not specifically harmed them personally is tantamount to unwanted and unwarranted censorship. This may lead to debate about the virtue of acting as an arbiter of what constitutes allowable speech on the Fediverse.

Some service providers may feel the inclusion of an arbitrary blocklist is over-reach by Mastodon gGmbH. However, the service providers most equipped to understand why they may not want an arbitrary blocklist are generally also the best equipped to modfiy or remove the blocklist themselves. This change is intended to serve the less-technically-capable and less-aware service providers who have no history or experience with the project, the software, or federated protocols.

## Rationale and alternatives

[rationale-and-alternatives]: #rationale-and-alternatives

- Why is this design the best in the space of possible designs?

This design is low-impact, requires no functional changes, and is demonstrably effective to the degree mastodon.social is considered a reasonable example of a functioning community.

- What other designs have been considered and what is the rationale for not choosing them?

Various options such as subscribing to third-party blocklists, using third-party blocklist management tools, or operating as unfederated by default would require significant work and debate.

- What is the impact of not doing this?

Mastodon will continue to be considered "unsafe" by a portion of the ocmmunity, and remain open to negative feedback from adopters, trust and safety practitioners, the press, and managers of communities created specifcally to offer a safe space for civil speech.

- Does the proposal make it easier or harder to moderate, administrate, and maintain Fediverse services?

This proposal significantly improves the ability of Mastodon service providers to operate and moderate their service on day one.

## Prior art

[prior-art]: #prior-art

Centralised social media services provide content and conduct moderation as a service to their entire member base. Mastodon is explicitly decentralised, and therefore has no such ability.

## Unresolved questions

[unresolved-questions]: #unresolved-questions

- What parts of the design do you expect to resolve through the RFC process before this gets merged?

A general consensus that while not universally accetped as the best fit for many communities, the mastodon.social blocklist represents a reasonable starting place for installers of the Mastodon software.

A list of reference posts or threads describing the issue by new server operators, e.g.
- https://law-and-politics.online/@Teri_Kanefield/110306278210932092 , https://law-and-politics.online/@Teri_Kanefield/110307712306870004 , https://law-and-politics.online/@Teri_Kanefield/110307362800589641 
- https://mastodon.cloud/@tomcoates/109400361263621840 , http://plasticbag.org/mastodon/
 

- What related issues do you consider out of scope for this RFC that could be addressed in the future independently of the solution that comes out of this RFC?

Automated blocklist management via subscription to a third-party blocklist

# Future possibilities

[future-possibilities]: #future-possibilities

IFTAS-WG-Blocklists is considering numerous enhancements to the blocklist processes for Activitypub software that will require implementation by the various implmenters.
