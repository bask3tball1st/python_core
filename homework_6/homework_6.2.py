max_time = 30

def create_time_checker():
    def time_checker(time):
        if time >= max_time:
            print("Превышен установленный лимит по времени!")
        else:
            print("Непревышен установленный лимит по времени!")
    return time_checker

func = create_time_checker()
func(10)
func(31)