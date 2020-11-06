'''
Fixed And Builded Belongs To : Ibal
Special Thanks To :
	Uwewwwxyz
	DYU
	Dolphin
	Yehezkiel Bagas
	RendyTR
Supported By :
	My Lovely 
	ExcellentTeamBotsô
	OmSquad‚ô
	MomoProtectionô
	HigherBrotherTeam
	MPCORSô
	NoelV2‚ô
	Mi Botsô
	BoneToReborn
	P.K BOTS
	Spenah
©2020 NoiBotsô
'''
# Error? Contact Me : Id Line : ibalv3
from linepy import *
from liff.ttypes import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from tmp.MySplit import *
from list_module import*
loop = asyncio.get_event_loop()
line = LINE("gmail","pass")
lineMID = line.profile.mid
lineProfile = line.profile
line_poll = OEPoll(line)
status = livejson.File('status.json', True, False, 4)
waitOpen = codecs.open("wait.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
author = status["author"] #Save Your Mid In File status.json
owner = status["owner"] #Save Your Mid In File status.json
#==================
cctv = {
	"cyduk":{},
	"point":{},
	"MENTION":{},
	"sidermem":{}
}

read = {
	"readPoint": {},
	"readMember": {},
	"readTime": {},
	"ROM": {}
}
#==================
with open("temp.json", "r", encoding="utf_8_sig") as f:
	set = json.loads(f.read())
	set.update(settings)
	settings = set
with open("wait.json", "r", encoding="utf_8_sig") as f:
	waits = json.loads(f.read())
	waits.update(wait)
	wait = waits
def backupData():
	try:
		backup = settings
		f = codecs.open('temp.json','w','utf-8')
		json.dump(backup,f,sort_keys=True,indent=4,ensure_ascii=False)
		backup = wait
		f = codecs.open('wait.json','w','utf-8')
		json.dump(backup,f,sort_keys=True,indent=4,ensure_ascii=False)
		backup = status
	except Exception as error:
		logError(error)
		return False
def speed_fetch():
	start = time.time()
	get = line.getProfile()
	taken = time.time() - start
	took = time.time() - start
	return "Speed Fetch ‚ô™\n- Took : %.3fms‚ô™\n- Taken : %.6fms‚ô™" % (took,taken)
def sendMention(to, mid, firstmessage, lastmessage):
	try:
		arrData = ""
		text = "%s " %(str(firstmessage))
		arr = []
		mention = "@x "
		slen = str(len(text))
		elen = str(len(text) + len(mention) - 1)
		arrData = {'S':slen, 'E':elen, 'M':mid}
		arr.append(arrData)
		text += mention + str(lastmessage)
		line.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		logError(error)
		line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
def sendMessageCustom(to, text, icon , name):
	annda = {'MSG_SENDER_ICON': icon,
		'MSG_SENDER_NAME':  name,
	}
	line.sendMessage(to, text, contentMetadata=annda)
def mentions(to, text="", mids=[]):
	arrData = ""
	arr = []
	mention = "@IbalxDevi  "
	if mids == []:
		raise Exception("Invalid mids")
	if "@!" in text:
		if text.count("@!") != len(mids):
			raise Exception("Invalid mids")
		texts = text.split("@!")
		textx = ""
		for mid in mids:
			textx += str(texts[mids.index(mid)])
			slen = len(textx)
			elen = len(textx) + 15
			arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
			arr.append(arrData)
			textx += mention
		textx += str(texts[len(mids)])
	else:
		textx = ""
		slen = len(textx)
		elen = len(textx) + 15
		arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
		arr.append(arrData)
		textx += mention + str(text)
	line.sendMessage(to, textx, {'AGENT_NAME':'line OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(line.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + line.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def command(text):
	noi = text.lower()
	if settings["setKey"] == True:
		if noi.startswith(settings["keyCommand"]):
			cmd = noi.replace(settings["keyCommand"],"")
		else:
			cmd = "Undefined Command"
	else:
		cmd = text.lower()
	return cmd
def restartBot():
	python = sys.executable
	os.execl(python,python,*sys.argv)
def changeVideoAndPictureProfile(pict, vids):
	try:
		files = {'file': open(vids, 'rb')}
		obs_params = line.genOBSParams({'oid': lineMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
		data = {'params': obs_params}
		r_vp = line.server.postContent('{}/talk/vp/upload.nhn'.format(str(line.server.line_OBS_DOMAIN)), data=data, files=files)
		if r_vp.status_code != 201:
			return "Failed..."
		line.updateProfilePicture(pict, 'vp')
		return "Success..."
	except Exception as e:
		raise Exception("Error! {}".format(str(e)))
		os.remove("ExcellentTeamBots.mp4")
def siderMembers(to, mid):
	try:
		arrData = ""
		textx = "Sider Terus,Sini Gabung Chat".format(str(mid))
		arr = []
		no = 1
		num = 2
		for i in mid:
			mention = "@IbalxDevi\n"
			slen = str(len(textx))
			elen = str(len(textx) + len(mention) - 1)
			arrData = {'S':slen, 'E':elen, 'M':i}
			arr.append(arrData)
			textx += mention
			if no < len(mid):
				no += 1
				textx += "%i. " % (num)
				num=(num+1)
			else:
				try:
					no = "\n {} ".format(str(line.getGroup(to).name))
				except:
					no = "\n Success "
		line.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
	except Exception as error:
		line.sendMessage(to, "[ INFO ] Error :\n" + str(error))
#===============
devq = """Hello @!
 Selfbot Edition!
©2020 NoiBotsô
      
 Menu Commands :
     Media
     Profile
     About
     Steal
     Sider On/Off
     Logout
     Restart
"""
medias = """Hello @!
 Selfbot Edition!
©2020 NoiBotsô
      
 Media Commands :
     Joox [ Query ]
     KBBI [ Query ]
     Corona Indo
     Hentai
     Gempa
Note : Without Brackets!
"""
profiles = """Hello @!
 Selfbot Edition!
©2020 NoiBotsô
      
 Profile Commands :
     MyName
     MyBio
     MyPicture
     MyCover
     ChangeVideo [ Url YouTube ]
Note : Without Brackets!
"""
steals = """Hello @!
 Selfbot Edition!
©2020 NoiBotsô
      
 Steal Commands :
     Media
     Profile
     Self
     Settings
     Steal
     Chat @Tag [ Text ]
Note : Without Brackets!
"""
#==================
async def ibal_devi(op):
	try:
		if op.type == 0:
			return
		if op.type == 5:
			pesan = ["Haiiüòâ","Thanks For Add Me"] #You Can Custome It
			rndm = random.choice(pesan)
			line.sendMessage(op.param1, rndm)
		if op.type == 25:
			msg = op.message
			text = str(msg.text)
			msg_id = msg.id
			reply = msg.id
			receiver = msg.to
			sender = msg._from
			ibal = command(text)
			if msg.toType == 0 and sender != line.profile.mid:
				to = sender
			else:
				to = receiver
			if msg.contentType == 0:
				for ibal in ibal.split(" & "):
					if ibal == "ping" or ibal == "":
						line.sendMention(to, "Yes? @! Im Here","",[sender])
					elif ibal == "speed":
						line.sendReplyMessage(msg.id, to, speed_fetch())
					elif ibal == "help":
						line.sendMention(to, devq,"",[sender])
					elif ibal == "media":
						line.sendMention(to, medias,"",[sender])
					elif ibal == "profile":
						line.sendMention(to, profiles,"",[sender])
					elif ibal == "steal":
						line.sendMention(to, steals,"",[sender])
					elif ibal == "about":
						h = line.getContact("ucf9bf411b5ee4c9e6a1faa0be27d94e9")
						groups = line.getGroupIdsJoined()
						contactlist = line.getAllContactIds()
						kontak = line.getContacts(contactlist)
						ac = subprocess.getoutput('lsb_release -a')
						am = subprocess.getoutput('cat /proc/meminfo')
						ax = subprocess.getoutput('lscpu')
						core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
						python_imp = platform.python_implementation()
						python_ver = platform.python_version()
						for devi in ac.splitdevis():
							if 'Description:' in devi:
								osi = devi.split('Description:')[1].replace('  ','')
						for devi in ax.splitdevis():
							if 'Architecture:' in devi:
								architecture =  devi.split('Architecture:')[1].replace(' ','')
						for devi in am.splitdevis():
							if 'MemTotal:' in devi:
								mem = devi.split('MemTotal:')[1].replace(' ','')
							if 'MemFree:' in devi:
								fr = devi.split('MemFree:')[1].replace(' ','')
						ret_ = "About System :\n\n"
						ret_ +="OS System : {}\n".format(osi)
						ret_ +="Language : {}\n".format(python_imp)
						ret_ +="Version : {}\n".format(python_ver)
						ret_ +="Architecture : {}\n".format(architecture)
						ret_ +="CPU Core : {}\n".format(core)
						ret_ +="Memory : {}\n".format(mem)
						ret_ +="Free Memory : {}".format(fr)
						ret_ += "About Bots :\n\n"
						ret_ += "\nCreator : {}".format(h.displayName)
						ret_ += "\nGroup : {}".format(str(len(groups)))
						ret_ += "\nFriend : {}".format(str(len(kontak)))
						ret_ += "\nType : SelfbotBot"
						line.sendReplyMessage(msg.id, to, str(ret_))
					elif ibal == 'logout':
						line.sendReplyMention(to,"User @! Has Been Logout ","",[sender])
						time.sleep(3)
						sys.exit('Logout')
					elif ibal == "restart":
						line.sendReplyMessage(msg.id,to,"Please Wait ")
						restartBot()
					elif ibal == 'sider on':
						try:
							line.sendReplyMessage(msg.id,to, "Check Sider Set To Enable")
							del cctv['point'][to]
							del cctv['sidermem'][to]
							del cctv['cyduk'][to]
						except:
							pass
						cctv['point'][to] = msg.id
						cctv['sidermem'][to] = ""
						cctv['cyduk'][to]=True
					elif ibal == 'sider off':
						if to in cctv['point']:
							cctv['cyduk'][to]=False
							line.sendReplyMessage(msg.id,to, "Check Sider Set To Disable")
						else:
							line.sendReplyMessage(msg.id,to, "Check Sider Has Been Disable")
#=====================================================
#Profile
					elif ibal.startswith('pc '):
						try:
							if 'MENTION' in msg.contentMetadata.keys()!=None:
								key = eval(msg.contentMetadata["MENTION"])
								key1 = key["MENTIONEES"][0]["M"]
								nama = line.getContact(key1).displayName
								anu = line.getContact(key1)
								if len(ibal.split(" ")) >= 2:
									mid  = "{}".format(key1)
									text = "{}".format(str(ibal.replace(ibal.split(" ")[0]+" ","")))
									icon = "http://dl.profile.line.naver.jp/{}".format(anu.pictureStatus)
									name = "{}".format(anu.displayName)
									b = [sendMessageCustom(key1, text, icon, name)];line.sendMention(to, '„Äå Personal Chat „Äç\n@! Please Cek My Pc','',[key1])
						except Exception as e:
							line.sendReplyMessage(msg.id, to, f" Notification Error \n {e}")
					elif ibal.startswith("changevideo "):
						try:
							sep = text.split(" ")
							link = text.replace(sep[0] + " ","")
							line.sendReplyMessage(msg.id, to, "Starting Download....")
							pic = "https://obs.line-scdn.net/{}".format(line.getProfile().pictureStatus)
							subprocess.getoutput(f'youtube-dl --format mp4 --output NoiBots.mp4 {link}')
							pict = line.downloadFileURL(pic)
							vids = "NoiBots.mp4"
							time.sleep(2)
							changeVideoAndPictureProfile(pict, vids)
							line.sendReplyMessage(msg.id, to, "Success....")
							os.remove("NoiBots.mp4")
						except Exception as e:
							line.sendReplyMessage(msg.id,to,str(e))
					elif ibal == "mypicture":
						path = line.getContact(sender).pictureStatus
						line.sendReplyMessage(msg.id,to,"https://obs.line-scdn.net/{}".format(str(path)))
					elif ibal == "mycover":
						image = line.getProfileCoverURL(sender)
						path = str(image)
						line.sendReplyMessage(msg.id,to,path)
					elif ibal == "myname":
						line.sendReplyMessage(msg.id,to," Name \n"+str(ibal.getContact(sender).displayName))
					elif ibal == "mybio":
						line.sendReplyMessage(msg.id,to," Bio \n"+str(ibal.getContact(sender).statusMessage))
#=================================================
#Steal
					elif ibal.startswith("getpicture "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								line.sendReplyMessage(msg.id,to,f"https://obs.line-scdn.net/{line.getContact(ls).pictureStatus}")
					elif ibal.startswith("getcover "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								image = line.getProfileCoverURL(ls)
								path = str(image)
								line.sendReplyMessage(msg.id,to,path)
					elif ibal.startswith("getbio "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								line.sendReplyMessage(msg.id,to," Status Message ï\n" + str(line.getContact(ls).statusMessage))
					elif ibal.startswith("getname "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								line.sendReplyMessage(msg.id,to," Name ï\n" + str(line.getContact(ls).displayName))
					elif ibal.startswith("getcontact "):
						if 'MENTION' in msg.contentMetadata.keys()!= None:
							names = re.findall(r'@(\w+)', text)
							mention = ast.literal_eval(msg.contentMetadata['MENTION'])
							mentionees = mention['MENTIONEES']
							lists = []
							for mention in mentionees:
								if mention["M"] not in lists:
									lists.append(mention["M"])
							for ls in lists:
								contact = line.getContact(ls)
								mi_d = contact.mid
								line.sendContact(to, mi_d)
					elif ibal.startswith("grouplist"):
						groups = line.groups
						ret_ = "Group List"
						no = 0 + 1
						for gid in groups:
							group = line.getGroup(gid)
							ret_ += "\n {}. {} | {} ".format(str(no), str(group.name), str(len(group.members)))
							no += 1
						ret_ += "\n Total {} Groups ".format(str(len(groups)))
						line.sendReplyMessage(msg.id,to, str(ret_))
					elif ibal == "tagall" or ibal == "mentionall" or ibal == "dor":
						group = line.getGroup(to)
						member = [a.mid for a in group.members]
						member.remove(line.profile.mid)
						line.datamention(to,"Mention Members",member)
#=================================================
#Media
					elif ibal.starswith("joox "):
						sep = ibal.split(" ")
						queryy = ibal.replace(sep[0] + " ","")
						url = json.loads(requests.get(f"https://mnazria.herokuapp.com/api/jooxnich?search={queryy}").text)
						line.sendReplyImageWithURL(msg.id, to, main["result"]["album_url"])
						line.sendReplyMessage(msg.id, to, main["lirik"])
						line.sendAudioWithURL(to, main["result"]["mp3Url"])
					elif ibal == "corona indo":
						r = requests.get("https://ibalapi.herokuapp.com/api/kawalcorona")
						data = json.loads(r.text)
						ret = "CORONA INFO\n"
						ret += "\n Country : "+str(data["result"]["city"])
						ret += "\n Death : "+str(data["result"]["death"])
						ret += "\n Healed : "+str(data["result"]["heal"])
						ret += "\n Case : "+str(data["result"]["opname"])
						ret += "\n Positive : "+str(data["result"]["positive"])
						line.sendReplyMessage(msg.id,to,str(ret))
					elif ibal.startswith("kbbi "):
						sep = ibal.split(" ")
						text = ibal.replace(sep[0] + " ","")
						result = requests.get(f"https://mnazria.herokuapp.com/api/kbbi?search={text}")
						data = result.json()
						a = "KBBI :\n"
						a += "\n" + str(data["result"][0])
						line.sendReplyMessage(msg.id,to,str(a))
					elif ibal == "hentai":
						r = json.loads(requests.get("https://mnazria.herokuapp.com/api/picanime?list=lewd").text)
						line.sendReplyImageWithURL(msg.id, to, r["gambar"])
					elif ibal == "gempa":
						r = json.loads(requests.get("https://mnazria.herokuapp.com/api/bmkg-gempa").text)
						line.sendReplyMessage(msg.id, to, r["result"])
#============================================
#End
		if op.type == 55:
			try:
				if op.param1 in read['readPoint']:
					if op.param2 in read['readMember'][op.param1]:
						pass
					else:
						read['readMember'][op.param1] += op.param2
					read['ROM'][op.param1][op.param2] = op.param2
				if cctv['cyduk'][op.param1]==True:
					if op.param1 in cctv['point']:
						Name = line.getContact(op.param2).displayName
						if Name in cctv['sidermem'][op.param1]:
							pass
						else:
							cctv['sidermem'][op.param1] += "~ " + Name
							siderMembers(op.param1, [op.param2])
							contact = line.getContact(op.param2)
					backupData()
	except Exception as error:
		error = traceback.format_exc()
def run_bot():
	while True:
		try:
			ops = line_poll.singleTrace(count=50)
			if ops != None:
				for op in ops:
					loop.run_until_complete(ibal_devi(op))
					line_poll.setRevision(op.revision)
		except TalkException as error:
			traceback.print_tb(error.__traceback__)
if __name__ == "__main__":
	run_bot()