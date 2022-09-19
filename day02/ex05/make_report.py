#!/usr/bin/env python3
import analytics
import config


def main():
    try:
        file_name, header = config.parameters()

        r = analytics.Research(file_name, header)
        file = r.file_reader()

        counter = r.Calculations(file)
        amount = counter.counts()
        fractions = counter.fractions(amount)

        analys = r.Analytics(file)
        rand = analys.predict_random(config.num_of_steps)
        rand_res = analys.count_random(rand)

        message = config.message(len(file), amount, fractions, rand_res)
        res_name = config.file_result_data()
        analys.save_file(res_name, message)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
