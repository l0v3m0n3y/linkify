import requests
class Client():
	def __init__(self):
		self.api="https://linkify.me/api"
		self.site_link="https://linkify.me"
		self.token=None
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36", "Content-Type": "application/json"}
	def new_loger(self,url,domain:str="linkify.me"):
		data={"url":url,"domain":domain}
		req=requests.put(f"{self.api}/new/",json=data,headers=self.headers)
		token=req.json()['redirect']
		self.headers["referer"]=f"{self.site_link}{token}"
		self.token=token.split("/")[2]
		return req.json()
	def edit_link(self,brandedUrl:str):
		data={"statsId":self.token,"brandedUrl":brandedUrl}
		return requests.put(f"{self.api}/stats/edit",json=data,headers=self.headers).json()
	def generate_loger(self,domain:str="redire.city"):
		data={"url":domain,"statsId":self.token,"domain":domain}
		return  requests.put(f"{self.api}/stats/generate",json=data,headers=self.headers).json()
	def get_logs(self):
		return requests.get(f"{self.site_link}/_next/data/9BhBhXehvlvFGh-ruCbPj/stats/{self.token}.json?stats={self.token}",headers=self.headers).json()
