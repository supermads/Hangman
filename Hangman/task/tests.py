from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class CoffeeMachineTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin='python', attach=(True, 'python')),
            TestCase(stdin='java', attach=(False, 'java')),
            TestCase(stdin='pyton', attach=(False, '')),
            TestCase(stdin='python', attach=(True, '')),
        ]

    def check(self, reply: str, attach: Any) -> CheckResult:

        right_ans, guess = attach

        survived = 'You survived!'
        hanged = 'You are hanged!'

        if survived in reply and hanged in reply:
            return CheckResult.wrong(
                f'Looks like your output contains both \"{survived}\"'
                f' and \"{hanged}\". You should output only one of them.')

        if survived not in reply and hanged not in reply:
            return CheckResult.wrong(
                f'Looks like your output doesn\'t contain neither \"{survived}\"'
                f' nor \"{hanged}\". You should output one of them.')

        if right_ans:
            if survived in reply:
                return CheckResult.correct()

            if guess:
                return CheckResult.wrong(
                    'input: ' + 'python\n'
                    'correct output: ' + survived
                )

            else:
                return CheckResult.wrong('')

        else:
            if hanged in reply:
                return CheckResult.correct()

            if guess:
                return CheckResult.wrong(
                    'input: ' + 'java\n'
                    'correct output: ' + hanged
                )

            else:
                return CheckResult.wrong('')


if __name__ == '__main__':
    CoffeeMachineTest('hangman.hangman').run_tests()
