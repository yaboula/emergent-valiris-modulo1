import fs from 'node:fs';
const base = 'D:/the next level/research-evidence/';
const target = 'D:/the next level/valiris-restaurants/docs/research/';
const fork = JSON.parse(fs.readFileSync(base+'thefork-es.json','utf8')).feed.entry;
const cover = JSON.parse(fs.readFileSync(base+'covermanager-alt.json','utf8')).feed.entry;
const forkSelections = [
['13920631378','UX','negative','Editing booking notes became difficult.'],
['13899364575','COST','negative','Reports disputed contract lock-in.'],
['13865773006','UX','mixed','Likes usability; requests dark mode.'],
['13779900421','COST','negative','Reports errors and excess charges.'],
['11523088596','SYNC','negative','Booking notifications reportedly fail.'],
['11208263649','CONTENT','negative','Photo restrictions obstruct restaurant updates.'],
['11034334674','SYNC','negative','Requires reopening to refresh changes.'],
['11018486989','RELIABILITY','negative','Required update reportedly stopped working.'],
['10827571477','UX','mixed','Useful; needs clearer release explanations.'],
['9917108690','CAPACITY','negative','Party-size options produce seating mismatches.'],
['9740727969','RELIABILITY','negative','Cannot navigate on updated iPad.'],
['9244992962','SYNC','negative','Reports stale views and broken newsletters.'],
['9193451930','UX','negative','Replacement booking interface feels worse.'],
['9037438682','UX','negative','Creating reservations now takes extra steps.'],
['9035643568','RELIABILITY','negative','Reports repeated freezes after changes.'],
['9029591747','UX','negative','Update feels slow and confusing.'],
['8974566529','RELIABILITY','negative','Prolonged outage prevents reservation management.'],
['8972182297','UX','negative','New version worsens an already-poor experience.'],
['8937990872','CAPACITY','negative','Must correct automatic table assignments.'],
['8928556723','SYNC','negative','Refresh delays and booking errors.'],
];
const coverSelections = [
['13885140569','UX','positive','Useful restaurant management information.'],
['13867286111','UX','positive','Praises design and app performance.'],
['13864403714','UX','positive','Welcomes recent usability changes.'],
['13850690346','RELIABILITY','negative','Reports deteriorating service; requests development focus.'],
['13130941187','COST','positive','Finds usability worth the price.'],
['13034691580','CUSTOMER','negative','Client lookup became difficult after changes.'],
['12849131432','RELIABILITY','negative','Uses website instead of unstable app.'],
['12735386769','CUSTOMER','positive','Values reservations and own customer database.'],
['12734816055','SYNC','negative','Stale bookings and slow customer records.'],
['12716688167','RELIABILITY','negative','Update prevents opening reservation console.'],
['12713160777','UX','positive','Recommends app after recent improvements.'],
['12688060733','UX','negative','Mobile lacks web capabilities; confusing workflows.'],
['12639993129','RELIABILITY','negative','Frequent updates reportedly worsen behaviour.'],
['12634578058','RELIABILITY','negative','Update introduced freezes and failures.'],
['12630709036','SUPPORT','negative','Reports delayed callbacks and unreliable app.'],
['12572432465','RELIABILITY','negative','Cannot sign in with password.'],
['12466410872','COST','negative','Reliability disappoints relative to subscription cost.'],
['12438789242','UX','mixed','Initially complex; later finds app useful.'],
['12393436314','SYNC','negative','Reports missing notifications in review title.'],
['12225088014','SUPPORT','negative','Plans switching after unresolved errors.'],
];
const rows=[];
function addApple(entries,selections,product,appId,source) {
  for(const [key,theme,sentiment,summary] of selections){
    const e=entries.find(x=>x.id.label===key);
    if(!e)throw new Error('Missing source review '+key);
    rows.push({id:'RM-'+String(rows.length+1).padStart(3,'0'),product,date:e.updated.label.slice(0,10),rating:e['im:rating'].label,version:e['im:version'].label,key,theme,sentiment,summary,source,locator:'Apple review ID '+key,role:'App reviewer; operator role unverified',incentive:'Not disclosed'});
  }
}
addApple(fork,forkSelections,'TheFork Manager','1295795281','https://itunes.apple.com/es/rss/customerreviews/page=1/id=1295795281/sortby=mostrecent/json');
addApple(cover,coverSelections,'CoverManager','1289393829','https://itunes.apple.com/es/rss/customerreviews/id=1289393829/sortBy=mostRecent/json');
const loopy=[
['2017-10-19','5','Christos K.','General manager; sector unspecified','COST','mixed','Easy operation; Growth plan feels expensive.','Incentivized'],
['2026-06-03','5','Jason K.','Food and beverages owner','UX','mixed','Likes scanning; repeated confirmation interrupts workflow.','Non-incentivized'],
['2026-04-09','5','Dhaval D.','Restaurant operations manager','INTEGRATION','mixed','Simple stamps; advanced integrations feel limited.','Non-incentivized'],
['2026-04-21','5','Ben G.','Food and beverages director','CUSTOMER','mixed','Unsaved cards require back-office customer access.','Non-incentivized'],
['2026-04-27','4','Matthieu M.','Food and beverages director','DATA','mixed','Wants recurring database delivery and notifications.','Non-incentivized'],
['2026-05-19','5','Maitham M.','Food and beverages owner','COST','mixed','Additional staff access requires costly upgrade.','Non-incentivized'],
['2026-04-14','5','Saad A.','Food and beverages operator','RELIABILITY','mixed','Occasional errors; slow chat-only support.','Non-incentivized'],
['2024-02-09','4','Miseol K.','Restaurant owner','LOYALTY','mixed','Helpful QR migration; wants automated stamping.','Non-incentivized'],
['2022-12-22','5','Gabe S.','Food and beverages manager','LOYALTY','mixed','Customers struggle to retrieve digital cards.','Non-incentivized'],
['2026-04-09','5','Wesley C.','Food and beverages owner','CUSTOMER','mixed','Needs lookup and device-change card recovery.','Non-incentivized'],
];
for(const [date,rating,key,role,theme,sentiment,summary,incentive] of loopy){rows.push({id:'RM-'+String(rows.length+1).padStart(3,'0'),product:'Loopy Loyalty',date,rating,version:'Not stated',key:date+' '+key,theme,sentiment,summary,source:'https://www.capterra.com/p/160859/Loopy-Loyalty/reviews/',locator:key+' / '+date,role,incentive});}
fs.mkdirSync(target,{recursive:true});
let md='# Public review ledger\n\nCollected: 2026-09-28. Exactly 50 distinct reviews; one primary theme per row. Read [the method and limitations](review-mining.md) before interpreting the counts. Summaries are paraphrases, not quotations. Stars and textual sentiment can disagree.\n\n';
for(const product of ['TheFork Manager','CoverManager','Loopy Loyalty']){
 const group=rows.filter(r=>r.product===product);
 md+='## '+product+'\n\nSource: ['+(product==='Loopy Loyalty'?'Capterra public reviews':'Apple public review feed (Spain storefront)')+']('+group[0].source+'). Accessed 2026-09-28.\n\n';
 md+='| ID | Date | Stars / 5 | Version | Source locator | Primary theme | Text sentiment | Reported experience (paraphrase) |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n';
 for(const r of group)md+=`| ${r.id} | ${r.date} | ${r.rating} | ${r.version} | ${r.locator} | ${r.theme} | ${r.sentiment} | ${r.summary} |\n`;
 if(product==='Loopy Loyalty')md+='\nReview roles: RM-041 general manager (sector unspecified); RM-042 food/beverages owner; RM-043 restaurant operations manager; RM-044/045 food/beverages directors; RM-046 food/beverages owner; RM-047 food/beverages operator; RM-048 restaurant owner; RM-049 food/beverages manager; RM-050 food/beverages owner. RM-041 is marked incentivized by Capterra; RM-042–050 are marked non-incentivized. These are platform labels and self-reported roles.\n';
 else md+='\nRoles are unverified app reviewers; operational language suggests restaurant use but does not confirm employment, country, business size or purchase. Incentives are not disclosed by this feed.\n';
}
fs.writeFileSync(target+'review-ledger.md',md);
const counts={themes:{},sentiments:{},products:{},years:{}};
for(const r of rows) for(const [k,v] of [['themes',r.theme],['sentiments',r.sentiment],['products',r.product],['years',r.date.slice(0,4)]])counts[k][v]=(counts[k][v]||0)+1;
fs.writeFileSync(base+'coded-reviews.json',JSON.stringify(rows,null,2));
console.log(JSON.stringify(counts,null,2));
console.log('Unique reviews: '+new Set(rows.map(r=>r.product+'|'+r.key)).size);
