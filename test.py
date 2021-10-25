import schedule, subprocess, time as t

def _change_led_on(place):
    print('on {}'.format(place))


def _change_led_off(place):
    print('off {}'.format(place))

def add_job(action, time, place, day):
        """
        adds a new scheduled task/job
        """
        if(time == None):
            return

        action_switch = {
            1 : _change_led_off,
            2 : _change_led_on
        }

        weekday_switch = {
            1: schedule.every().monday.at(time).do(action_switch[action], place),
            2: schedule.every().tuesday.at(time).do(action_switch[action], place),
            3: schedule.every().wednesday.at(time).do(action_switch[action], place),
            4: schedule.every().thursday.at(time).do(action_switch[action], place),
            5: schedule.every().friday.at(time).do(action_switch[action], place),
            6: schedule.every().saturday.at(time).do(action_switch[action], place),
            7: schedule.every().sunday.at(time).do(action_switch[action], place)
        }

        job = weekday_switch[day]

        print(job)

        return job



tasks = list()
time = "18:46"
action = 2
place = "10.3.141.103"
day = 4

add_job(action, time, place, day)


print(len(schedule.jobs))

while True:
    schedule.run_pending()
    t.sleep(1)

