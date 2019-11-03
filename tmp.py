# -*- coding: utf-8 -*-


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)
        self.tts = ALProxy('ALTextToSpeech')  # ←追記
        self.TimeLine = [
			['ろせんバス', 'あつぎバスセンター', '10:20'],
			['ろせんバス', 'あつぎバスセンター', '10:50'],
			['ろせんバス', 'あつぎバスセンター', '11:20'],
			['ろせんバス', 'あつぎバスセンター', '11:50'],
			['ろせんバス', 'あつぎバスセンター', '12:20'],
			['ろせんバス', 'あつぎバスセンター', '12:50'],
			['ろせんバス', 'あつぎバスセンター', '13:20'],
			['りんじバス', 'ほんあつぎえき', '13:25'],
			['りんじバス', 'ほんあつぎえき', '13:45'],
			['ろせんバス', 'あつぎバスセンター', '13:50'],
			['ろせんバス', 'あつぎバスセンター', '14:20'],
			['りんじバス', 'ほんあつぎえき', '14:25'],
			['りんじバス', 'ほんあつぎえき', '14:45'],
			['ろせんバス', 'あつぎバスセンター', '14:50'],
			['りんじバス', 'ほんあつぎえき', '15:05'],
			['ろせんバス', 'あつぎバスセンター', '15:20'],
			['りんじバス', 'ほんあつぎえき', '15:35'],
			['ろせんバス', 'あつぎバスセンター', '15:50'],
			['りんじバス', 'ほんあつぎえき', '15:55'],
			['りんじバス', 'ほんあつぎえき', '16:15'],
			['ろせんバス', 'あつぎバスセンター', '16:20'],
			['りんじバス', 'ほんあつぎえき', '16:45'],
			['ろせんバス', 'あつぎバスセンター', '16:50'],
			['りんじバス', 'ほんあつぎえき', '17:05'],
			['ろせんバス', 'あつぎバスセンター', '17:20'],
			['りんじバス', 'ほんあつぎえき', '17:25'],
			['ろせんバス', 'あつぎバスセンター', '17:50'],
			['りんじバス', 'ほんあつぎえき', '17:55'],
			['りんじバス', 'ほんあつぎえき', '18:15'],
			['ろせんバス', 'あつぎバスセンター', '18:20'],
			['ろせんバス', 'あつぎバスセンター', '18:50'],
			['りんじバス', 'ほんあつぎえき', '19:05'],
			['ろせんバス', 'あつぎバスセンター', '19:20'],
			['ろせんバス', 'あつぎバスセンター', '19:50'],
			['ろせんバス', 'あつぎバスセンター', '20:20'],
			['ろせんバス', 'あつぎバスセンター', '20:45'],
			['ろせんバス', 'あつぎバスセンター', '21:45'],
			['ろせんバス', 'あつぎバスセンター', '6:20'],
			['ろせんバス', 'あつぎバスセンター', '6:50'],
			['ろせんバス', 'あつぎバスセンター', '7:20'],
			['ろせんバス', 'あつぎバスセンター', '7:50'],
			['ろせんバス', 'あつぎバスセンター', '8:20'],
			['ろせんバス', 'あつぎバスセンター', '8:50'],
			['ろせんバス', 'あつぎバスセンター', '9:20'],
			['しゅうバス', 'あつぎバスセンター', '9:50'],
        ]
        pass

    def select_timedate(self, limit=3):
        import datetime
        d = datetime.datetime
        now = d.now().strftime('%H:%M:%S')
        now = d.strptime(now, '%H:%M:%S')
        basedate = []
        index = limit
        for timedate in self.TimeLine:
            if d.strptime(timedate[2], '%H:%M') > now:
                basedate.append(timedate)
                index -= 1
                if index == 0:
                    return basedate
        return

    def remaining_second(self, date_time):
        import datetime
        d = datetime.datetime
        now = d.now().strftime('%H:%M:%S')
        now = d.strptime(now, '%H:%M:%S')
        checktime = d.strptime(date_time, '%H:%M')
        return (checktime - now).total_seconds()

    def onInput_onStart(self):
        timedate = self.select_timedate(limit=2)
        if timedate is None:
            self.tts.post.say("本日のバスは終了しました")  # ←追記
            return

        for basedate in timedate:
            bas_type = basedate[0]
            direction = basedate[1]
            minute = self.remaining_second(date_time=basedate[2])
            minute = int(minute) / 60
            minute = str(minute)
            say = bas_type + '、、、'
            say += direction + '行きが後、'
            say += minute + '分'
            say += 'で参ります'
            self.tts.post.say(say)  # ←追記
        self.onStopped()
        pass

    def onInput_onStop(self):
        self.onUnload(
        )  #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped()  #activate the output of the box
