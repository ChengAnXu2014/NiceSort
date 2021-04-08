import re
import os
import sublime
import sublime_plugin


class NiceSortCommand(sublime_plugin.WindowCommand):
	def run(self):
		rotNam=self.window.folders()[0]
		file_lst=os.listdir(rotNam)
		numStr_lst=["000"]
		i=0
		while i<999:
			i+=1
			if i<10:
				numStr_lst.append("00"+str(i))
			elif i<100:
				numStr_lst.append("0"+str(i))
			else:
				numStr_lst.append(str(i))


		for filNam in file_lst:
			(basNam, exNam)=os.path.splitext(filNam)
			namIdx=re.match("^(.+?)([0-9]+)$", basNam).group(2)
			if not namIdx:
				continue

			newBas=basNam.replace(namIdx, numStr_lst[int(namIdx)])
			newFil=newBas+exNam
			os.rename(os.path.join(rotNam, filNam), os.path.join(rotNam, newFil))








