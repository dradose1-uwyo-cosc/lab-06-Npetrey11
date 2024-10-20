# Nikita petrey
# UWYO COSC 1010
# 10/18/2024
# Lab 06
# Lab Section: 16
# Sources, people worked with, help given to: Python Crashcourse 3rd edition


random_string = """
jppamiqxegokaizvkyawwurhewtcxohryzptznyuedhhmawpic
pkzwuiorngdfcsgqnlyifzyaivehpiyszykqprbcsobygzhadd
yfddbulxmcnyvqhesmnybyuhxjqqmhdxwhcselasiayqhctnlw
hakethjahqnvjdowhlyzosemxkbenestxgvgncmffkcxldcmkl
itclmqdhrbdgzwtvdxwedcknbyaecvttjphtxubvhwvcvjqayy
almxuxjbcmznnzekptfzbldsjwpvringlmalwufvlppeiendur
dyophftqjkghhncwxoksqaqnpueudpygiytqgpcgjqsjbtbpzi
vaeczmyicnednjjoxkpnjmpfbgyjnbfjlweqqppodfxfzzwkuf
rldgryyhceuikimoavosuzuozthmatcgxcmkxnaxmsevkcumby
spiajlbycvrluxdkfavxidzalxuixqkxiybhfuqhcvmrhzbzse
idjwgwdwgfkyreozkyoxdvhixfejxjfgkkgobescboyfshiovu
fxdyvfsnmjzsphgmtldlaoehofcspzujghcdcxzggvunpbtglr
topplmkviuewwpoaplmbpgejmymxbyzzwbnujrlysszmxkjerb
zpiewqvgopvhmmcgwcyvxvwhdvfgsrybcozhdtwujhdbxzznkc
ergcqbetpgwrejuluqfxchlihunzbcdwboysjqenjxzbgqbycx
dybxpyztjyxpkqfvxullzkedpkjjobhymfinpvprxejktyrpai
ehjgwahpquzcmvclatdfcmattavoehnhnzveoxwnmnptxbvxto
gpcobgzdhsjevhcohkltftmrqkosknkxeylhqxkkctbnusijgr
uvecpbqmylqdaohkfaqbgeokyyipumjuaaayikdzyxfrpaieyo
uxiosjwioebsjtslblfurgcodtyaggzovzfnnyjngawiwbbtqi
kqqhnkwheolpqzasmsmbxqkeiqvogquobphewznfsnlkkizhca
cbiyvxpmjxywqvzqtshfvnfbusphggexfqzepsrduvtovdsknl
ztyuwugprkhbmktfvrenbmqgdjwnkeugtojrpqfmjhtrlcqcpq
pwsguedzgvktpwbqkhkueymjtxbvzmdfjopzkygujrjdtogssg
cxczryuqhhgjlpultkoffescpzyjrfqqabnhkfdnhkylpjamxk
uxidjkqdrkxqjqjtflebvwhcvqjciykzhrvppvxhvpedgznwty
kujglixooczrhxziasjxddfcghzlwrqcyiilpruhdfvitewxzg
dzcvmvnoskchscgoqfsojfvahlwkrslzeirlblseplcmpmbmum
ibrdamvqfstydtjopdkdcbnnmpifxckozyxzluhcqbqtpismog
ulufaajxvuizvdzioxfvypxovptkibcrjvfidomejknuggfrtp
kptwffersvqjknemkejsgspckwqisdcliuezhbeqpwgrjcqajl
huobykkbujmyuuinbwdklqfhvakyozzsxghfyownjjwqtkxgkf
ipdbjzxfogozstfsektujsvklrvecditiectuvtfibohmxxzna
cpqzeoburtquuizhypugnkvuwbdxnraareqkofhfjobrpcsuxq
nbafxlkuafbfsiuyrxdusqyasqyrwhdjrukgxdackumvairlgn
fjhenwbrdghbevgqbybpwncclolgqyuhallbqtzdywbvlzwtil
jctmsxjortnxvlbhuhkblppewjhqjzxrwgftlturxjuwfoaqpp
sgfnxwxolkbrpdmpniitoljzaxabgtnelrmryetxqypwrjdyjc
zipwbdpbazxpesmrcfuikeamtlsrgxrhzfytecenyydeemrhxj
gmdruhillntvpadzbroyygydpmonwuakruvxbdrqhtrjvoqsin
gjbarzvuqplmsmbwtqfghteoknbxmaokwlqqfoblmzsxczjzfj
mzmawtarjdtgongqqufhhdjwcinhlxcsgoltjycxrkloqozxoi
crlfmgflzzxgiiliqlksxyaydsohhahzxtsufzppftvgbpsdlx
ertfmbothijzrrdvfrnsohnwulcxvcvxngvmznhazxrgdsugij
fracotpirvqemsiuualpkpvtmtgchmowkmvoolrjfblrtwkmtr
xhawucytgwlahddkhxxfublukkdldpovqokntydhzzrxiisdwu
ujrkoewqoflyebogbwgdhriwkkoiofwtjlhxxtmzkklzbcmxhv
lrslowamkcwolbcgfkfciegdwqskuazxnycqkkggzsowcmafay
ibmkdwkqmdkjesqnjiqpijixbwjhenmsrrlpcseliiajlvcaac
zkdenxczyooloczcaahnkehbwimvieedpdlqfafbqvxvfmvabd
"""
random_string = random_string.replace("\n","") #remove all newline characters
print(f'String size = {len(random_string)}') # Print out the size for reference 
string_len = len(random_string)

print("*"*75)
# Above is a string with 2500 characters.
# Create a program that goes through and counts the occurrence of each character, excluding \n using a  dictionary
# Output each letter and its corresponding occurrence in alphabetical order
# Output which letter occurred the most 
# Output which letter occurred the least 
# Output what the percentage of the string each character is, again in alphabetical

#Tips and trick:
# You can iterate through strings like you would a list
# All characters are lowercase 
# Each letter will be PAIRED with its corresponding value 
# That is to say, this is a great use of dictionaries
    # You will  need to add the letter to the dictionary on first occurrence 
    # Then increment its corresponding count 

string = random_string
a_count = string.count("a")
b_count = string.count("b")
c_count = string.count("c")
d_count = string.count("d")
e_count = string.count("e")
f_count = string.count("f")
g_count = string.count("g")
h_count = string.count("h")
i_count = string.count("i")
j_count = string.count("j")
k_count = string.count("k")
l_count = string.count("l")
m_count = string.count("m")
n_count = string.count("m")
o_count = string.count("o")
p_count = string.count("p")
q_count = string.count("q")
r_count = string.count("r")
s_count = string.count("s")
t_count = string.count("t")
u_count = string.count("u")
v_count = string.count("v")
w_count = string.count("w")
x_count = string.count("x")
y_count = string.count("y")
z_count = string.count("z")

#Sort into dictinary
#Will need to first declare a dictionary 

letter_count = {
    "a": a_count,
    "b": b_count,
    "c": c_count,
    "d": d_count,
    "e": e_count,
    "f": f_count,
    "g": g_count,
    "h": h_count,
    "j": j_count,
    "k": k_count,
    "l": l_count,
    "m": m_count,
    "n": n_count,
    "o": o_count,
    "p": p_count,
    "q": q_count,
    "r": r_count,
    "s": s_count,
    "t": t_count,
    "u": u_count,
    "v": v_count,
    "w": w_count,
    "x": x_count,
    "y": y_count,
    "z": z_count
}
# Output: each letter and its corresponding occurrence in alphabetical order
print(letter_count)

print("*"*75)
# Output which letter occurred the most 

most_occurred = max(letter_count, key=lambda k: letter_count[k])
least_occurred = min(letter_count, key=lambda k: letter_count[k])

print(f"The letter that occurred the most is {most_occurred}")
print("*"*75)
# Output which letter occurred the least 
print(f"The letter that occurred the most is {least_occurred}")
print("*"*75)

# Output what the percentage of the string each character is, again in alphabetical

a_percent = (a_count/string_len)*100
b_percent = (b_count/string_len)*100
c_percent = (c_count/string_len)*100
d_percent = (d_count/string_len)*100
e_percent = (e_count/string_len)*100
f_percent = (f_count/string_len)*100
g_percent = (g_count/string_len)*100
h_percent = (h_count/string_len)*100
i_percent = (i_count/string_len)*100
j_percent = (j_count/string_len)*100
k_percent = (k_count/string_len)*100
l_percent = (l_count/string_len)*100
m_percent = (m_count/string_len)*100
n_percent = (n_count/string_len)*100
o_percent = (o_count/string_len)*100
p_percent = (p_count/string_len)*100
q_percent = (q_count/string_len)*100
r_percent = (r_count/string_len)*100
s_percent = (s_count/string_len)*100
t_percent = (t_count/string_len)*100
u_percent = (u_count/string_len)*100
v_percent = (v_count/string_len)*100
w_percent = (w_count/string_len)*100
x_percent = (x_count/string_len)*100
y_percent = (y_count/string_len)*100
z_percent = (y_count/string_len)*100

letter_percentage = {
    "a": f'{a_percent}%',
    "b": f'{b_percent}%',
    "c": f'{c_percent}%',
    "d": f'{d_percent}%',
    "e": f'{e_percent}%',
    "f": f'{f_percent}%',
    "g": f'{g_percent}%',
    "h": f'{h_percent}%',
    "j": f'{j_percent}%',
    "k": f'{k_percent}%',
    "l": f'{l_percent}%',
    "m": f'{m_percent}%',
    "n": f'{n_percent}%',
    "o": f'{o_percent}%',
    "p": f'{p_percent}%',
    "q": f'{q_percent}%',
    "r": f'{r_percent}%',
    "s": f'{s_percent}%',
    "t": f'{t_percent}%',
    "u": f'{u_percent}%',
    "v": f'{v_percent}%',
    "w": f'{w_percent}%',
    "x": f'{x_percent}%',
    "y": f'{y_percent}%',
    "z": f'{z_percent}%'
}
print(letter_percentage)