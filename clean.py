import twitter
import math

api = twitter.Api(consumer_key='puOCS7Qy8rvSvHluJDhJZcqcR',consumer_secret='cIQIzXkRxv2yJlR2GnGZPO2GGiIov7auSZrzlevGsMSVyM701p', access_token_key='625100109-E6Rc57gTnIzlpN86GnEXgFCsBN51KNuJIBEhh8oU', access_token_secret='TVHD8RkO4qIwjE5AplPhXOwgN1WTvNSVglEd6sbzBNiE0')


def get_filtered_words():
    filter = [
            '2g1c',
            '2 girls 1 cup',
            'acrotomophilia',
            'anal',
            'anilingus',
            'anus',
            'arsehole',
            'ass',
            'asshole',
            'assmunch',
            'auto erotic',
            'autoerotic',
            'babeland',
            'baby batter',
            'ball gag',
            'ball gravy',
            'ball kicking',
            'ball licking',
            'ball sack',
            'ball sucking',
            'bangbros',
            'bareback',
            'barely legal',
            'barenaked',
            'bastardo',
            'bastinado',
            'bbw',
            'bdsm',
            'beaver cleaver',
            'beaver lips',
            'bestiality',
            'bi curious',
            'big black',
            'big breasts',
            'big knockers',
            'big tits',
            'bimbos',
            'birdlock',
            'bitch',
            'black cock',
            'blonde action',
            'blonde on blonde action',
            'blow j',
            'blow your l',
            'blue waffle',
            'blumpkin',
            'bollocks',
            'bondage',
            'boner',
            'boob',
            'boobs',
            'booty call',
            'brown showers',
            'brunette action',
            'bukkake',
            'bulldyke',
            'bullet vibe',
            'bung hole',
            'bunghole',
            'busty',
            'butt',
            'buttcheeks',
            'butthole',
            'camel toe',
            'camgirl',
            'camslut',
            'camwhore',
            'carpet muncher',
            'carpetmuncher',
            'chocolate rosebuds',
            'circlejerk',
            'cleveland steamer',
            'clit',
            'clitoris',
            'clover clamps',
            'clusterfuck',
            'cock',
            'cocks',
            'coprolagnia',
            'coprophilia',
            'cornhole',
            'cum',
            'cumming',
            'cunnilingus',
            'cunt',
            'darkie',
            'date rape',
            'daterape',
            'deep throat',
            'deepthroat',
            'dick',
            'dildo',
            'dirty pillows',
            'dirty sanchez',
            'dog style',
            'doggie style',
            'doggiestyle',
            'doggy style',
            'doggystyle',
            'dolcett',
            'domination',
            'dominatrix',
            'dommes',
            'donkey punch',
            'double dong',
            'double penetration',
            'dp action',
            'eat my ass',
            'ecchi',
            'ejaculation',
            'erotic',
            'erotism',
            'escort',
            'ethical slut',
            'eunuch',
            'faggot',
            'fecal',
            'felch',
            'fellatio',
            'feltch',
            'female squirting',
            'femdom',
            'figging',
            'fingering',
            'fisting',
            'foot fetish',
            'footjob',
            'frotting',
            'fuck',
            'fucking',
            'fuck buttons',
            'fudge packer',
            'fudgepacker',
            'futanari',
            'g-spot',
            'gang bang',
            'gay sex',
            'genitals',
            'giant cock',
            'girl on',
            'girl on top',
            'girls gone wild',
            'goatcx',
            'goatse',
            'gokkun',
            'golden shower',
            'goo girl',
            'goodpoop',
            'goregasm',
            'grope',
            'group sex',
            'guro',
            'hand job',
            'handjob',
            'hard core',
            'hardcore',
            'hentai',
            'homoerotic',
            'honkey',
            'hooker',
            'hot chick',
            'how to kill',
            'how to murder',
            'huge fat',
            'humping',
            'incest',
            'intercourse',
            'jack off',
            'jail bait',
            'jailbait',
            'jerk off',
            'jigaboo',
            'jiggaboo',
            'jiggerboo',
            'jizz',
            'juggs',
            'kike',
            'kinbaku',
            'kinkster',
            'kinky',
            'knobbing',
            'leather restraint',
            'leather straight jacket',
            'lemon party',
            'lolita',
            'lovemaking',
            'make me come',
            'male squirting',
            'masturbate',
            'menage a trois',
            'milf',
            'missionary position',
            'motherfucker',
            'mound of venus',
            'mr hands',
            'muff diver',
            'muffdiving',
            'nambla',
            'nawashi',
            'negro',
            'neonazi',
            'nig nog',
            'nigga',
            'nigger',
            'nimphomania',
            'nipple',
            'nipples',
            'nsfw images',
            'nude',
            'nudity',
            'nympho',
            'nymphomania',
            'octopussy',
            'omorashi',
            'one cup two girls',
            'one guy one jar',
            'orgasm',
            'orgy',
            'paedophile',
            'panties',
            'panty',
            'pedobear',
            'pedophile',
            'pegging',
            'penis',
            'phone sex',
            'piece of shit',
            'piss pig',
            'pissing',
            'pisspig',
            'playboy',
            'pleasure chest',
            'pole smoker',
            'ponyplay',
            'poof',
            'poop chute',
            'poopchute',
            'porn',
            'porno',
            'pornography',
            'prince albert piercing',
            'pthc',
            'pubes',
            'pussy',
            'queaf',
            'raghead',
            'raging boner',
            'rape',
            'raping',
            'rapist',
            'rectum',
            'reverse cowgirl',
            'rimjob',
            'rimming',
            'rosy palm',
            'rosy palm and her 5 sisters',
            'rusty trombone',
            's&m',
            'sadism',
            'scat',
            'schlong',
            'scissoring',
            'semen',
            'sex',
            'sexo',
            'sexy',
            'shaved beaver',
            'shaved pussy',
            'shemale',
            'shibari',
            'shit',
            'shota',
            'shrimping',
            'slanteye',
            'slut',
            'smut',
            'snatch',
            'snowballing',
            'sodomize',
            'sodomy',
            'spic',
            'spooge',
            'spread legs',
            'strap on',
            'strapon',
            'strappado',
            'strip club',
            'style doggy',
            'suck',
            'sucks',
            'suicide girls',
            'sultry women',
            'swastika',
            'swinger',
            'tainted love',
            'taste my',
            'tea bagging',
            'threesome',
            'throating',
            'tied up',
            'tight white',
            'tit',
            'tits',
            'titties',
            'titty',
            'tongue in a',
            'topless',
            'tosser',
            'towelhead',
            'tranny',
            'tribadism',
            'tub girl',
            'tubgirl',
            'tushy',
            'twat',
            'twink',
            'twinkie',
            'two girls one cup',
            'undressing',
            'upskirt',
            'urethra play',
            'urophilia',
            'vagina',
            'venus mound',
            'vibrator',
            'violet blue',
            'violet wand',
            'vorarephilia',
            'voyeur',
            'vulva',
            'wank',
            'wet dream',
            'wetback',
            'white power',
            'women rapping',
            'wrapping men',
            'wrinkled starfish',
            'xx',
            'xxx',
            'yaoi',
            'yellow showers',
            'yiffy',
            'zoophilia']
    return filter


def clean_tweet(status):
    return 'Tweet from ' +  status['created_at'] + ' with the text \'' + status['text'] + '\' was flagged as inappropriate.'


def convert_date(date):
    month = {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    } [date[0]]
    day = int(date[1])
    year = int(date[2])
    return [month, day, year]


def get_tweets_in_range(statuses, start=0, stop=0):
    if start == 0 and stop == 0:
        return statuses
    statuses_in_range = []
    for status in statuses:
        full_date = status['created_at'].split()
        date = [full_date[1], full_date[2], full_date[5]]
        date = convert_date(date)
        if start[2] <= date[2] <= stop[2]:
            if date[2] == stop[2]:
                if date[0] == stop[0]:
                    if date[1] == stop[1]:
                        statuses_in_range.append(status)
                    if date[1] < stop[1]:
                        statuses_in_range.append(status)
                if date[0] < stop[0]:
                    statuses_in_range.append(status)
            elif date[2] == start[2]:
                if date[0] == start[0]:
                    if date[1] == start[1]:
                        statuses_in_range.append(status)
                    if date[1] > stop[1]:
                        statuses_in_range.append(status)
                if date[0] > start[0]:
                    statuses_in_range.append(status)
            elif date[2] < stop[2]:
                statuses_in_range.append(status)
    return statuses_in_range


def flag_tweets(handle, start=0, stop=0):
    """Takes in start and stop dates in the format: '11 13 2018' for Nov. 13 2018"""
    status_list = api.GetUserTimeline(screen_name=handle, count=200)
    statuses = [i.AsDict() for i in status_list]
    if start != 0 and stop != 0:
        start = start.split()
        start = [int(start[0]), int(start[1]), int(start[2])]
        stop = stop.split()
        stop = [int(stop[0]), int(stop[1]), int(stop[2])]
        statuses = get_tweets_in_range(statuses, start, stop)
    filtered_statuses = []
    for status in statuses:
        for word in status['text'].split():
            if word.lower() in get_filtered_words():
                if status not in filtered_statuses:
                    filtered_statuses.append(status)

    return filtered_statuses, 100*(len(filtered_statuses) / len(statuses))

def cleanedTweets(tweets):
   cleaned = []
   for status in tweets[0]:
      cleaned.append(clean_tweet(status))
   return cleaned, tweets[1]

print(cleanedTweets(flag_tweets("alxxyng",0,0)))
