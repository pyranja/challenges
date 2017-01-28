#!/usr/bin/env python3
import sys
import logging

"""translate integers to words"""


def solve(n):
    if n == 0:
        return 'Zero'
    result = []
    position = 0
    while n > 0:
        current = n % 1000
        if position > 0 and current != 0:
            result.append(MAGNITUDES[position])
        result.extend(triplet(current))
        logging.info("result is now %s", result)
        n //= 1000
        position += 1
    result.reverse()
    return ' '.join(result)


SINGLE_DIGIT = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
TEEN_WORDS = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen',
              'Eighteen', 'Nineteen']
BELOW_TWENTY = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five',
                'Six', 'Seven', 'Eight', 'Nine',
                'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
                'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
TWO_DIGIT = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty',
             'Ninety']
MAGNITUDES = ['', 'Thousand', 'Million', 'Billion', 'Trillion']


def triplet(it):
    """translate an up to three digit number 0 <= <= 999"""
    assert 0 <= it < 1000, "illegal call triplet(%s)" % it
    logging.info("translating triplet %d", it)
    if it == 0:
        return []
    result = []
    result.extend(duet(it % 100))
    if it >= 100:
        result.extend(["Hundred", BELOW_TWENTY[it // 100]])
    return result


def duet(it):
    assert 0 <= it < 100, "illegal call duet(%s)" % it
    if it == 0:
        return []
    if it < 20:
        return [BELOW_TWENTY[it]]
    if it % 10 == 0:
        return [TWO_DIGIT[(it // 10)]]
    return [BELOW_TWENTY[it % 10], TWO_DIGIT[(it // 10)]]


# ========================================= boilerplate ========================================== #

def main(cases):
    return '\n'.join([str(solve(int(case))) for case in cases])


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARN)
    print(main(sys.stdin.readlines()[1:]))
