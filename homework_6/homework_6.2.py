def create_time_checker(max_time):
    def time_checker(time):
        if time > max_time:
            print("Установленный лимит по времени превышен!")
        else:
            print("Установленный лимит по времени не превышен!")
    return time_checker

checker_1 = create_time_checker(10)
checker_2 = create_time_checker(30)

checker_1(9)
checker_1(19)
checker_2(23)
checker_2(31)