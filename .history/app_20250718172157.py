from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample car data

    


car_data ={

"acura": ["ilx", "mdx", "tsx", "tl", "rdx", "zdx", "rsx", "rl", "legend", "el", "cl", "integra", "rlx", "tsx sport wagon", "tlx"],
"audi": ["a4", "a6", "q5", "a3", "sq5", "s5", "a8", "tts", "s4", "a7", "a5", "r8", "q7", "tt", "s6", "allroad quattro", "allroad", "rs 7", "rs 5", "s8", "rs 6", "cabriolet", "s7", "tt rs", "rs 4", "q3"],
"bmw": ["3 series", "6 series gran coupe", "m5", "6 series", "5 series", "x5", "x6", "x1", "4 series", "750i", "7 series", "1 series", "750li", "m3", "x3", "z4", "x5 m", "5 series gran turismo", "x6 m", "7", "z3", "m", "m4", "750lxi", "alp", "activehybrid x6", "m6", "320i", "2 series", "m6 gran coupe", "323i", "1", "3 series gran turismo", "activehybrid 7", "328i", "z4 m", "i8", "activehybrid 5", "8 series", "x4", "4 series gran coupe"],
"buick": ["verano", "enclave", "lacrosse", "rendezvous", "lesabre", "century", "park avenue", "regal", "roadmaster", "lucerne", "terraza", "rainier", "encore", "riviera", "allure"],

















"cadillac": [
    "elr", "srx", "escalade", "cts coupe", "escalade esv", "cts", "cts-v", "cts-v coupe", "escalade hybrid", "sts",
    "dts", "deville", "xlr", "seville", "eldorado", "ats", "cts wagon", "escalade ext", "catera", "xts",
    "sts-v", "cts-v wagon", "fleetwood"],
"chevrolet": [
    "cruze", "camaro", "impala", "suburban", "malibu", "silverado 2500hd", "silverado 1500", "traverse", "equinox",
    "captiva sport", "volt", "express cargo", "colorado", "express", "sonic", "hhr", "tahoe", "impala limited",
    "spark", "aveo", "g1500", "corvette", "avalanche", "2500", "tahoe hybrid", "malibu classic", "cobalt",
    "silverado 1500 classic", "uplander", "monte carlo", "trailblazer", "malibu maxx", "1500", "blazer", "cavalier",
    "venture", "s-10", "silverado 1500hd", "prizm", "s10", "ssr", "astro cargo", "silverado 3500", "tahoe limited/z71",
    "c/k 1500 series", "capt", "silverado 3500hd", "g3500", "silverado 1500 hybrid", "silverado 2500hd classic",
    "3500", "trailblazer ext", "optra", "classic", "silverado 2500", "astro", "tracker", "lumina", "corsica",
    "caprice", "black diamond avalanche", "corvette stingray", "ss", "malibu hybrid", "c/k 3500 series", "g2500",
    "comm", "uplandr", "c/k 2500 series", "silverado 3500 classic", "s-10 blazer", "spark ev"

],
"chrysler": [
    "200", "300", "town and country", "sebring", "town", "pt cruiser", "pacifica", "300m", "concorde", "lhs",
    "voyager", "aspen", "crossfire", "pt", "prowler", "cirrus", "twn&country", "le baron", "grand", "twn/cntry"
],
"dodge": [
    "avenger", "journey", "charger", "grand caravan", "nitro", "challenger", "dart", "caliber", "magnum", "durango",
    "ram pickup 1500", "ram pickup 3500", "sprinter cargo", "dakota", "neon", "stratus", "ram pickup 2500",
    "sprinter", "ram", "intrepid", "caravan", "grand", "ram3500", "b1500", "gr", "ram cargo", "spirit", "viper",
    "ram van"
],
"ford": [
    "fusion", "e-series wagon", "escape", "edge", "focus", "flex", "f-350 super duty", "fiesta", "e350", "f-150",
    "explorer", "e-series van", "e150", "expedition", "mustang", "transit connect", "taurus", "escape hybrid",
    "ranger", "fusion hybrid", "f-250 super duty", "econoline cargo", "econoline wagon", "f-450 super duty",
    "taurus x", "explorer sport trac", "five hundred", "c-max hybrid", "freestyle", "freestar", "excursion",
    "thunderbird", "windstar", "explorer sport", "escort", "f250", "contour", "f150", "mustang svt cobra",
    "shelby gt500", "c-max energi", "focus st", "expeditn", "crown victoria", "e250", "police", "crown",
    "expedition el", "fusion energi", "f-150 heritage", "expedit", "excurs", "e-150", "bronco", "f350", "350",
    "e", "windstar cargo", "tempo", "f-150 svt lightning", "aspire", "transit van", "f-250", "e-250", "e-350",
    "transit wagon"
],
"gmc": [
    "terrain", "yukon", "sierra 1500", "acadia", "yukon xl", "sierra 2500hd", "envoy xl", "canyon", "envoy xuv",
    "envoy", "savana cargo", "sonoma", "safari cargo", "sierra 3500hd", "yukon hybrid", "sierra 1500 classic",
    "sierra 2500hd classic", "sr", "savana", "sierra 1500hd", "2500", "jimmy", "sierra 2500", "suburban", "1500",
    "yukon denali", "safari", "subrbn", "sierra 3500", "sierra 1500 hybrid"
],






















"honda": [
    "accord", "cr-v", "civic", "fit", "pilot", "odyssey", "crosstour", "cr-z", "accord crosstour", "insight",
    "ridgeline", "element", "s2000", "ridgelin", "prelude", "passport", "accord hybrid", "civic del sol"
],
"hyundai": [
    "sonata", "elantra", "santa fe", "genesis", "equus", "sonata hybrid", "accent", "veloster", "elantra coupe",
    "azera", "tucson", "genesis coupe", "veracruz", "santa", "santa fe sport", "elantra gt", "entourage",
    "elantra touring", "tiburon", "xg350", "xg300"
],
"infiniti": [
    "g coupe", "g sedan", "fx", "m", "jx", "g convertible", "qx", "ex", "m37", "qx56", "g37 convertible", "g37",
    "g35", "m45", "fx35", "fx45", "q45", "qx4", "i30", "g20", "q50", "qx70", "qx60", "q60 convertible", "m35",
    "i35", "qx80", "m56", "g37 coupe", "q60 coupe", "q70", "qx50", "ex35", "j30", "fx50"
],
"jaguar": [
    "xf", "xj", "xk", "xj-series", "s-type", "x-type", "f-type", "xk-series"
],
"jeep": [
    "wrangler", "compass", "grand cherokee", "liberty", "patriot", "commander", "gr", "cherokee", "grand",
    "grand cherokee srt"
],
"kia": [
    "sorento", "optima", "k900", "rio", "soul", "forte", "sportage", "sedona", "spectra", "rondo", "borrego",
    "amanti", "cadenza", "sephia"
],
"land rover": [
    "lr4", "range rover evoque", "range rover sport", "range rover", "lr2", "range", "discovery series ii",
    "discovery", "lr3", "rrs", "freelander", "rr"
],
"lexus": [
    "rx 350", "gs 350", "es 350", "rx 450h", "ls 460", "is 250", "ct 200h", "is 350", "gx 470", "rx 400h",
    "is f", "gs 450h", "gx", "gs 430", "es 330", "gs 300", "lx", "ls 430", "rx 330", "sc 430", "es 300",
    "is 300", "rx 300", "ls 400", "gx 460", "sc 300", "sc 400", "lx 570", "es 300h", "is 250 c", "hs 250h",
    "lx 470", "gs 400", "is 350 c", "gs 460", "ls 600h l", "lx 450", "rc f", "rc 350"
],
"lincoln": [
    "mkx", "mkt", "mkz", "navigator", "town car", "mks", "mark lt", "aviator", "ls", "continental", "navigator l",
    "town", "zephyr", "blackwood", "mark viii", "mkz hybrid", "mkc"
],
"mazda": [
    "mazda2", "mazda3", "cx-9", "mazda5", "mazda6", "cx-7", "mazdaspeed mazda3", "rx8", "mpv", "mazdaspeed protege",
    "protege5", "mx-5 miata", "millenia", "cx-5", "tribute", "3", "mazdaspeed3", "6", "b-series truck",
    "mazdaspeed mazda6", "truck", "protege", "626", "b-series pickup", "mazdaspeed 3", "mazdaspeed mx-5 miata",
    "rx-8", "tribute hybrid", "b2300", "b-series"
],
















"mercedes-benz": ["s-class", "c-class", "slk-class", "e-class", "glk-class", "gl-class", "m-class", "sl-class", "sprinter", "cls-class", "g-class", "clk-class", "cl-class", "r-class", "cla-class", "sls amg", "500-class", "300-class", "400-class", "190-class", "ml55 amg", "420-class", "b-class electric drive", "sls amg gt", "gla-class"],
"mercury": ["milan", "mariner", "grand marquis", "monterey", "mountaineer", "marauder", "cougar", "sable", "milan hybrid", "mariner hybrid", "montego", "grand", "villager", "mountnr", "tracer", "mystique"],
"mini": ["cooper clubman", "cooper", "cooper countryman", "cooper coupe", "cooper roadster", "cooper paceman"],
"mitsubishi": ["outlander", "outlander sport", "lancer", "galant", "lancer sportback", "raider", "lancer evolution", "eclipse", "endeavor", "montero", "eclipse spyder", "diamante", "montero sport", "mirage", "i-miev", "3000gt"],
"nissan": ["altima", "versa", "versa note", "370z", "juke", "sentra", "rogue", "nv", "leaf", "nv200", "quest", "maxima", "xterra", "frontier", "cube", "armada", "murano", "pathfinder", "gt-r", "altima hybrid", "titan", "350z", "200sx", "rogue select", "truck", "x-trail", "murano crosscabriolet", "nv cargo", "pathfind", "300zx", "nv passenger"],
"other": ["other"],
"pontiac": ["g6", "g5", "grand prix", "solstice", "g8", "montana", "grand am", "bonneville", "sunfire", "vibe", "grand", "torrent", "g3", "montana sv6", "wave", "pursuit", "gto", "firebird", "aztek"],
    








'porsche': ['cayenne', '911', 'boxster', 'panamera', 'cayman s', 'cayman', 'carrera', 'macan'],
    'ram': ['1500', '2500', '3500', 'c/v cargo van', 'dakota', 'c/v tradesman', 'promaster cargo van', 'cv tradesman'],
    'saturn': ['vue', 'aura', 'outlook', 'ion', 'relay', 'l-series', 's-series', 'vue hybrid', 'astra', 'sky', 'l300', 'aura hybrid'],
    'scion': ['fr-s', 'tc', 'xb', 'xd', 'iq', 'xa'],
    'subaru': ['impreza wrx', 'legacy', 'forester', 'impreza', 'outback', 'b9 tribeca', 'xv crosstrek', 'tribeca', 'baja', 'brz', 'wrx'],
    'suzuki': ['verona', 'forenza', 'xl-7', 'grand vitara', 'sx4', 'grand', 'kizashi', 'xl7', 'reno', 'aerio', 'esteem', 'swift', 'equator', 'vitara', 'sidekick'],
    'toyota': ['corolla', 'sienna', 'yaris', 'camry', 'tacoma', 'fj cruiser', 'avalon', 'rav4', 'tundra', 'prius', 'camry hybrid', '4runner', 'sequoia', 'venza',
'highlander', 'highlander hybrid', 'prius plug-in', 'land cruiser', 'matrix', 'camry solara', 'celica', 'echo', 'tercel', 'pickup', 'prius v',
'prius c', 'mr2 spyder', 'previa', 'avalon hybrid', 't100', 'paseo'],
    'volkswagen': ['passat', 'cc', 'jetta', 'beetle', 'jetta sportwagen', 'gli', 'tiguan', 'gti', 'routan', 'new beetle', 'golf', 'rabbit', 'touareg 2',
'touareg', 'eos', 'phaeton', 'r32', 'jetta gli', 'eurovan', 'cabrio', 'jetta hybrid', 'beetle convertible', 'golf r', 'golf gti'],
    'volvo': ['s60', 'xc70', 'v60', 'xc60', 's80', 'xc90', 'v50', 's40', 'c70', 'c30', 'v40', 'v70', 'xc', 's90', 's70', '960', '850', '940']

}


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_models')
def get_models():
    company = request.args.get('company', '').lower()
    models = car_data.get(company, [])
    return jsonify({'models': models})

if __name__ == '__main__':
    app.run(debug=True)
