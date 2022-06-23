import requests

url = "https://www.yahoo.com/ads.txt"
# out={"Pubmatic.com": {reseller:5 , direct:1}}

domain = {}
content = requests.get(url).text.split("\n")
for line in content:
    l_list = line.split(",")
    if '.' in l_list[0] and len(l_list) > 2:  # to extract required line
        if l_list[0] in domain:
            d = domain[l_list[0]]
            if "DIRECT" in line and "DIRECT" in d:
                d["DIRECT"] += 1
            else:  # Assuming there are two type DIRECT or RESELLER
                d["RESELLER"] += 1
        else:
            if "DIRECT" in line:
                domain[l_list[0]] = {"DIRECT": 1, "RESELLER": 0}
            else:
                domain[l_list[0]] = {"DIRECT": 0, "RESELLER": 1}

print(domain)
# output={'advertising.com': {'DIRECT': 14, 'RESELLER': 6}, 'yahoo.com': {'DIRECT': 93, 'RESELLER': 2}, 'aax.media': {'DIRECT': 2, 'RESELLER': 0}, 'Media.net': {'DIRECT': 0, 'RESELLER': 1}, 'sharethrough.com': {'DIRECT': 0, 'RESELLER': 3}, 'indexexchange.com': {'DIRECT': 3, 'RESELLER': 24}, 'appnexus.com': {'DIRECT': 1, 'RESELLER': 26}, 'pubmatic.com': {'DIRECT': 5, 'RESELLER': 38}, 'adpushup.com': {'DIRECT': 1, 'RESELLER': 0}, 'google.com': {'DIRECT': 7, 'RESELLER': 61}, 'openx.com': {'DIRECT': 1, 'RESELLER': 22}, 'rubiconproject.com': {'DIRECT': 5, 'RESELLER': 26}, 'yieldmo.com': {'DIRECT': 0, 'RESELLER': 4}, 'onetag.com': {'DIRECT': 0, 'RESELLER': 2}, 'sonobi.com': {'DIRECT': 0, 'RESELLER': 2}, 'contextweb.com': {'DIRECT': 0, 'RESELLER': 8}, '33across.com': {'DIRECT': 0, 'RESELLER': 3}, 'xandr.com': {'DIRECT': 0, 'RESELLER': 3}, 'smartadserver.com': {'DIRECT': 0, 'RESELLER': 3}, '152media.info': {'DIRECT': 0, 'RESELLER': 1}, 'amxrtb.com': {'DIRECT': 0, 'RESELLER': 1}, 'consumable.com': {'DIRECT': 0, 'RESELLER': 1}, 'lijit.com': {'DIRECT': 2, 'RESELLER': 4}, 'connectad.io': {'DIRECT': 0, 'RESELLER': 1}, 'rhythmone.com': {'DIRECT': 3, 'RESELLER': 2}, 'smaato.com': {'DIRECT': 0, 'RESELLER': 2}, 'sovrn.com': {'DIRECT': 1, 'RESELLER': 2}, 'spotx.tv': {'DIRECT': 1, 'RESELLER': 21}, 'spotxchange.com': {'DIRECT': 1, 'RESELLER': 13}, 'telaria.com': {'DIRECT': 0, 'RESELLER': 3}, 'tremorhub.com': {'DIRECT': 0, 'RESELLER': 11}, 'triplelift.com': {'DIRECT': 1, 'RESELLER': 3}, 'EMXDGT.com': {'DIRECT': 0, 'RESELLER': 2}, 'conversantmedia.com': {'DIRECT': 1, 'RESELLER': 1}, 'gumgum.com': {'DIRECT': 1, 'RESELLER': 0}, 'kargo.com': {'DIRECT': 0, 'RESELLER': 1}, 'media.net': {'DIRECT': 0, 'RESELLER': 2}, 'themediagrid.com': {'DIRECT': 0, 'RESELLER': 1}, 'adops.com': {'DIRECT': 1, 'RESELLER': 0}, 'freewheel.tv': {'DIRECT': 0, 'RESELLER': 3}, 'video.unrulymedia.com': {'DIRECT': 1, 'RESELLER': 1}, 'springserve.com': {'DIRECT': 0, 'RESELLER': 3}, 'spotim.market': {'DIRECT': 2, 'RESELLER': 0}, 'openweb.market': {'DIRECT': 1, 'RESELLER': 0}, 'adtech.com': {'DIRECT': 0, 'RESELLER': 1}, 'pubMatic.com': {'DIRECT': 1, 'RESELLER': 0}, 'adyoulike.com': {'DIRECT': 1, 'RESELLER': 0}, 'Kargo.com': {'DIRECT': 1, 'RESELLER': 0}, 'xad.com': {'DIRECT': 0, 'RESELLER': 1}, 'nsightvideo.com': {'DIRECT': 1, 'RESELLER': 0}, 'districtm.io': {'DIRECT': 0, 'RESELLER': 1}, 'richaudience.com': {'DIRECT': 0, 'RESELLER': 1}, 'twiago.com': {'DIRECT': 0, 'RESELLER': 2}, 'smartclip.net': {'DIRECT': 1, 'RESELLER': 2}, 'aps.amazon.com': {'DIRECT': 0, 'RESELLER': 1}, 'btrll.com': {'DIRECT': 3, 'RESELLER': 0}, 'lkqd.net': {'DIRECT': 1, 'RESELLER': 3}, 'aol.com': {'DIRECT': 1, 'RESELLER': 0}, 'teads.tv': {'DIRECT': 2, 'RESELLER': 0}, 'vindicosuite.com': {'DIRECT': 0, 'RESELLER': 1}, 'lkqd.com': {'DIRECT': 0, 'RESELLER': 1}, 'mediabong.com': {'DIRECT': 0, 'RESELLER': 7}, 'beachfront.com': {'DIRECT': 0, 'RESELLER': 1}}